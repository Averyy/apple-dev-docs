# exportFinishedWithCompletionHandler:

**Framework**: BrowserKit  
**Kind**: method  
**Role**: Instance Method

A callback the system invokes when an export of browsing data completes.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```objc
- (void) exportFinishedWithCompletionHandler:(void (^)(NSError *)) completionHandler;
```

## Parameters

- `completionHandler`: A closure that the system calls when the export completes or fails.

## See Also

### Exporting browser data
- [func requestExport(for: BEExportMetadata, token: UUID?, completionHandler: (BEExportOptions?, (any Error)?) -> Void)](./requestexport%28for,token,completionhandler%29.md)
  Requests that the system display the browsing-data transfer sheet to export data to another browser.
- [- exportBrowserData:completionHandler:](./exportbrowserdata_completionhandler_.md)
  Exports the given browser data with the given completion handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/exportfinishedwithcompletionhandler:)*