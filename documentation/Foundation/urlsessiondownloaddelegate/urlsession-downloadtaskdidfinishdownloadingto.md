# urlSession(_:downloadTask:didFinishDownloadingTo:)

**Framework**: Foundation  
**Kind**: method  
**Required**: Yes

Tells the delegate that a download task has finished downloading.

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
func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL)
```

## Mentions

- [Downloading files from websites](downloading-files-from-websites.md)
- [Downloading files in the background](downloading-files-in-the-background.md)

## Parameters

- `session`: The session containing the download task that finished.
- `downloadTask`: The download task that finished.
- `location`: If you choose to open the file for reading, you should do the actual reading in another thread to avoid blocking the delegate queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/urlsessiondownloaddelegate/urlsession(_:downloadtask:didfinishdownloadingto:))*