# NSPasteboardTypeOwner

**Framework**: AppKit  
**Kind**: protocol

An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPasteboardTypeOwner : NSObjectProtocol
```

## Topics

### Fulfilling lazy data requests
- [func pasteboard(NSPasteboard, provideDataForType: NSPasteboard.PasteboardType)](nspasteboardtypeowner/pasteboard(_:providedatafortype:).md)
  Requests that the object provide data for the data type to the pasteboard.
### Changing pasteboard ownership
- [func pasteboardChangedOwner(NSPasteboard)](nspasteboardtypeowner/pasteboardchangedowner(_:).md)
  Notifies the object that the pasteboard’s owner changed.

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
- [protocol NSPasteboardItemDataProvider](nspasteboarditemdataprovider.md)
  A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardtypeowner)*