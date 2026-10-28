# exportBrowserData:completionHandler:

**Framework**: BrowserKit  
**Kind**: method  
**Role**: Instance Method

Exports the given browser data with the given completion handler.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```objc
- (void) exportBrowserData:(BEBrowserData *) browserData completionHandler:(void (^)(NSError *)) completionHandler;
```

## Discussion

Call this method to stream browsing data to the system, as identified by [`dataTypes`](../beexportoptions/datatypes-swift.property.md).

Use this method after [`requestExport(for:token:completionHandler:)`](./requestexport%28for,token,completionhandler%29.md) returns an [`BEExportOptions`](../beexportoptions.md) with [`exportToFiles`](../beexportoptions/exporttofiles.md) = `false`, or when the system launches your app as part of the transfer of browsing data to another browser.

For more information, see [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md).

## Parameters

- `browserData`: An asynchronous stream of browser data items to export.
- `completionHandler`: A closure that the system calls when the export completes or fails.

## See Also

### Exporting browser data
- [func requestExport(for: BEExportMetadata, token: UUID?, completionHandler: (BEExportOptions?, (any Error)?) -> Void)](./requestexport%28for,token,completionhandler%29.md)
  Requests that the system display the browsing-data transfer sheet to export data to another browser.
- [- exportFinishedWithCompletionHandler:](./exportfinishedwithcompletionhandler_.md)
  A callback the system invokes when an export of browsing data completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/exportbrowserdata:completionhandler:)*