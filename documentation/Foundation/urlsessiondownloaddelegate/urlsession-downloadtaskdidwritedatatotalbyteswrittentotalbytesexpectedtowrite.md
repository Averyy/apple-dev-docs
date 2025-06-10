# urlSession(_:downloadTask:didWriteData:totalBytesWritten:totalBytesExpectedToWrite:)

**Framework**: Foundation  
**Kind**: method

Periodically informs the delegate about the download’s progress.

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
optional func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64)
```

## Mentions

- [Downloading files from websites](downloading-files-from-websites.md)

## Parameters

- `session`: The session containing the download task.
- `downloadTask`: The download task.
- `bytesWritten`: The number of bytes transferred since the last time this delegate method was called.
- `totalBytesWritten`: The total number of bytes transferred so far.
- `totalBytesExpectedToWrite`: The expected length of the file, as provided by the   header. If this header was not provided, the value is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didwritedata:totalbyteswritten:totalbytesexpectedtowrite:))*