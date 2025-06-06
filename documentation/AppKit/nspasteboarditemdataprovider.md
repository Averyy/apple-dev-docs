# NSPasteboardItemDataProvider

**Framework**: AppKit  
**Kind**: protocol

A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPasteboardItemDataProvider : NSObjectProtocol
```

#### Overview

You can specify an object as a pasteboard data provider for a pasteboard item using [`NSPasteboardItem`](nspasteboarditem.md)’s [`setDataProvider(_:forTypes:)`](nspasteboarditem/setdataprovider(_:fortypes:).md) method. The data provider must implement this protocol to provide data upon request.

## Topics

### Providing Data
- [func pasteboard(NSPasteboard?, item: NSPasteboardItem, provideDataForType: NSPasteboard.PasteboardType)](nspasteboarditemdataprovider/pasteboard(_:item:providedatafortype:).md)
  Asks the receiver to provide data for a specified type to a given pasteboard.
- [func pasteboardFinishedWithDataProvider(NSPasteboard)](nspasteboarditemdataprovider/pasteboardfinishedwithdataprovider(_:).md)
  Informs the receiver that the pasteboard no longer needs the data provider for any of its pasteboard items.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [class NSPasteboardItem](nspasteboarditem.md)
  An item on a pasteboard.
- [protocol NSPasteboardReading](nspasteboardreading.md)
  A set of methods that defines the interface for initializing an object from a pasteboard.
- [protocol NSPasteboardWriting](nspasteboardwriting.md)
  A set of methods that defines the interface for retrieving a representation of an object that can be written to a pasteboard.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
- [protocol NSPasteboardTypeOwner](nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboarditemdataprovider)*