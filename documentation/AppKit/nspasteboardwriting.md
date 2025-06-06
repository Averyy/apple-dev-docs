# NSPasteboardWriting

**Framework**: AppKit  
**Kind**: protocol

A set of methods that defines the interface for retrieving a representation of an object that can be written to a pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPasteboardWriting : NSObjectProtocol
```

#### Overview

The Cocoa framework classes [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`NSColor`](nscolor.md), [`NSSound`](nssound.md), [`NSImage`](nsimage.md), and [`NSPasteboardItem`](nspasteboarditem.md) implement this protocol. You can make your custom class conform to this protocol so that you can write instances of the class to a pasteboard using the [`writeObjects(_:)`](nspasteboard/writeobjects(_:).md) method of [`NSPasteboard`](nspasteboard.md).

## Topics

### Required Methods
- [func writableTypes(for: NSPasteboard) -> [NSPasteboard.PasteboardType]](nspasteboardwriting/writabletypes(for:).md)
  Returns an array of UTI strings of data types the receiver can write to a given pasteboard.
- [func writingOptions(forType: NSPasteboard.PasteboardType, pasteboard: NSPasteboard) -> NSPasteboard.WritingOptions](nspasteboardwriting/writingoptions(fortype:pasteboard:).md)
  Returns options for writing data of a specified type to a given pasteboard.
- [NSPasteboard.WritingOptions](nspasteboard/writingoptions.md)
  Type to specify options for writing to a pasteboard.
### Property List for Type
- [func pasteboardPropertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboardwriting/pasteboardpropertylist(fortype:).md)
  Returns a property list object to represent the receiver on a pasteboard as an object of a specified type.
### Constants
- [Pasteboard Writing Options](pasteboard-writing-options.md)
  Constant to specify options for writing to a pasteboard, used by [`writingOptions(forType:pasteboard:)`](nspasteboardwriting/writingoptions(fortype:pasteboard:).md).
- [NSPasteboard.WritingOptions](nspasteboard/writingoptions.md)
  Type to specify options for writing to a pasteboard.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSColor](nscolor.md)
- [NSFilePromiseProvider](nsfilepromiseprovider.md)
- [NSImage](nsimage.md)
- [NSPasteboardItem](nspasteboarditem.md)
- [NSSound](nssound.md)
- [NSTextStorage](nstextstorage.md)

## See Also

- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [class NSPasteboardItem](nspasteboarditem.md)
  An item on a pasteboard.
- [protocol NSPasteboardReading](nspasteboardreading.md)
  A set of methods that defines the interface for initializing an object from a pasteboard.
- [protocol NSPasteboardItemDataProvider](nspasteboarditemdataprovider.md)
  A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
- [protocol NSPasteboardTypeOwner](nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardwriting)*