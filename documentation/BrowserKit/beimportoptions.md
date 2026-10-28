# BEImportOptions

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

Options for importing browsing data.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEImportOptions
```

```objc
@interface BEImportOptions : NSObject
```

## Mentions

- [Transferring browsing data to another browser](./transferring-browsing-data-to-another-browser.md)

## Overview

The [`requestImport(for:completionHandler:)`](./bebrowserdataimportmanager/requestimport%28for,completionhandler%29.md) returns an instance of this class, which indicates whether the import needs to source from files rather than direct browser-to-browser transfer.

## Topics

### Creating import options
- [init?(coder: NSCoder)](./beimportoptions/init%28coder%29.md)
  Initializes imports from a decoder.
- [init(importFromFiles: Bool)](./beimportoptions/init%28importfromfiles%29.md)
  Initializes imports with a file import preference.
### Configuring import preferences
- [var importFromFiles: Bool](./beimportoptions/importfromfiles.md)
  A Boolean value that indicates whether to import browser data from files.

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
- [class BEImportMetadata](./beimportmetadata.md)
  Metadata that describes import capabilities for browser data transfers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beimportoptions)*