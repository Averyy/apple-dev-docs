# NSPasteboard.ContentsOptions

**Framework**: AppKit  
**Kind**: struct

Options for preparing the pasteboard.

**Availability**:
- macOS 10.12+

## Declaration

```swift
struct ContentsOptions
```

## Topics

### Options
- [static var currentHostOnly: NSPasteboard.ContentsOptions](nspasteboard/contentsoptions/currenthostonly.md)
  The pasteboard contents are available only on the current device, and not on any other devices.
### Initializers
- [init(rawValue: UInt)](nspasteboard/contentsoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

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
- [protocol NSPasteboardTypeOwner](nspasteboardtypeowner.md)
  An object that serves as a data provider for data types that use lazy data fulfillment from a pasteboard request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/contentsoptions)*