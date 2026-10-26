# requestExport(for:token:completionHandler:)

**Framework**: BrowserKit  
**Kind**: method  
**Role**: Instance Method

Requests that the system display the browsing-data transfer sheet to export data to another browser.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
func requestExport(for metadata: BEExportMetadata, token: UUID?, completionHandler: @escaping @Sendable (BEExportOptions?, (any Error)?) -> Void)
```

```swift
func requestExport(for metadata: BEExportMetadata, token: UUID?) async throws -> BEExportOptions
```

```objc
- (void) requestExportForMetadata:(BEExportMetadata *) metadata token:(NSUUID *) token completionHandler:(void (^)(BEExportOptions *, NSError *)) completionHandler;
```

## Mentions

- [Transferring browsing data to another browser](../transferring-browsing-data-to-another-browser.md)

#### Discussion

This method provides your completion handler with an object that describes the types of browsing data someone exports, and also indicates whether the export needs to send data to files rather than directly to another browser on the device.

## Parameters

- `metadata`: Metadata that describes the available data for export, including types, counts, and whether the sheet can include the option to export the data to files instead of directly to another browser.
- `token`: A UUID that identifies the export operation. Pass `nil` if your app presents the export sheet through a person’s interaction with your app’s UI. If the system launches your app with the [`userActivityType`](./useractivitytype-4ar5j.md) activity, pass the token you retrieve from the activity’s info dictionary using the [`exportTokenUserInfoKey`](./exporttokenuserinfokey-1y5l1.md).
- `completionHandler`: A closure that the system calls, passing in export options that contain the person’s selections in the sheet.

## See Also

### Exporting browser data
- [func exportBrowserData(AsyncStream<BEBrowserData>) async throws](./exportbrowserdata%28_%29.md)
  Exports the given browser data.
- [- exportBrowserData:completionHandler:](./exportbrowserdata_completionhandler_.md)
  Exports the given browser data with the given completion handler.
- [- exportFinishedWithCompletionHandler:](./exportfinishedwithcompletionhandler_.md)
  A callback the system invokes when an export of browsing data completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/requestexport(for:token:completionhandler:))*