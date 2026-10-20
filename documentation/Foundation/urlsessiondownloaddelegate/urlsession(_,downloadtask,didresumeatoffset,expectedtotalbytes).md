# urlSession(_:downloadTask:didResumeAtOffset:expectedTotalBytes:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Tells the delegate that the download task has resumed downloading.

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
optional func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didResumeAtOffset fileOffset: Int64, expectedTotalBytes: Int64)
```

```objc
- (void) URLSession:(NSURLSession *) session downloadTask:(NSURLSessionDownloadTask *) downloadTask didResumeAtOffset:(int64_t) fileOffset expectedTotalBytes:(int64_t) expectedTotalBytes;
```

## Mentions

- [Pausing and resuming downloads](../pausing-and-resuming-downloads.md)

#### Discussion

If a resumable download task is canceled or fails, you can request a `resumeData` object that provides enough information to restart the download in the future. Later, you can call [`downloadTask(withResumeData:)`](../urlsession/downloadtask%28withresumedata%29.md) or [`downloadTask(withResumeData:completionHandler:)`](../urlsession/downloadtask%28withresumedata,completionhandler%29.md) with that data.

When you call those methods, you get a new download task. As soon as you resume that task, the session calls this method with that new task to indicate that the download is resumed.

## Parameters

- `session`: The session containing the download task that finished.
- `downloadTask`: The download task that resumed. See explanation in the discussion.
- `fileOffset`: If the file’s cache policy or last modified date prevents reuse of the existing content, then this value is zero. Otherwise, this value is an integer representing the number of bytes on disk that do not need to be retrieved again.

  > **Note**:  In some situations, it may be possible for the transfer to resume earlier in the file than where the previous transfer ended.
- `expectedTotalBytes`: The expected length of the file, as provided by the `Content-Length` header. If this header was not provided, the value is [`NSURLSessionTransferSizeUnknown`](../nsurlsessiontransfersizeunknown.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didresumeatoffset:expectedtotalbytes:))*