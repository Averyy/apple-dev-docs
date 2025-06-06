# downloadTask(withResumeData:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func downloadTask(withResumeData resumeData: Data, completionHandler: @escaping (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask
```

## Mentions

- [Pausing and resuming downloads](pausing-and-resuming-downloads.md)

#### Return Value

The new session download task.

#### Discussion

By using a completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting data, response, or error inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

You should pass a `nil` completion handler  when creating tasks in sessions whose delegates include a [`urlSession(_:downloadTask:didFinishDownloadingTo:)`](urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:).md) method.

Your app can obtain a `resumeData` object in two ways:

- If your app cancels an existing transfer by calling [`cancel(byProducingResumeData:)`](urlsessiondownloadtask/cancel(byproducingresumedata:).md), the session object passes a `resumeData` object to the completion handler that you provided in that call.
- If a transfer fails, the session object provides an `NSError` object either to its delegate or to the task’s completion handler. In that object, the [`NSURLSessionDownloadTaskResumeData`](nsurlsessiondownloadtaskresumedata.md) key in the `userInfo` dictionary contains a `resumeData` object.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

If the request completes successfully, the `location` parameter of the completion handler block contains the location of the temporary file, and the `error` parameter is `nil`. If the request fails, the `location` parameter is `nil` and the `error` parameter contain information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

> **Note**:  A download can be resumed only if it is an HTTP or HTTPS `GET` request, and only if the remote server supports byte-range requests (with the `Range` header) and provides the `ETag` or `Last-Modified` header in its responses. A download may also restart if the file on the server has been modified, or if the temporary file has been deleted because of low disk space.

 A download can be resumed only if it is an HTTP or HTTPS `GET` request, and only if the remote server supports byte-range requests (with the `Range` header) and provides the `ETag` or `Last-Modified` header in its responses. A download may also restart if the file on the server has been modified, or if the temporary file has been deleted because of low disk space.

## Parameters

- `resumeData`: A data object that provides the data necessary to resume the download.
- `completionHandler`: If you pass  , only the session delegate methods are called when the task completes, making this method equivalent to the   method.

## See Also

- [func downloadTask(with: URL) -> URLSessionDownloadTask](urlsession/downloadtask(with:)-1onj.md)
  Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [func downloadTask(with: URL, completionHandler: (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask](urlsession/downloadtask(with:completionhandler:)-7cuje.md)
  Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
- [func downloadTask(with: URLRequest) -> URLSessionDownloadTask](urlsession/downloadtask(with:)-3fb7s.md)
  Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [func downloadTask(with: URLRequest, completionHandler: (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask](urlsession/downloadtask(with:completionhandler:)-4a84s.md)
  Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [func downloadTask(withResumeData: Data) -> URLSessionDownloadTask](urlsession/downloadtask(withresumedata:).md)
  Creates a download task to resume a previously canceled or failed download.
- [class URLSessionDownloadTask](urlsessiondownloadtask.md)
  A URL session task that stores downloaded data to a file.
- [protocol URLSessionDownloadDelegate](urlsessiondownloaddelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/downloadtask(withresumedata:completionhandler:))*