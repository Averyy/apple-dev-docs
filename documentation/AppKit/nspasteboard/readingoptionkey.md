# NSPasteboard.ReadingOptionKey

**Framework**: AppKit  
**Kind**: struct

Options for reading pasteboard data.

**Availability**:
- macOS ?+

## Declaration

```swift
struct ReadingOptionKey
```

#### Discussion

These options can be used for both the [`readObjects(forClasses:options:)`](nspasteboard/readobjects(forclasses:options:).md) and [`canReadObject(forClasses:options:)`](nspasteboard/canreadobject(forclasses:options:).md) methods, unless otherwise specified.  The currently available options allow for customization of how URLS are read from the pasteboard.

## Topics

### Type Properties
- [static let urlReadingContentsConformToTypes: NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey/urlreadingcontentsconformtotypes.md)
  Option for reading URLs to restrict the results to URLs with contents that conform to any of the provided UTI types.
- [static let urlReadingFileURLsOnly: NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey/urlreadingfileurlsonly.md)
  Option for reading URLs to restrict the results to file URLs only.
### Initializers
- [init(rawValue: String)](nspasteboard/readingoptionkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/readingoptionkey)*