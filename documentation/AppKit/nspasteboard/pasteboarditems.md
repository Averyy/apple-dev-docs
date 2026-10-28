# pasteboardItems

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array that contains all the items held by the pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var pasteboardItems: [NSPasteboardItem]? { get }
```

```objc
@property (copy, readonly, nullable) NSArray<NSPasteboardItem *> * pasteboardItems;
```

## Discussion

If an error occurs when retrieving the pasteboard items, the value of this property is `nil`.

## See Also

### Reading data
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](./readingoptionkey.md)
  Options for reading pasteboard data.
- [NSPasteboard.ReadingOptions](./readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
- [func index(of: NSPasteboardItem) -> Int](./index%28of%29.md)
  Returns the index of the specified pasteboard item.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./propertylist%28fortype%29.md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./string%28fortype%29.md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/pasteboarditems)*