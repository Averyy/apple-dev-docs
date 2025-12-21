# URLSessionDownloadDelegate

**Framework**: Foundation  
**Kind**: protocol

A protocol that defines methods that URL session instances call on their delegates to handle task-level events specific to download tasks.

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
protocol URLSessionDownloadDelegate : URLSessionTaskDelegate
```

## Mentions

- [Downloading files from websites](downloading-files-from-websites.md)
- [Downloading files in the background](downloading-files-in-the-background.md)
- [Fetching website data into memory](fetching-website-data-into-memory.md)

#### Overview

In addition to the methods in this protocol, be sure to implement the methods in the [`URLSessionTaskDelegate`](urlsessiontaskdelegate.md) and [`URLSessionDelegate`](urlsessiondelegate.md) protocols to handle events common to all task types and session-level events, respectively.

> **Note**:  An [`URLSession`](urlsession.md) object need not have a delegate. If no delegate is assigned, a system-provided delegate is used, and you must provide a completion callback to obtain the data.

## Topics

### Handling download life cycle changes
- [func urlSession(URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo: URL)](urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:).md)
  Tells the delegate that a download task has finished downloading.
### Resuming paused downloads
- [func urlSession(URLSession, downloadTask: URLSessionDownloadTask, didResumeAtOffset: Int64, expectedTotalBytes: Int64)](urlsessiondownloaddelegate/urlsession(_:downloadtask:didresumeatoffset:expectedtotalbytes:).md)
  Tells the delegate that the download task has resumed downloading.
### Receiving progress updates
- [func urlSession(URLSession, downloadTask: URLSessionDownloadTask, didWriteData: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)](urlsessiondownloaddelegate/urlsession(_:downloadtask:didwritedata:totalbyteswritten:totalbytesexpectedtowrite:).md)
  Periodically informs the delegate about the download’s progress.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [URLSessionDelegate](urlsessiondelegate.md)
- [URLSessionTaskDelegate](urlsessiontaskdelegate.md)

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
- [class URLSessionDownloadTask](urlsessiondownloadtask.md)
  A URL session task that stores downloaded data to a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate)*