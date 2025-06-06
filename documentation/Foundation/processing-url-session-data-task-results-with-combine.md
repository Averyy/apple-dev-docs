# Processing URL session data task results with Combine

**Framework**: Foundation

Use a chain of asynchronous operators to receive and process data fetched from a URL.

#### Overview

Performing tasks with URL sessions is inherently asynchronous; it takes time to fetch data from network endpoints, file systems, and other URL-based sources. The URL Loading System accounts for this by delivering results asynchronously to delegates or completion handlers. The [`Combine`](https://developer.apple.com/documentation/Combine) framework also handles asynchronicity; using it to process your URL task results simplifies and empowers your code.

##### Create a Data Task Publisher

[`URLSession`](urlsession.md) offers a Combine publisher, [`URLSession.DataTaskPublisher`](urlsession/datataskpublisher.md), which publishes the results of fetching data from a [`URL`](url.md) or [`URLRequest`](urlrequest.md). You create this publisher with the method [`dataTaskPublisher(for:)`](urlsession/datataskpublisher(for:)-5kiir.md). When the task completes, it publishes either:

- A tuple that contains the fetched data and a [`URLResponse`](urlresponse.md), if the task succeeds.
- An error, if the task fails.

Unlike the completion handler passed to [`dataTask(with:completionHandler:)`](urlsession/datatask(with:completionhandler:)-52wk8.md), the types received by your code aren’t optionals, since the publisher has already unwrapped the data or error.

When using [`URLSession`](urlsession.md)’s completion handler-based code, you need to do all your work in the handler closure: error-handling, data parsing, and so on. When you instead use the data task publisher, you can move many of these responsibilities to Combine operators.

##### Convert Incoming Raw Data to Your Types with Combine Operators

When a data task completes successfully, it delivers a block of raw [`Data`](data.md) to your app. Most apps need to convert this data to their own types. Combine provides operators to perform these conversions, allowing you to declare a chain of processing operations.

The data task publisher produces a tuple that contains a [`Data`](data.md) and a [`URLResponse`](urlresponse.md). You can use the [`map(_:)`](https://developer.apple.com/documentation/Combine/Publisher/map(_:)-99evh) operator to convert the contents of this tuple to another type. If you want to inspect the response before inspecing the data, use [`tryMap(_:)`](https://developer.apple.com/documentation/Combine/Publisher/tryMap(_:)) and throw an error if the response is unacceptable.

To convert raw data to your own types that conform to the [`Decodable`](https://developer.apple.com/documentation/Swift/Decodable) protocol, use Combine’s [`decode(type:decoder:)`](https://developer.apple.com/documentation/Combine/Publisher/decode(type:decoder:)) operator.

The following example combines both these operators to parse JSON data from a URL endpoint into a custom `User` type:

```swift
struct User: Codable {
    let name: String
    let userID: String
}
let url = URL(string: "https://example.com/endpoint")!
cancellable = urlSession
    .dataTaskPublisher(for: url)
    .tryMap() { element -> Data in
        guard let httpResponse = element.response as? HTTPURLResponse,
            httpResponse.statusCode == 200 else {
                throw URLError(.badServerResponse)
            }
        return element.data
        }
    .decode(type: User.self, decoder: JSONDecoder())
    .sink(receiveCompletion: { print ("Received completion: \($0).") },
          receiveValue: { user in print ("Received user: \(user).")})
```

##### Retry Transient Errors and Catch and Replace Persistent Errors

Any app that uses the network should expect to encounter errors, and your app should handle them gracefully. Because transient network errors are fairly common, you may want to immediately retry a failed data task. With [`URLSession`](urlsession.md)‘s completion handler idiom, you need to create a whole new task to perform a retry. With the data task publisher, you can instead use Combine’s [`retry(_:)`](https://developer.apple.com/documentation/Combine/Publisher/retry(_:)) operator. This handles errors by recreating the subscription to the upstream publisher a specified number of times. However, since network operations are expensive, only retry a small number of times, and ensure all requests are idempotent.

You can also use Combine operators to replace the error, rather than letting it reach the subscriber:

- [`catch(_:)`](https://developer.apple.com/documentation/Combine/Publisher/catch(_:)) replaces the error with another publisher. You can use this with another [`URLSession.DataTaskPublisher`](urlsession/datataskpublisher.md), such as one that loads data from a fallback URL.
- [`replaceError(with:)`](https://developer.apple.com/documentation/Combine/Publisher/replaceError(with:)) replaces the error with an element you provide. If it makes sense in your application, you can use this to provide a substitute for the value you expected to load from the URL.

The following example shows both of these techniques, retrying a failed request once, and using a fallback URL after that. If either the original request, the retry, or the fallback request succeeds, the [`sink(receiveValue:)`](https://developer.apple.com/documentation/Combine/Publisher/sink(receiveValue:)) operator receives data from the endpoint. If all three fail, the sink receives a [`Subscribers.Completion.failure(_:)`](https://developer.apple.com/documentation/Combine/Subscribers/Completion/failure(_:)).

```swift
let pub = urlSession
    .dataTaskPublisher(for: url)
    .retry(1)
    .catch() { _ in
        self.fallbackUrlSession.dataTaskPublisher(for: fallbackURL)
    }
cancellable = pub
    .sink(receiveCompletion: { print("Received completion: \($0).") },
          receiveValue: { print("Received data: \($0.data).") })
```

##### Move Work Between Dispatch Queues with Scheduling Operators

When using [`URLSession`](urlsession.md)’s delegate and completion handler idioms, the session calls back to your code on a fixed [`delegateQueue`](urlsession/delegatequeue.md). Sometimes, this means your callback code has to manually use dispatch queues or other scheduling APIs to put work on a specific queue.

With [`URLSession.DataTaskPublisher`](urlsession/datataskpublisher.md), you can use Combine’s scheduling operators instead. Use [`receive(on:options:)`](https://developer.apple.com/documentation/Combine/Publisher/receive(on:options:)) to specify how you want later operators in the chain and your subscriber, to schedule the work. [`DispatchQueue`](https://developer.apple.com/documentation/Dispatch/DispatchQueue) and [`RunLoop`](runloop.md) both implement Combine’s [`Scheduler`](https://developer.apple.com/documentation/Combine/Scheduler) protocol, so you can use them to receive URL session data. The following snippet ensures that the sink logs its results on the main dispatch queue.

```swift
cancellable = urlSession
    .dataTaskPublisher(for: url)
    .receive(on: DispatchQueue.main)
    .sink(receiveCompletion: { print ("Received completion: \($0).") },
          receiveValue: { print ("Received data: \($0.data).")})
```

##### Share the Result of a Data Task Publisher with Multiple Subscribers

You may want to use data from the URL endpoint in different parts of your application. Because network requests are expensive, don’t reissue them needlessly. Combine lets you use multiple subscribers to a single [`URLSession.DataTaskPublisher`](urlsession/datataskpublisher.md), while allowing the publisher to service all of them with a single request.

To support multiple downstream subscribers, use the [`share()`](https://developer.apple.com/documentation/Combine/Publisher/share()) operator. This operator works like a combination of the [`Publishers.Multicast`](https://developer.apple.com/documentation/Combine/Publishers/Multicast) and [`PassthroughSubject`](https://developer.apple.com/documentation/Combine/PassthroughSubject) publishers. You can connect multiple operator chains or subscribers to the [`share()`](https://developer.apple.com/documentation/Combine/Publisher/share()) operator, and any upstream publisher only sees one downstream. In the case of a [`URLSession.DataTaskPublisher`](urlsession/datataskpublisher.md), this means it only performs the data task once.

The following example uses a URL session data task for two unrelated purposes. One subscriber uses the returned data to parse the custom `User` type seen earlier, and logs it on the main dispatch queue. A second subscriber is only concerned with the [`URLResponse`](urlresponse.md), which it inspects to print an HTTP status code, and doesn’t care which queue it uses. By using [`share()`](https://developer.apple.com/documentation/Combine/Publisher/share()), the data task publisher can serve both subscribers with a single load from the URL endpoint.

```swift
let sharedPublisher = urlSession
    .dataTaskPublisher(for: url)
    .share()

cancellable1 = sharedPublisher
    .tryMap() {
        guard $0.data.count > 0 else { throw URLError(.zeroByteResource) }
        return $0.data
    }
    .decode(type: User.self, decoder: JSONDecoder())
    .receive(on: DispatchQueue.main)
    .sink(receiveCompletion: { print ("Received completion 1: \($0).") },
          receiveValue: { print ("Received id: \($0.userID).")})

cancellable2 = sharedPublisher
    .map() {
        $0.response
    }
    .sink(receiveCompletion: { print ("Received completion 2: \($0).") },
           receiveValue: { response in
            if let httpResponse = response as? HTTPURLResponse {
                print ("Received HTTP status: \(httpResponse.statusCode).")
            } else {
                print ("Response was not an HTTPURLResponse.")
            }
    }
)

```

To prove that this code only loads the data once, temporarily put a [`print(_:to:)`](https://developer.apple.com/documentation/Combine/Publisher/print(_:to:)) debugging operator before the [`share()`](https://developer.apple.com/documentation/Combine/Publisher/share()) operator. When the app runs, Xcode’s console output shows it receives only a single value from the data task publisher, even though both subscribers receive their expected results.

Be aware that the URL session starts loading data as soon as the [`URLSession.DataTaskPublisher`](urlsession/datataskpublisher.md) has unsatisfied demand from a downstream subscriber. In this case, that happens when the first sink subscriber attaches. If you need extra time to attach other subscribers, use [`makeConnectable()`](https://developer.apple.com/documentation/Combine/Publisher/makeConnectable()) to wrap the [`Publishers.Share`](https://developer.apple.com/documentation/Combine/Publishers/Share) publisher with a [`ConnectablePublisher`](https://developer.apple.com/documentation/Combine/ConnectablePublisher). After connecting all subscribers, call [`connect()`](https://developer.apple.com/documentation/Combine/ConnectablePublisher/connect()) on the connectable publisher to allow the data load to begin.

## See Also

- [func dataTaskPublisher(for: URLRequest) -> URLSession.DataTaskPublisher](urlsession/datataskpublisher(for:)-61v3e.md)
  Returns a publisher that wraps a URL session data task for a given URL request.
- [func dataTaskPublisher(for: URL) -> URLSession.DataTaskPublisher](urlsession/datataskpublisher(for:)-5kiir.md)
  Returns a publisher that wraps a URL session data task for a given URL.
- [URLSession.DataTaskPublisher](urlsession/datataskpublisher.md)
  A publisher that delivers the results of performing URL session data tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processing-url-session-data-task-results-with-combine)*