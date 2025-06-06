# retry(_:)

**Framework**: Combine  
**Kind**: method

Attempts to recreate a failed subscription with the upstream publisher up to the number of times you specify.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func retry(_ retries: Int) -> Publishers.Retry<Self>
```

#### Return Value

A publisher that attempts to recreate its subscription to a failed upstream publisher.

#### Discussion

Use [`retry(_:)`](publisher/retry(_:).md) to try a connecting to an upstream publisher after a failed connection attempt.

In the example below, a [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher) attempts to connect to a remote URL. If the connection attempt succeeds, it publishes the remote service’s HTML to the downstream publisher and completes normally. Otherwise, the retry operator attempts to reestablish the connection. If after three attempts the publisher still can’t connect to the remote URL, the [`catch(_:)`](publisher/catch(_:).md) operator replaces the error with a new publisher that publishes a “connection timed out” HTML page. After the downstream subscriber receives the timed out message, the stream completes normally.

```swift
struct WebSiteData: Codable {
    var rawHTML: String
}

let myURL = URL(string: "https://www.example.com")

cancellable = URLSession.shared.dataTaskPublisher(for: myURL!)
    .retry(3)
    .map({ (page) -> WebSiteData in
        return WebSiteData(rawHTML: String(decoding: page.data, as: UTF8.self))
    })
    .catch { error in
        return Just(WebSiteData(rawHTML: "<HTML>Unable to load page - timed out.</HTML>"))
}
.sink(receiveCompletion: { print ("completion: \($0)") },
      receiveValue: { print ("value: \($0)") }
 )

// Prints: The HTML content from the remote URL upon a successful connection,
//         or returns "<HTML>Unable to load page - timed out.</HTML>" if the number of retries exceeds the specified value.
```

After exceeding the specified number of retries, the publisher passes the failure to the downstream receiver.

## Parameters

- `retries`: The number of times to attempt to recreate the subscription.

## See Also

- [func assertNoFailure(String, file: StaticString, line: UInt) -> Publishers.AssertNoFailure<Self>](publishers/allsatisfy/assertnofailure(_:file:line:).md)
  Raises a fatal error when its upstream publisher fails, and otherwise republishes all received input.
- [func `catch`<P>((Self.Failure) -> P) -> Publishers.Catch<Self, P>](publishers/allsatisfy/catch(_:).md)
  Handles errors from an upstream publisher by replacing it with another publisher.
- [func tryCatch<P>((Self.Failure) throws -> P) -> Publishers.TryCatch<Self, P>](publishers/allsatisfy/trycatch(_:).md)
  Handles errors from an upstream publisher by either replacing it with another publisher or throwing a new error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/allsatisfy/retry(_:))*