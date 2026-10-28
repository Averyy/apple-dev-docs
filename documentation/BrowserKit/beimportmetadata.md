# BEImportMetadata

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

Metadata that describes import capabilities for browser data transfers.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEImportMetadata
```

```objc
@interface BEImportMetadata : NSObject
```

## Mentions

- [Transferring browsing data to another browser](./transferring-browsing-data-to-another-browser.md)

## Overview

This class provides information about the import methods your browser supports. Configure an instance of this class to include in the sheet the option of importing data from files.

## Topics

### Creating import metadata
- [init?(coder: NSCoder)](./beimportmetadata/init%28coder%29.md)
  Initializes import metadata from a decoder.
- [init(supportForImportFromFiles: Bool)](./beimportmetadata/init%28supportforimportfromfiles%29.md)
  Initializes import metadata with file support information.
### Configuring import capabilities
- [var supportImportFromFiles: Bool](./beimportmetadata/supportimportfromfiles.md)
  A Boolean value that indicates whether the import supports data from files.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data import management
- [class BEBrowserDataImportManager](./bebrowserdataimportmanager.md)
  A class that handles importing browsing data from other browsers.
- [class BEImportOptions](./beimportoptions.md)
  Options for importing browsing data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beimportmetadata)*