# Processing URL session data task results with Combine

**Framework**: Foundation  
**Role**: Article

Use a chain of asynchronous operators to receive and process data fetched from a URL.

## Overview

Performing tasks with URL sessions is inherently asynchronous; it takes time to fetch data from network endpoints, file systems, and other URL-based sources. The URL Loading System accounts for this by delivering results asynchronously to delegates or completion handlers. The [Combine](../Combine/Combine.md) framework also handles asynchronicity; using it to process your URL task results simplifies and empowers your code.

### Create a data task publisher

[`URLSession`](./urlsession.md) offers a Combine publisher, [`URLSession.DataTaskPublisher`](./urlsession/datataskpublisher.md), which publishes the results of fetching data from a [`URL`](./url.md) or [`URLRequest`](./urlrequest.md). You create this publisher with the method [`dataTaskPublisher(for:)`](./urlsession/datataskpublisher%28for%29-5kiir.md). When the task completes, it publishes either:

- A tuple that contains the fetched data and a [`URLResponse`](./urlresponse.md), if the task succeeds.
- An error, if the task fails.

Unlike the completion handler passed to [`dataTask(with:completionHandler:)`](./urlsession/datatask%28with,completionhandler%29-52wk8.md), the types received by your code aren’t optionals, since the publisher has already unwrapped the data or error.

When using [`URLSession`](./urlsession.md)’s completion handler-based code, you need to do all your work in the handler closure: error-handling, data parsing, and so on. When you instead use the data task publisher, you can move many of these responsibilities to Combine operators.

### Convert incoming raw data to your types with Combine operators

When a data task completes successfully, it delivers a block of raw [`Data`](./data.md) to your app. Most apps need to convert this data to their own types. Combine provides operators to perform these conversions, allowing you to declare a chain of processing operations.

The data task publisher produces a tuple that contains a [`Data`](./data.md) and a [`URLResponse`](./urlresponse.md). You can use the [`map(_:)`](../Combine/publisher/map%28_%29-99evh.md) operator to convert the contents of this tuple to another type. If you want to inspect the response before inspecing the data, use [`tryMap(_:)`](../Combine/publisher/trymap%28_%29.md) and throw an error if the response is unacceptable.

To convert raw data to your own types that conform to the [`Decodable`](../Swift/decodable.md) protocol, use Combine’s [`decode(type:decoder:)`](../Combine/publisher/decode%28type,decoder%29.md) operator.

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

### Retry transient errors and catch and replace persistent errors

Any app that uses the network should expect to encounter errors, and your app should handle them gracefully. Because transient network errors are fairly common, you may want to immediately retry a failed data task. With [`URLSession`](./urlsession.md)‘s completion handler idiom, you need to create a whole new task to perform a retry. With the data task publisher, you can instead use Combine’s [`retry(_:)`](../Combine/publisher/retry%28_%29.md) operator. This handles errors by recreating the subscription to the upstream publisher a specified number of times. However, since network operations are expensive, only retry a small number of times, and ensure all requests are idempotent.

You can also use Combine operators to replace the error, rather than letting it reach the subscriber:

- [`catch(_:)`](../Combine/publisher/catch%28_%29.md) replaces the error with another publisher. You can use this with another [`URLSession.DataTaskPublisher`](./urlsession/datataskpublisher.md), such as one that loads data from a fallback URL.
- [`replaceError(with:)`](../Combine/publisher/replaceerror%28with%29.md) replaces the error with an element you provide. If it makes sense in your application, you can use this to provide a substitute for the value you expected to load from the URL.

The following example shows both of these techniques, retrying a failed request once, and using a fallback URL after that. If either the original request, the retry, or the fallback request succeeds, the [`sink(receiveValue:)`](../Combine/publisher/sink%28receivevalue%29.md) operator receives data from the endpoint. If all three fail, the sink receives a [`Subscribers.Completion.failure(_:)`](../Combine/subscribers/completion/failure%28_%29.md).

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

### Move work between dispatch queues with scheduling operators

