# NSURLSessionDownloadTaskResumeData

**Framework**: Foundation  
**Kind**: var  
**Role**: Global Variable

A key in the error dictionary that provides resume data.

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
let NSURLSessionDownloadTaskResumeData: String
```

```c
extern NSString * const NSURLSessionDownloadTaskResumeData;
```

## Mentions

- [Pausing and resuming downloads](./pausing-and-resuming-downloads.md)

#### Discussion

When a transfer error occurs or when you call the [`cancel(byProducingResumeData:)`](./urlsessiondownloadtask/cancel%28byproducingresumedata%29.md) method, the delegate object or completion handler gets an [`NSError`](./nserror.md) object. If the transfer is resumable, that error object’s `userInfo` dictionary contains a value for this key. To resume the transfer, your app can pass that value to the [`downloadTask(withResumeData:)`](./urlsession/downloadtask%28withresumedata%29.md) or [`downloadTask(withResumeData:completionHandler:)`](./urlsession/downloadtask%28withresumedata,completionhandler%29.md) method.

## See Also

### User info dictionary keys
- [let NSURLErrorBackgroundTaskCancelledReasonKey: String](./nsurlerrorbackgroundtaskcancelledreasonkey.md)
  A key in the error dictionary that provides the reason for canceling a background task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlsessiondownloadtaskresumedata)*