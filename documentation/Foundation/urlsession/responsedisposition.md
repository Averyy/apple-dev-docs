# URLSession.ResponseDisposition

**Framework**: Foundation  
**Kind**: enum

Constants indicating how a data or upload session should proceed after receiving the initial headers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum ResponseDisposition
```

#### Overview

When a data or upload task first receives a response, it calls the  [`urlSession(_:dataTask:didReceive:completionHandler:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md) method of [`URLSessionDataDelegate`](urlsessiondatadelegate.md). Implement this method to inspect the received [`URLResponse`](urlresponse.md) and then call the provided completion handler. The first parameter to the completion handler is of this type, a disposition that tells the task how to proceed.

## Topics

### Task dispositions
- [URLSession.ResponseDisposition.cancel](urlsession/responsedisposition/cancel.md)
  Cancel the load.
- [URLSession.ResponseDisposition.allow](urlsession/responsedisposition/allow.md)
  Allow the load operation to continue.
- [URLSession.ResponseDisposition.becomeDownload](urlsession/responsedisposition/becomedownload.md)
  Convert the response for this request to use a [`URLSessionDownloadTask`](urlsessiondownloadtask.md).
- [URLSession.ResponseDisposition.becomeStream](urlsession/responsedisposition/becomestream.md)
  Convert the response for this request to use a [`URLSessionStreamTask`](urlsessionstreamtask.md).
### Initializers
- [init?(rawValue: Int)](urlsession/responsedisposition/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func urlSession(URLSession, dataTask: URLSessionDataTask, didReceive: URLResponse, completionHandler: (URLSession.ResponseDisposition) -> Void)](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md)
  Tells the delegate that the data task received the initial reply (headers) from the server.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionDownloadTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5.md)
  Tells the delegate that the data task was changed to a download task.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionStreamTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-7nqzu.md)
  Tells the delegate that the data task was changed to a stream task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition)*