# exportBrowserData(_:)

**Framework**: BrowserKit  
**Kind**: method

Exports the given browser data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
@nonobjc
final func exportBrowserData(_ browserDataStream: AsyncStream<BEBrowserData>) async throws
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Discussion

Call this method to stream browsing data to the system, as identified by [`dataTypes`](beexportoptions/datatypes-swift.property.md).

Use this method after [`requestExport(for:token:completionHandler:)`](bebrowserdataexportmanager/requestexport(for:token:completionhandler:).md) returns an [`BEExportOptions`](beexportoptions.md) with [`exportToFiles`](beexportoptions/exporttofiles.md) = `false`, or when the system launches your app as part of the transfer of browsing data to another browser.

For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## Parameters

- `browserDataStream`: An asynchronous stream of browser data to export.

## See Also

- [func requestExport(for: BEExportMetadata, token: UUID?, completionHandler: (BEExportOptions?, (any Error)?) -> Void)](bebrowserdataexportmanager/requestexport(for:token:completionhandler:).md)
  Requests that the system display the browsing-data transfer sheet to export data to another browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager/exportbrowserdata(_:))*