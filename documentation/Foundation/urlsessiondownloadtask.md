# URLSessionDownloadTask

**Framework**: Foundation  
**Kind**: class

A URL session task that stores downloaded data to a file.

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
class URLSessionDownloadTask
```

## Mentions

- [Pausing and resuming downloads](pausing-and-resuming-downloads.md)
- [Downloading files from websites](downloading-files-from-websites.md)
- [Fetching website data into memory](fetching-website-data-into-memory.md)

#### Overview

An [`URLSessionDownloadTask`](urlsessiondownloadtask.md) is a concrete subclass of [`URLSessionTask`](urlsessiontask.md), which provides most of the methods for this class.

Download tasks directly write the server’s response data to a temporary file, providing your app with progress updates as data arrives from the server. When you use download tasks in background sessions, these downloads continue even when your app is in the suspended state or otherwise not running.

You can pause (cancel) download tasks and resume them later (assuming the server supports doing so). You can also resume downloads that failed because of network connectivity problems.

##### Download Delegate Behavior

When you use a download task, your delegate receives several callbacks unique to download scenarios.

- During download, the session periodically calls the delegate’s [`urlSession(_:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:)`](urlsessiondownloaddelegate/urlsession(_:downloadtask:didwritedata:totalbyteswritten:totalbytesexpectedtowrite:).md) method with status information.
- Upon successful completion, the session calls the delegate’s [`urlSession(_:downloadTask:didFinishDownloadingTo:)`](urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:).md) method or completion handler. In that method, you must either open the file for reading or move it to a permanent location in your app’s sandbox container directory.
- Upon unsuccessful completion, the session calls the delegate’s [`urlSession(_:task:didCompleteWithError:)`](urlsessiontaskdelegate/urlsession(_:task:didcompletewitherror:).md) method or completion handler. The only errors your delegate receives through the `error` parameter are client-side errors, such as being unable to resolve the hostname or connect to the host. To check for server-side errors, inspect the [`response`](urlsessiontask/response.md) property of the `task` parameter received by this callback.

## Topics

### Canceling a download
- [func cancel(byProducingResumeData: (Data?) -> Void)](urlsessiondownloadtask/cancel(byproducingresumedata:).md)
  Cancels a download and calls a callback with resume data for later use.
### Creating download tasks
- [init()](urlsessiondownloadtask/init.md)
  Initializes a download task.
- [class func new() -> Self](urlsessiondownloadtask/new.md)
  Creates and initializes a download task.

## Relationships

### Inherits From
- [URLSessionTask](urlsessiontask.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](nscopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [ProgressReporting](progressreporting.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [func downloadTask(withResumeData: Data, completionHandler: (URL?, URLResponse?, (any Error)?) -> Void) -> URLSessionDownloadTask](urlsession/downloadtask(withresumedata:completionhandler:).md)
  Creates a download task to resume a previously canceled or failed download and calls a handler upon completion.
- [protocol URLSessionDownloadDelegate](urlsessiondownloaddelegate.md)
  A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloadtask)*