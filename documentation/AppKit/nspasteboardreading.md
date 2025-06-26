# NSPasteboardReading

**Framework**: AppKit  
**Kind**: protocol

A set of methods that defines the interface for initializing an object from a pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPasteboardReading : NSObjectProtocol
```

#### Overview

The Cocoa framework classes [`NSString`](https://developer.apple.com/documentation/Foundation/NSString), [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString), [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL), [`NSColor`](nscolor.md), [`NSSound`](nssound.md), [`NSImage`](nsimage.md), and [`NSPasteboardItem`](nspasteboarditem.md) implement this protocol. You can make your custom class conform to this protocol so that you can read instances from a pasteboard using the [`readObjects(forClasses:options:)`](nspasteboard/readobjects(forclasses:options:).md) method of [`NSPasteboard`](nspasteboard.md).

## Topics

### Initializing the Pasteboard
- [init?(pasteboardPropertyList: Any, ofType: NSPasteboard.PasteboardType)](nspasteboardreading/init(pasteboardpropertylist:oftype:).md)
  Initializes an instance with a property list object and a type string.
### Reading From the Pasteboard
- [static func readableTypes(for: NSPasteboard) -> [NSPasteboard.PasteboardType]](nspasteboardreading/readabletypes(for:).md)
  Returns an array of uniform type identifier strings of data types the receiver can read from the pasteboard and initialize from.
- [static func readingOptions(forType: NSPasteboard.PasteboardType, pasteboard: NSPasteboard) -> NSPasteboard.ReadingOptions](nspasteboardreading/readingoptions(fortype:pasteboard:).md)
  Returns options for reading data of a specified type from a given pasteboard.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [NSColor](nscolor.md)
- [NSFilePromiseReceiver](nsfilepromisereceiver.md)
- [NSImage](nsimage.md)
- [NSPasteboardItem](nspasteboarditem.md)
- [NSSound](nssound.md)
- [NSTextStorage](nstextstorage.md)

## See Also

- [class NSPasteboard](nspasteboard.md)
  An object that transfers data to and from the pasteboard server.
- [class NSPasteboardItem](nspasteboarditem.md)
  An item on a pasteboard.
- [protocol NSPasteboardWriting](nspasteboardwriting.md)
  A set of methods that defines the interface for retrieving a representation of an object that can be written to a pasteboard.
- [protocol NSPasteboardItemDataProvider](nspasteboarditemdataprovider.md)
  A set of methods implemented by the data provider of a pasteboard item to provide the data for a particular UTI type.
- [NSPasteboard.ContentsOptions](nspasteboard/contentsoptions.md)
  Options for preparing the pasteboard.
- [protocol NSPasteboardTypeOwner](nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboardreading)*