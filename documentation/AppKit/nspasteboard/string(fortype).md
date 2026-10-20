# string(forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.

**Availability**:
- macOS

## Declaration

```swift
func string(forType dataType: NSPasteboard.PasteboardType) -> String?
```

```objc
- (NSString *) stringForType:(NSPasteboardType) dataType;
```

#### Return Value

A concatenation of the strings for the specified type from all the items in the receiver that contain the type, or `nil` if none of the items contain strings of the specified type.

#### Discussion

This method invokes [`data(forType:)`](./data%28fortype%29.md) to obtain the string. If the string cannot be obtained, [`string(forType:)`](./string%28fortype%29.md) returns `nil`. See [`data(forType:)`](./data%28fortype%29.md) for a description of what will cause `nil` to be returned.

In macOS 10.6 and later, if the receiver contains multiple items that can provide string, RTF, or RTFD data, the text data from each item is returned as a combined result separated by newlines.

##### Special Considerations

It’s a good idea to check [`types`](./types.md) or call [`availableType(from:)`](./availabletype%28from%29.md) before invoking [`string(forType:)`](./string%28fortype%29.md). Although performing this check isn’t required, doing so can help you determine if a `nil` result from a reading method is due to something like a pasteboard timeout.

## Parameters

- `dataType`: The pasteboard data type to read.

## See Also

### Related Documentation
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
### Reading data
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](./readobjects%28forclasses,options%29.md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](./readingoptionkey.md)
  Options for reading pasteboard data.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/string(fortype:))*