When using [`URLSession`](./urlsession.md)’s delegate and completion handler idioms, the session calls back to your code on a fixed [`delegateQueue`](./urlsession/delegatequeue.md). Sometimes, this means your callback code has to manually use dispatch queues or other scheduling APIs to put work on a specific queue.

With [`URLSession.DataTaskPublisher`](./urlsession/datataskpublisher.md), you can use Combine’s scheduling operators instead. Use [`receive(on:options:)`](../Combine/publisher/receive%28on,options%29.md) to specify how you want later operators in the chain and your subscriber, to schedule the work. [`DispatchQueue`](../Dispatch/dispatchqueue.md) and [`RunLoop`](./runloop.md) both implement Combine’s [`Scheduler`](../Combine/scheduler.md) protocol, so you can use them to receive URL session data. The following snippet ensures that the sink logs its results on the main dispatch queue.

```swift
cancellable = urlSession
    .dataTaskPublisher(for: url)
    .receive(on: DispatchQueue.main)
    .sink(receiveCompletion: { print ("Received completion: \($0).") },
          receiveValue: { print ("Received data: \($0.data).")})
```

### Share the result of a data task publisher with multiple subscribers

You may want to use data from the URL endpoint in different parts of your application. Because network requests are expensive, don’t reissue them needlessly. Combine lets you use multiple subscribers to a single [`URLSession.DataTaskPublisher`](./urlsession/datataskpublisher.md), while allowing the publisher to service all of them with a single request.

To support multiple downstream subscribers, use the [`share()`](../Combine/publisher/share%28%29.md) operator. This operator works like a combination of the [`Publishers.Multicast`](../Combine/publishers/multicast.md) and [`PassthroughSubject`](../Combine/passthroughsubject.md) publishers. You can connect multiple operator chains or subscribers to the [`share()`](../Combine/publisher/share%28%29.md) operator, and any upstream publisher only sees one downstream. In the case of a [`URLSession.DataTaskPublisher`](./urlsession/datataskpublisher.md), this means it only performs the data task once.

The following example uses a URL session data task for two unrelated purposes. One subscriber uses the returned data to parse the custom `User` type seen earlier, and logs it on the main dispatch queue. A second subscriber is only concerned with the [`URLResponse`](./urlresponse.md), which it inspects to print an HTTP status code, and doesn’t care which queue it uses. By using [`share()`](../Combine/publisher/share%28%29.md), the data task publisher can serve both subscribers with a single load from the URL endpoint.

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

To prove that this code only loads the data once, temporarily put a [`print(_:to:)`](../Combine/publisher/print%28_,to%29.md) debugging operator before the [`share()`](../Combine/publisher/share%28%29.md) operator. When the app runs, Xcode’s console output shows it receives only a single value from the data task publisher, even though both subscribers receive their expected results.

Be aware that the URL session starts loading data as soon as the [`URLSession.DataTaskPublisher`](./urlsession/datataskpublisher.md) has unsatisfied demand from a downstream subscriber. In this case, that happens when the first sink subscriber attaches. If you need extra time to attach other subscribers, use [`makeConnectable()`](../Combine/publisher/makeconnectable%28%29.md) to wrap the [`Publishers.Share`](../Combine/publishers/share.md) publisher with a [`ConnectablePublisher`](../Combine/connectablepublisher.md). After connecting all subscribers, call [`connect()`](../Combine/connectablepublisher/connect%28%29.md) on the connectable publisher to allow the data load to begin.

## See Also

### Performing tasks as a Combine Publisher
- [func dataTaskPublisher(for: URLRequest) -> URLSession.DataTaskPublisher](./urlsession/datataskpublisher%28for%29-61v3e.md)
  Returns a publisher that wraps a URL session data task for a given URL request.
- [func dataTaskPublisher(for: URL) -> URLSession.DataTaskPublisher](./urlsession/datataskpublisher%28for%29-5kiir.md)
  Returns a publisher that wraps a URL session data task for a given URL.
- [URLSession.DataTaskPublisher](./urlsession/datataskpublisher.md)
  A publisher that delivers the results of performing URL session data tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/processing-url-session-data-task-results-with-combine)*