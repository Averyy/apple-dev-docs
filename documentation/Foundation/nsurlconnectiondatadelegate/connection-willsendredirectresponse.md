# connection(_:willSend:redirectResponse:)

**Framework**: Foundation  
**Kind**: method

Sent when the connection determines that it must change URLs in order to continue loading a request.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func connection(_ connection: NSURLConnection, willSend request: URLRequest, redirectResponse response: URLResponse?) -> URLRequest?
```

#### Return Value

The actual URL request to use in light of the redirection response. The delegate may return `request` unmodified to allow the redirect, return a new request, or return `nil` to reject the redirect and continue processing the connection.

#### Discussion

If `redirectResponse` is `nil`, the URL was canonicalized (rewritten into its standard form) by the [`URLProtocol`](urlprotocol.md) object handling the request. Update your user interface to show the standardized form of the URL, then return the original request unmodified.

Otherwise, to cancel the redirect, call the `connection` object’s `cancel` method, then return the provided request object.

To receive the body of the redirect response itself, return `nil` to cancel the redirect. The connection continues to process, eventually sending your delegate a `connectionDidFinishLoading` or `connection:didFailLoadingWithError:` message, as appropriate.

To redirect the request to a different URL, create a new request object and return it.

> ❗ **Important**:  Your delegate method is called on the thread where the connection is scheduled. If you call the `cancel` method, do so on that same thread.

The delegate should be prepared to receive this message multiple times.

## Parameters

- `connection`: The connection sending the message.
- `request`: The proposed redirected request. The delegate should inspect the redirected request to verify that it meets its needs, and create a copy with new attributes to return to the connection if necessary.
- `response`: The URL response that caused the redirect. May be   in cases where this method is called because of URL canonicalization.

## See Also

- [func connection(NSURLConnection, needNewBodyStream: URLRequest) -> InputStream?](nsurlconnectiondatadelegate/connection(_:neednewbodystream:).md)
  Called when an `NSURLConnection` needs to retransmit a request that has a body stream to provide a new, unopened stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:willsend:redirectresponse:))*