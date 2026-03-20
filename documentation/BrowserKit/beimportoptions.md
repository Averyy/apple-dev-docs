# BEImportOptions

**Framework**: BrowserKit  
**Kind**: class

Options for importing browsing data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEImportOptions
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Overview

The [`requestImport(for:completionHandler:)`](bebrowserdataimportmanager/requestimport(for:completionhandler:).md) returns an instance of this class, which indicates whether the import needs to source from files rather than direct browser-to-browser transfer.

## Topics

### Creating import options
- [init?(coder: NSCoder)](beimportoptions/init(coder:).md)
  Initializes imports from a decoder.
- [init(importFromFiles: Bool)](beimportoptions/init(importfromfiles:).md)
  Initializes imports with a file import preference.
### Configuring import preferences
- [var importFromFiles: Bool](beimportoptions/importfromfiles.md)
  A Boolean value that indicates whether to import browser data from files.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class BEBrowserDataImportManager](bebrowserdataimportmanager.md)
  A class that handles importing browsing data from other browsers.
- [class BEImportMetadata](beimportmetadata.md)
  Metadata that describes import capabilities for browser data transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beimportoptions)*