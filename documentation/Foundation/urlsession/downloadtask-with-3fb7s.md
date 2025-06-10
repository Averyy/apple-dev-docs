# downloadTask(with:)

**Framework**: Foundation  
**Kind**: method

Creates a download task that retrieves the contents of a URL based on the specified URL request object and saves the results to a file.

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
func downloadTask(with request: URLRequest) -> URLSessionDownloadTask
```

## Mentions

- [Downloading files from websites](downloading-files-from-websites.md)
- [Downloading files in the background](downloading-files-in-the-background.md)

#### Return Value

The new session download task.

#### Discussion

By creating a task based on a request object, you can tune various aspects of the task’s behavior, including the cache policy and timeout interval.

After you create the task, you must start it by calling its [`resume()`](urlsessiontask/resume().md) method. The task calls methods on the session’s delegate to provide you with progress notifications, the location of the resulting temporary file, and so on.

## Parameters

- `request`: A URL request object that provides the URL, cache policy, request type, body data or body stream, and so on.

## See Also

- [func downloadTask(with: URL) -> URLSessionDownloadTask](urlsession/downloadtask(with:)-1onj.md)
  Creates a download task that retrieves the contents of the specified URL and saves the results to a file.
- [func downloadTask(with: URL, completionHandler: (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask](urlsession/downloadtask(with:completionhandler:)-7cuje.md)
  Creates a download task that retrieves the contents of the specified URL, saves the results to a file, and calls a handler upon completion.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsession/downloadtask(with:)-3fb7s)*