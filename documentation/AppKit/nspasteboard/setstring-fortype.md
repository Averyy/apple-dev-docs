# setString(_:forType:)

**Framework**: AppKit  
**Kind**: method

Sets the given string as the representation for the specified type for the first item on the receiver.

**Availability**:
- macOS ?+

## Declaration

```swift
func setString(_ string: String, forType dataType: NSPasteboard.PasteboardType) -> Bool
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data was written successfully, otherwise [`false`](https://developer.apple.com/documentation/swift/false) if ownership of the pasteboard has changed. Any other error raises an `NSPasteboardCommunicationException`.

#### Discussion

This method invokes [`setData(_:forType:)`](nspasteboard/setdata(_:fortype:).md) to perform the write.

## Parameters

- `string`: The string to write to the pasteboard.
- `dataType`: The type of string data. The type must have been declared by a previous   message.

## See Also

- [func string(forType: NSPasteboard.PasteboardType) -> String?](nspasteboard/string(fortype:).md)
  Returns a concatenation of the strings for the specified type from all the items in the receiver that contain the type.
- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [func writeObjects([any NSPasteboardWriting]) -> Bool](nspasteboard/writeobjects(_:).md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setpropertylist(_:fortype:).md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](nspasteboard/pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/setstring(_:fortype:))*