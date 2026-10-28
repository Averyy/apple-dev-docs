# NSPasteboard.ReadingOptionKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Options for reading pasteboard data.

**Availability**:
- macOS

## Declaration

```swift
struct ReadingOptionKey
```

```c
typedef NSString * NSPasteboardReadingOptionKey;
```

## Discussion

These options can be used for both the [`readObjects(forClasses:options:)`](./readobjects%28forclasses,options%29.md) and [`canReadObject(forClasses:options:)`](./canreadobject%28forclasses,options%29.md) methods, unless otherwise specified.  The currently available options allow for customization of how URLS are read from the pasteboard.

## Topics

### Type Properties
- [static let urlReadingContentsConformToTypes: NSPasteboard.ReadingOptionKey](./readingoptionkey/urlreadingcontentsconformtotypes.md)
  Option for reading URLs to restrict the results to URLs with contents that conform to any of the provided UTI types.
- [static let urlReadingFileURLsOnly: NSPasteboard.ReadingOptionKey](./readingoptionkey/urlreadingfileurlsonly.md)
  Option for reading URLs to restrict the results to file URLs only.
### Initializers
- [init(rawValue: String)](./readingoptionkey/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reading data
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptions](./readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptionkey)*