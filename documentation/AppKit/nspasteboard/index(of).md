# index(of:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index of the specified pasteboard item.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func index(of pasteboardItem: NSPasteboardItem) -> Int
```

```objc
- (NSUInteger) indexOfPasteboardItem:(NSPasteboardItem *) pasteboardItem;
```

## Return Value

The index of the specified pasteboard item. If `pasteboardItem` has not been added to any pasteboard, or is owned by another pasteboard, returns `NSNotFound`.

## Discussion

An item’s index in the pasteboard is useful for a pasteboard item data provider that has promised data for multiple items, to be able to easily match the pasteboard item to an array of source data from which to derive the promised data.

## Parameters

- `pasteboardItem`: A pasteboard item.

## See Also

### Reading data
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](./readingoptionkey.md)
  Options for reading pasteboard data.
- [NSPasteboard.ReadingOptions](./readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](./pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](./data%28fortype%29.md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./propertylist%28fortype%29.md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](./string%28fortype%29.md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/index(of:))*