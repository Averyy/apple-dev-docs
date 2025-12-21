# writeObjects(_:)

**Framework**: AppKit  
**Kind**: method

Writes an array of objects to the receiver.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func writeObjects(_ objects: [any NSPasteboardWriting]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the array was successfully added, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `objects`: An array of objects that implement the   protocol (including instances of  ).

## See Also

- [func clearContents() -> Int](nspasteboard/clearcontents.md)
  Clears the existing contents of the pasteboard.
- [func setData(Data?, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setdata(_:fortype:).md)
  Sets the data as the representation for the specified type for the first item on the receiver.
- [func setPropertyList(Any, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setpropertylist(_:fortype:).md)
  Sets the given property list as the representation for the specified type for the first item on the receiver.
- [func setString(String, forType: NSPasteboard.PasteboardType) -> Bool](nspasteboard/setstring(_:fortype:).md)
  Sets the given string as the representation for the specified type for the first item on the receiver.
- [NSPasteboard.PasteboardType](nspasteboard/pasteboardtype.md)
  The supported pasteboard types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspasteboard/writeobjects(_:))*