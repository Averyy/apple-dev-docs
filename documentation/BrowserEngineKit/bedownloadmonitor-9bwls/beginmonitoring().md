# beginMonitoring()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Informs the system to start monitoring the download.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
(beginMonitoring:) func beginMonitoring() async throws -> BEDownloadMonitor.Location?
```

## Mentions

- [Downloading files in a web browser with an alternative browser engine](../downloading-files-in-a-web-browser.md)

#### Return Value

If you called [`useDownloadsFolder(placeholderType:finalFileCreatedHandler:)`](./usedownloadsfolder%28placeholdertype,finalfilecreatedhandler%29.md), this method returns the placeholder location that the system creates to host the downloaded content; otherwise, it returns `nil`.

## See Also

### Reporting progress to the system
- [func resumeMonitoring(placeholderURL: URL) async throws](./resumemonitoring%28placeholderurl%29.md)
  Informs the system that it needs to resume monitoring the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/beginmonitoring())*