# URLSession.ResponseDisposition.becomeDownload

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

Convert the response for this request to use a [`URLSessionDownloadTask`](../../urlsessiondownloadtask.md).

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
case becomeDownload
```

```c
NSURLSessionResponseBecomeDownload
```

## Discussion

When used with the completion handler from [`urlSession(_:dataTask:didReceive:completionHandler:)`](../../urlsessiondatadelegate/urlsession%28_,datatask,didreceive,completionhandler%29.md), this disposition converts the data task to a download task. This will result in your delegate’s [`urlSession(_:dataTask:didBecome:)`](../../urlsessiondatadelegate/urlsession%28_,datatask,didbecome%29-60op5.md) being called to provide you with the new download task that supersedes the current task.

## See Also

### Task dispositions
- [URLSession.ResponseDisposition.cancel](./cancel.md)
  Cancel the load.
- [URLSession.ResponseDisposition.allow](./allow.md)
  Allow the load operation to continue.
- [URLSession.ResponseDisposition.becomeStream](./becomestream.md)
  Convert the response for this request to use a [`URLSessionStreamTask`](../../urlsessionstreamtask.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/responsedisposition/becomedownload)*