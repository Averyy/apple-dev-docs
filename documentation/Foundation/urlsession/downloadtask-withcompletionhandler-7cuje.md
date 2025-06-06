# downloadTask(with:completionHandler:)

**Framework**: Foundation  
**Kind**: method

Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.

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
func downloadTask(with url: URL, completionHandler: @escaping (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask
```

#### Return Value

The new session download task.

#### Discussion

By using the completion handler, the task bypasses calls to delegate methods for response and data delivery, and instead provides any resulting [`NSData`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169), [`URLResponse`](urlresponse.md), and [`NSError`](nserror.md) objects inside the completion handler. Delegate methods for handling authentication challenges, however, are still called.

You should pass a `nil` completion handler  when creating tasks in sessions whose delegates include a [`urlSession(_:downloadTask:didFinishDownloadingTo:)`](urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:).md) method.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method.

If the request completes successfully, the `location` parameter of the completion handler block contains the location of the temporary file, and the `error` parameter is `nil`. If the request fails, the `location` parameter is `nil` and the `error` parameter contain information about the failure. If a response from the server is received, regardless of whether the request completes successfully or fails, the `response` parameter contains that information.

## Parameters

- `url`: The URL to download.
- `completionHandler`: This completion handler takes the following parameters:

## See Also

- [func downloadTask(with: URL) -> URLSessionDownloadTask](urlsession/downloadtask(with:)-1onj.md)
  Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [func downloadTask(with: URLRequest) -> URLSessionDownloadTask](urlsession/downloadtask(with:)-3fb7s.md)
  Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.
- [func downloadTask(with: URLRequest, completionHandler: (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask](urlsession/downloadtask(with:completionhandler:)-4a84s.md)
  Creates a download task that retrieves the contents of a URL based on the specified URL request object, saves the results to a file, and calls a handler upon completion.
- [func downloadTask(withResumeData: Data) -> URLSessionDownloadTask](urlsession/downloadtask(withresumedata:).md)
  Creates a download task to resume a previously canceled or failed download.
- [func downloadTask(withResumeData: Data, completionHandler: (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask](urlsession/downloadtask(withresumedata:completionhandler:).md)
  Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [class URLSessionDownloadTask](urlsessiondownloadtask.md)
  A URL session task that stores downloaded data to a file.
- [protocol URLSessionDownloadDelegate](urlsessiondownloaddelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/downloadtask(with:completionhandler:)-7cuje)*