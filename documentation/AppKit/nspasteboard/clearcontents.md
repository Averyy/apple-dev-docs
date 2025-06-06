# clearContents()

**Framework**: AppKit  
**Kind**: method

Clears the existing contents of the pasteboard.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func clearContents() -> Int
```

#### Return Value

The change count of the receiver.

#### Discussion

Clears the existing contents of the pasteboard, preparing it for new contents. This is the first step in providing data on the pasteboard.

## See Also

- [func writeObjects([any NSPasteboardWriting]) -> Bool](nspasteboard/writeobjects(_:).md)
  Writes an array of objects to the receiver.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setpropertylist(_:fortype:).md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setstring(_:fortype:).md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](nspasteboard/pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/clearcontents())*