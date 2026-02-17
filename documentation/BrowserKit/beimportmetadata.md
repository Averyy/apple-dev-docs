# BEImportMetadata

**Framework**: BrowserKit  
**Kind**: class

Metadata that describes import capabilities for browser data transfers.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
class BEImportMetadata
```

## Mentions

- [Transferring browsing data to another browser](transferring-browsing-data-to-another-browser.md)

#### Overview

This class provides information about the import methods your browser supports. Configure an instance of this class to include in the sheet the option of importing data from files.

## Topics

### Creating import metadata
- [init?(coder: NSCoder)](beimportmetadata/init(coder:).md)
  Initializes import metadata from a decoder.
- [init(supportForImportFromFiles: Bool)](beimportmetadata/init(supportforimportfromfiles:).md)
  Initializes import metadata with file support information.
### Configuring import capabilities
- [var supportImportFromFiles: Bool](beimportmetadata/supportimportfromfiles.md)
  A Boolean value that indicates whether the import supports data from files.

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
- [class BEImportOptions](beimportoptions.md)
  Options for importing browsing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beimportmetadata)*