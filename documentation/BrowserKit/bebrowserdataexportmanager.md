# BEBrowserDataExportManager

**Framework**: BrowserKit  
**Kind**: class

A class that handles exporting browsing data to other browsers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEBrowserDataExportManager
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Overview

This class coordinates the transfer of browsing data by presenting an *export sheet* when someone exports data through your app’s UI (see [`requestExport(for:token:completionHandler:)`](bebrowserdataexportmanager/requestexport(for:token:completionhandler:).md)). Call this class’s [`exportBrowserData:completionHandler:`](bebrowserdataexportmanager/exportbrowserdata:completionhandler:.md) to stream browsing data to the system. For more information and details about the export sheet, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## Topics

### Creating an export manager
- [init(scene: UIWindowScene)](bebrowserdataexportmanager/init(scene:).md)
  Initializes an export manager with your app’s window scene.
### Exporting browser data
- [func exportBrowserData(AsyncStream<BEBrowserData>) async throws](bebrowserdataexportmanager/exportbrowserdata(_:).md)
  Exports the given browser data.
- [func requestExport(for: BEExportMetadata, token: UUID?, completionHandler: (BEExportOptions?, (any Error)?) -> Void)](bebrowserdataexportmanager/requestexport(for:token:completionhandler:).md)
  Requests that the system display the browsing-data transfer sheet to export data to another browser.
### Managing export tokens
- [static var exportTokenUserInfoKey: String](bebrowserdataexportmanager/exporttokenuserinfokey-1y5l1.md)
  A key for accessing the data transfer token in the export launch activity’s info dictionary.
- [class let exportTokenUserInfoKey: String](bebrowserdataexportmanager/exporttokenuserinfokey-7e56u.md)
  A key for accessing the data transfer token in the export launch activity’s info dictionary.
- [static var userActivityType: String](bebrowserdataexportmanager/useractivitytype-4ar5j.md)
  A constant that identifies the launch activity for data export requests.
- [class let userActivityType: String](bebrowserdataexportmanager/useractivitytype-g862.md)
  A constant that identifies the launch activity for data export requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class BEExportOptions](beexportoptions.md)
  Options that identify data to export.
- [class BEExportMetadata](beexportmetadata.md)
  Metadata that describes available browser data for export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataexportmanager)*