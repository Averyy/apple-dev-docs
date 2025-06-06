# resumeMonitoring(placeholderURL:)

**Framework**: BrowserEngineKit  
**Kind**: method

Informs the system that it needs to resume monitoring the download.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
@objc
(resumeMonitoring:completionHandler:) func resumeMonitoring(placeholderURL: URL) async throws
```

#### Discussion

Call this method when your browser resumes the download after an interruption, for example, someone cancels the download, or your networking extension encounters a network error.

## Parameters

- `placeholderURL`: The placeholder location your networking extension previously received when it called  .

## See Also

- [func beginMonitoring() async throws -> BEDownloadMonitor.Location?](bedownloadmonitor-9bwls/beginmonitoring.md)
  Informs the system to start monitoring the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9bwls/resumemonitoring(placeholderurl:))*