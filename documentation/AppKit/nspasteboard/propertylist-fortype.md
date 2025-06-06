# propertyList(forType:)

**Framework**: AppKit  
**Kind**: method

Returns the property list for the specified type from the first item in the receiver that contains the type.

**Availability**:
- macOS ?+

## Declaration

```swift
func propertyList(forType dataType: NSPasteboard.PasteboardType) -> Any?
```

#### Return Value

A property list of objects of the specified type, obtained from the first item in the receiver that contains the type. The returned property list can contain any combination of objects, as long as each object is a valid property-list type (for a list of types, see [`Property list`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/PropertyList.html#//apple_ref/doc/uid/TP40008195-CH44)).

#### Discussion

This method invokes the [`data(forType:)`](nspasteboard/data(fortype:).md) method.

##### Special Considerations

It’s a good idea to check [`types`](nspasteboard/types.md) or call [`availableType(from:)`](nspasteboard/availabletype(from:).md) before invoking [`propertyList(forType:)`](nspasteboard/propertylist(fortype:).md). Although performing this check isn’t required, doing so can help you determine if a `nil` result from a reading method is due to something like a pasteboard timeout.

## Parameters

- `dataType`: The pasteboard data type containing the property-list data.

## See Also

- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setpropertylist(_:fortype:).md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func readObjects(forClasses: [AnyClass], options: [NSPasteboard.ReadingOptionKey : Any]?) -> [Any]?](nspasteboard/readobjects(forclasses:options:).md)
  Reads from the receiver objects that best match the specified array of classes.
- [NSPasteboard.ReadingOptionKey](nspasteboard/readingoptionkey.md)
  Options for reading pasteboard data.
- [NSPasteboard.ReadingOptions](nspasteboard/readingoptions.md)
  Options that specify how to interpret data on the pasteboard when initializing pasteboard data.
- [var pasteboardItems: [NSPasteboardItem]?](nspasteboard/pasteboarditems.md)
  An array that contains all the items held by the pasteboard.
- [func index(of: NSPasteboardItem) -> Int](nspasteboard/index(of:).md)
  Returns the index of the specified pasteboard item.
- [func data(forType: NSPasteboard.PasteboardType) -> Data?](nspasteboard/data(fortype:).md)
  Returns the data for the specified type from the first item in the receiver that contains the type.
- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboard/string(fortype:).md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/propertylist(fortype:))*