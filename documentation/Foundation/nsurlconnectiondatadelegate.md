# NSURLConnectionDataDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that most delegates of a URL connection implement to receive data associated with the connection.

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
protocol NSURLConnectionDataDelegate : NSURLConnectionDelegate
```

#### Overview

The `NSURLConnectionDataDelegate` protocol describes methods that should be implemented by the delegate for an instance of the [`NSURLConnection`](nsurlconnection.md) class. Many methods in this protocol existed as part of an informal protocol in previous versions of macOS and iOS.

In addition to the methods described in this protocol, an `NSURLConnection` delegate should also implement the methods described in the [`NSURLConnectionDelegate`](nsurlconnectiondelegate.md) protocol.

> **Note**:  If you are using `NSURLConnection` as part of Newsstand Kit on iOS, you should also implement the methods in the [`NSURLConnectionDownloadDelegate`](nsurlconnectiondownloaddelegate.md) protocol.

 If you are using `NSURLConnection` as part of Newsstand Kit on iOS, you should also implement the methods in the [`NSURLConnectionDownloadDelegate`](nsurlconnectiondownloaddelegate.md) protocol.

## Topics

### Handling Incoming Data
- [func connection(NSURLConnection, didReceive: URLResponse)](nsurlconnectiondatadelegate/connection(_:didreceive:)-8t66w.md)
  Sent when the connection has received sufficient data to construct the URL response for its request.
- [func connection(NSURLConnection, didReceive: Data)](nsurlconnectiondatadelegate/connection(_:didreceive:)-8p5vg.md)
  Sent as a connection loads data incrementally.
### Receiving Connection Progress
- [func connection(NSURLConnection, didSendBodyData: Int, totalBytesWritten: Int, totalBytesExpectedToWrite: Int)](nsurlconnectiondatadelegate/connection(_:didsendbodydata:totalbyteswritten:totalbytesexpectedtowrite:).md)
  Sent as the body (message data) of a request is transmitted (such as in an HTTP POST request).
- [func connectionDidFinishLoading(NSURLConnection)](nsurlconnectiondatadelegate/connectiondidfinishloading(_:).md)
  Sent when a connection has finished loading successfully.
### Handling Redirects
- [func connection(NSURLConnection, willSend: URLRequest, redirectResponse: URLResponse?) -> URLRequest?](nsurlconnectiondatadelegate/connection(_:willsend:redirectresponse:).md)
  Sent when the connection determines that it must change URLs in order to continue loading a request.
- [func connection(NSURLConnection, needNewBodyStream: URLRequest) -> InputStream?](nsurlconnectiondatadelegate/connection(_:neednewbodystream:).md)
  Called when an `NSURLConnection` needs to retransmit a request that has a body stream to provide a new, unopened stream.
### Overriding Caching Behavior
- [func connection(NSURLConnection, willCacheResponse: CachedURLResponse) -> CachedURLResponse?](nsurlconnectiondatadelegate/connection(_:willcacheresponse:).md)
  Sent before the connection stores a cached response in the cache, to give the delegate an opportunity to alter it.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSURLConnectionDelegate](nsurlconnectiondelegate.md)

## See Also

- [class NSURLConnection](nsurlconnection.md)
  An object that enables you to start and stop URL requests.
- [protocol NSURLConnectionDelegate](nsurlconnectiondelegate.md)
  A protocol that delegates of a URL connection implement to receive status about and provide feedback to the connection object.
- [protocol NSURLConnectionDownloadDelegate](nsurlconnectiondownloaddelegate.md)
  A protocol that delegates of a URL connection created with Newsstand Kit implement to receive data associated with a download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate)*