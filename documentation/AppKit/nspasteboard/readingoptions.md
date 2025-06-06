# NSPasteboard.ReadingOptions

**Framework**: AppKit  
**Kind**: struct

Options that specify how to interpret data on the pasteboard when initializing pasteboard data.

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ReadingOptions
```

#### Overview

You can specify only one option. If you don’t specify an option, the system uses the default [`asData`](nspasteboard/readingoptions/asdata.md).

## Topics

### Options
- [static var asData: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/asdata.md)
  An option to read data from the pasteboard as-is and return it as a data object.
- [static var asString: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/asstring.md)
  An option to read data from the pasteboard and convert it to a string object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.
- [static var asKeyedArchive: NSPasteboard.ReadingOptions](nspasteboard/readingoptions/askeyedarchive.md)
  An option to read data from the pasteboard and use it to initialize the object.
### Initializers
- [init(rawValue: UInt)](nspasteboard/readingoptions/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey.md)
  Options for reading pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](nspasteboard/pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func index(of: NSPasteboardItem) -> Int](nspasteboard/index(of:).md)
  Returns the index of the specified pasteboard item.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboard/data(fortype:).md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboard/propertylist(fortype:).md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboard/string(fortype:).md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions)*