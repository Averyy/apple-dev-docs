# BEImportMetadata

**Framework**: BrowserKit  
**Kind**: class

Metadata that describes import capabilities for browser data transfers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class BEBrowserDataImportManager](bebrowserdataimportmanager.md)
  A class that handles importing browsing data from other browsers.
- [class BEImportOptions](beimportoptions.md)
  Options for importing browsing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beimportmetadata)*