# urlSession(_:dataTask:didBecome:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the data task was changed to a stream task.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didBecome streamTask: URLSessionStreamTask)
```

#### Discussion

When your [`urlSession(_:dataTask:didReceive:completionHandler:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md) delegate method uses the [`URLSession.ResponseDisposition.becomeStream`](urlsession/responsedisposition/becomestream.md) disposition to convert the request to use a stream, the session calls this delegate method to provide you with the new stream task. After this call, the session delegate receives no further delegate method calls related to the original data task.

For requests that were pipelined, the stream task allows only reading, and the object  immediately sends the delegate message [`urlSession(_:writeClosedFor:)`](urlsessionstreamdelegate/urlsession(_:writeclosedfor:).md). You can disable pipelining for all requests in a session by setting the [`httpShouldUsePipelining`](urlsessionconfiguration/httpshouldusepipelining.md) property on its [`URLSessionConfiguration`](urlsessionconfiguration.md) object, or for individual requests  by setting the [`httpShouldUsePipelining`](nsurlrequest/httpshouldusepipelining.md) property on an [`NSURLRequest`](nsurlrequest.md) object.

## Parameters

- `session`: The session containing the task that was replaced by a stream task.
- `dataTask`: The data task that was replaced by a stream task.
- `streamTask`: The new stream task that replaced the data task.

## See Also

- [func urlSession(URLSession, dataTask: URLSessionDataTask, didReceive: URLResponse, completionHandler: (URLSession.ResponseDisposition) -> Void)](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md)
  Tells the delegate that the data task received the initial reply (headers) from the server.
- [URLSession.ResponseDisposition](urlsession/responsedisposition.md)
  Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionDownloadTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5.md)
  Tells the delegate that the data task was changed to a download task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-7nqzu)*