# setPropertyList(_:forType:)

**Framework**: AppKit  
**Kind**: method

Sets the given property list as the representation for the specified type for the first item on the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func setPropertyList(_ plist: Any, forType dataType: NSPasteboard.PasteboardType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data was written successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false) if ownership of the pasteboard has changed. Any other error raises an `NSPasteboardCommunicationException`.

#### Discussion

This method invokes [`setData(_:forType:)`](nspasteboard/setdata(_:fortype:).md) with a serialized property list parameter.

## Parameters

- `plist`: The property list data to write to the pasteboard.
- `dataType`: The type of property-list data in the   parameter. The type must have been declared by a previous   message.

## See Also

- [func propertyList(forType: NSPasteboard.PasteboardType) -> Any?](nspasteboard/propertylist(fortype:).md)
  Returns the property list for the specified type from the first item in the receiver that contains the type.
- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](nspasteboard/writeobjects(_:).md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setstring(_:fortype:).md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](nspasteboard/pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/setpropertylist(_:fortype:))*