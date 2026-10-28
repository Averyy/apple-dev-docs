# BEExportMetadata

**Framework**: BrowserKit  
**Kind**: class  
**Role**: Class

Metadata that describes available browser data for export.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
class BEExportMetadata
```

```objc
@interface BEExportMetadata : NSObject
```

## Mentions

- [Transferring browsing data to another browser](./transferring-browsing-data-to-another-browser.md)

## Overview

Create an instance of this class to represent the types and counts of data that originate from someone’s interaction with your browser and are available for export, such as bookmarks, page visit history, reading list items, and extensions. Pass the instance into [`requestExport(for:token:completionHandler:)`](./bebrowserdataexportmanager/requestexport%28for,token,completionhandler%29.md) to request that the system display the framework-provided transfer sheet.

For more information, see [Transferring browsing data to another browser](./transferring-browsing-data-to-another-browser.md).

## Topics

### Creating export metadata
- [init?(coder: NSCoder)](./beexportmetadata/init%28coder%29.md)
  Initializes export metadata from a decoder.
- [init(supportForExportToFiles: Bool, bookmarksCount: Int, readingListCount: Int, historyCount: Int, extensionsCount: Int)](./beexportmetadata/init%28supportforexporttofiles,bookmarkscount,readinglistcount,historycount,extensionscount%29.md)
  Initializes export metadata with file support information and data counts.
### Accessing data counts
- [var bookmarksCount: Int](./beexportmetadata/bookmarkscount.md)
  A count of bookmarks available for export.
- [var extensionsCount: Int](./beexportmetadata/extensionscount.md)
  A count of extensions available for export.
- [var historyCount: Int](./beexportmetadata/historycount.md)
  A count of history items available for export.
- [var readingListCount: Int](./beexportmetadata/readinglistcount.md)
  A count of reading list items available for export.
### Configuring export capabilities
- [var supportExportToFiles: Bool](./beexportmetadata/supportexporttofiles.md)
  A Boolean value that determines whether the sheet offers the option to export the data to files.

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

### Data export management
- [class BEBrowserDataExportManager](./bebrowserdataexportmanager.md)
  A class that handles exporting browsing data to other browsers.
- [class BEExportOptions](./beexportoptions.md)
  Options that identify data to export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserkit/beexportmetadata)*