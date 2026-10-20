# connection(_:didReceive:)

**Framework**: Foundation  
**Kind**: method

Sent when the connection has received sufficient data to construct the URL response for its request.

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
optional func connection(_ connection: NSURLConnection, didReceive response: URLResponse)
```

#### Discussion

In rare cases, for example in the case of an HTTP load where the content type of the load data is `multipart/x-mixed-replace`, the delegate will receive more than one `connection:didReceiveResponse:` message. When this happens, discard (or process) all data previously delivered by `connection:didReceiveData:`, and prepare to handle the next part (which could potentially have a different MIME type).

The only case where this message is not sent to the delegate is when the protocol implementation encounters an error before a response could be created.

## Parameters

- `connection`: The connection sending the message.
- `response`: The URL response for the connection’s request. This object is immutable and will not be modified by the URL loading system once it is presented to the delegate.

## See Also

- [URL Loading System](url-loading-system.md)
  Interact with URLs and communicate with servers using standard Internet protocols.
- [func connection(NSURLConnection, didReceive: Data)](nsurlconnectiondatadelegate/connection(_:didreceive:)-8p5vg.md)
  Sent as a connection loads data incrementally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:didreceive:)-8t66w)*