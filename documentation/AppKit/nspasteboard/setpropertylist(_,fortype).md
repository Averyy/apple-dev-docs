# setPropertyList(_:forType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the given property list as the representation for the specified type for the first item on the receiver.

**Availability**:
- macOS

## Declaration

```swift
func setPropertyList(_ plist: Any, forType dataType: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) setPropertyList:(id) plist forType:(NSPasteboardType) dataType;
```

## Return Value

[`true`](../../Swift/true.md) if the data was written successfully, otherwise [`false`](../../Swift/false.md) if ownership of the pasteboard has changed. Any other error raises an `NSPasteboardCommunicationException`.

## Discussion

This method invokes [`setData(_:forType:)`](./setdata%28_,fortype%29.md) with a serialized property list parameter.

## Parameters

- `plist`: The property list data to write to the pasteboard.
- `dataType`: The type of property-list data in the `propertyList` parameter. The type must have been declared by a previous [`declareTypes(_:owner:)`](./declaretypes%28_,owner%29.md) message.

## See Also

### Related Documentation
- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](./propertylist%28fortype%29.md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
### Writing data
- [func clearContents() -> Int](./clearcontents%28%29.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](./writeobjects%28_%29.md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](./setdata%28_,fortype%29.md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](./setstring%28_,fortype%29.md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](./pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/setpropertylist(_:fortype:))*