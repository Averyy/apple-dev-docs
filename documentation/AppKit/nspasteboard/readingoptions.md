# NSPasteboard.ReadingOptions

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Options that specify how to interpret data on the pasteboard when initializing pasteboard data.

**Availability**:
- macOS 10.6+

## Declaration

```swift
struct ReadingOptions
```

```c
enum NSPasteboardReadingOptions : NSUInteger;
```

#### Overview

You can specify only one option. If you don’t specify an option, the system uses the default [`asData`](./readingoptions/asdata.md).

## Topics

### Options
- [static var asData: NSPasteboard.ReadingOptions](./readingoptions/asdata.md)
  An option to read data from the pasteboard as-is and return it as a data object.
- [static var asString: NSPasteboard.ReadingOptions](./readingoptions/asstring.md)
  An option to read data from the pasteboard and convert it to a string object.
- [static var asPropertyList: NSPasteboard.ReadingOptions](./readingoptions/aspropertylist.md)
  An option to read data from the pasteboard and unserialize it as a property list.
- [static var asKeyedArchive: NSPasteboard.ReadingOptions](./readingoptions/askeyedarchive.md)
  An option to read data from the pasteboard and use it to initialize the object.
### Initializers
- [init(rawValue: UInt)](./readingoptions/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Reading data
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](./readingoptionkey.md)
  Options for reading pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](./pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func index(of: NSPasteboardItem) -> Int](./index%28of%29.md)
  Returns the index of the specified pasteboard item.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./propertylist%28fortype%29.md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./string%28fortype%29.md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptions)*