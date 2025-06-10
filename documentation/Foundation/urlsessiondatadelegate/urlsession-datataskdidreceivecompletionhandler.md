# urlSession(_:dataTask:didReceive:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Tells the delegate that the data task received the initial reply (headers) from the server.

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
optional func urlSession(_ session: URLSession, dataTask: URLSessionDataTask, didReceive response: URLResponse) async -> URLSession.ResponseDisposition
```

## Mentions

- [Fetching website data into memory](fetching-website-data-into-memory.md)

#### Discussion

Implementing this method is optional unless you need to cancel the transfer or convert it to a download task when the response headers are first received. If you don’t provide this delegate method, the session always allows the task to continue.

You also implement this method if you need to support the fairly obscure `multipart/x-mixed-replace` content type. With that content type, the server sends a series of parts, each of which is intended to replace the previous part. The session calls this method at the beginning of each part, followed by one or more calls to [`urlSession(_:dataTask:didReceive:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:).md) with the contents of that part.

Each time the [`urlSession(_:dataTask:didReceive:completionHandler:)`](urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:).md) method is called for a part, collect the data received for the previous part (if any) and process the data as needed for your application. This processing can include storing the data to the filesystem, parsing it into custom types, or displaying it to the user. Next, begin receiving the next part by calling the completion handler with the [`URLSession.ResponseDisposition.allow`](urlsession/responsedisposition/allow.md) constant. Finally, if you have also implemented [`urlSession(_:task:didCompleteWithError:)`](urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:).md), the session will call it after sending all the data for the last part.

## Parameters

- `session`: The session containing the data task that received an initial reply.
- `dataTask`: The data task that received an initial reply.
- `response`: A URL response object populated with headers.
- `completionHandler`: A completion handler that your code calls to continue a transfer, passing a   constant to indicate whether the transfer should continue as a data task or should become a download task.

## See Also

- [URLSession.ResponseDisposition](urlsession/responsedisposition.md)
  Constants indicating how a data or upload session should proceed after receiving the initial headers.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionDownloadTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-60op5.md)
  Tells the delegate that the data task was changed to a download task.
- [func urlSession(URLSession, dataTask: URLSessionDataTask, didBecome: URLSessionStreamTask)](urlsessiondatadelegate/urlsession(_:datatask:didbecome:)-7nqzu.md)
  Tells the delegate that the data task was changed to a stream task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondatadelegate/urlsession(_:datatask:didreceive:completionhandler:))*