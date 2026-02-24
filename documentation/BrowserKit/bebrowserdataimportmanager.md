# BEBrowserDataImportManager

**Framework**: BrowserKit  
**Kind**: class

A class that handles importing browsing data from other browsers.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
class BEBrowserDataImportManager
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Overview

This class coordinates the transfer of browsing data by presenting the framework-provided import sheet when a person wants to import data through your app’s UI (see [`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md)). Call this class’s [`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md) to stream browsing data from the system, as received through another browser. For more information, see [`Transferring browsing data to another browser`](transferring-browsing-data-to-another-browser.md).

## Topics

### Creating an import manager
- [init()](bebrowserdataimportmanager/init.md)
  Initializes an import manager.
### Importing browser data
- [func importBrowserData(token: UUID) -> AsyncThrowingStream<BEBrowserData, any Error>](bebrowserdataimportmanager/importbrowserdata(token:).md)
  Imports another app’s browsing data as a stream.
- [func requestImport(for: BEImportMetadata, completionHandler: (BEImportOptions?, (any Error)?) -> Void)](bebrowserdataimportmanager/requestimport(for:completionhandler:).md)
  Requests that the system display the sheet to import data from another browser.
### Managing import tokens
- [class let importTokenUserInfoKey: String](bebrowserdataimportmanager/importtokenuserinfokey-3bqve.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [static var importTokenUserInfoKey: String](bebrowserdataimportmanager/importtokenuserinfokey-3zzub.md)
  A key for accessing the data transfer token in the import launch activity’s info dictionary.
- [static var userActivityType: String](bebrowserdataimportmanager/useractivitytype-35jes.md)
  A constant that identifies the launch activity for data import requests.
- [class let userActivityType: String](bebrowserdataimportmanager/useractivitytype-8xgjo.md)
  A constant that identifies the launch activity for data import requests.
### Initializers
- [init(scene: UIWindowScene?)](bebrowserdataimportmanager/init(scene:).md)
  Initializes an import manager for a window scene.

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

- [class BEImportMetadata](beimportmetadata.md)
  Metadata that describes import capabilities for browser data transfers.
- [class BEImportOptions](beimportoptions.md)
  Options for importing browsing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/bebrowserdataimportmanager)*