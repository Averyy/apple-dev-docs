# beginMonitoring:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Informs the system to start monitoring the download.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```objc
- (void) beginMonitoring:(void (^)(BEDownloadMonitorLocation *placeholderLocation, NSError *error)) completion;
```

## Parameters

- `completion`: A closure the system calls when it finishes processing the request. If it succeeds, and you called [`useDownloadsFolderWithPlaceholderType:finalFileCreatedHandler:`](./usedownloadsfolderwithplaceholdertype_finalfilecreatedhandler_.md), the first parameter is the placeholder location that the system creates to host the downloaded content; otherwise, it’s `nil`. If it fails, the first parameter is `nil` and the second parameter is an error object that describes the failure.

## See Also

### Reporting progress to the system
- [- resumeMonitoring:completionHandler:](./resumemonitoring_completionhandler_.md)
  Informs the system that it needs to resume monitoring the download.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedownloadmonitor-9y4hu/beginmonitoring:)*