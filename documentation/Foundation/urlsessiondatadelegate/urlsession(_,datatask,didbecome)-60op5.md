# urlSession(_:dataTask:didBecome:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the data task was changed to a download task.

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
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didBecome downloadTask: URLSessionDownloadTask)
```

```objc
- (void) URLSession:(NSURLSession *) session dataTask:(NSURLSessionDataTask *) dataTask didBecomeDownloadTask:(NSURLSessionDownloadTask *) downloadTask;
```

#### Discussion

When your [`urlSession(_:dataTask:didReceive:completionHandler:)`](./urlsession%28_,datatask,didreceive,completionhandler%29.md) delegate method uses the [`URLSession.ResponseDisposition.becomeDownload`](../urlsession/responsedisposition/becomedownload.md) disposition to convert the request to use a download, the session calls this delegate method to provide you with the new download task. After this call, the session delegate receives no further delegate method calls related to the original data task.

## Parameters

- `session`: The session containing the task that was replaced by a download task.
- `dataTask`: The data task that was replaced by a download task.
- `downloadTask`: The new download task that replaced the data task.

## See Also

### Handling task life cycle changes
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didReceive: URLResponse, completionHandler: (URLSession.ResponseDisposition) -> Void)](./urlsession%28_,datatask,didreceive,completionhandler%29.md)
  Tells the delegate that the data task received the initial reply (headers) from the server.
- [URLSession.ResponseDisposition](../urlsession/responsedisposition.md)
  Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionStreamTask)](./urlsession%28_,datatask,didbecome%29-7nqzu.md)
  Tells the delegate that the data task was changed to a stream task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5)*