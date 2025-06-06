# validRequestor(forSendType:returnType:)

**Framework**: AppKit  
**Kind**: method

Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?
```

#### Return Value

`self` if `sendType` specifies a type of data the text view can put on the pasteboard and `returnType` contains a type of data the text view can read from the pasteboard; otherwise `nil`.

## Parameters

- `sendType`: The type of data requested.
- `returnType`: The type of data that will be returned.

## See Also

- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsresponder/validrequestor(forsendtype:returntype:).md)
  Overridden by subclasses to determine what services are available.
- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:).md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
- [func readSelection(from: NSPasteboard) -> Bool](nstextview/readselection(from:).md)
  Reads the text view’s preferred type of data from the specified pasteboard.
- [func readSelection(from: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextview/readselection(from:type:).md)
  Reads data of the given type from the specified pasteboard.
- [var readablePasteboardTypes: [NSPasteboard.PasteboardType]](nstextview/readablepasteboardtypes.md)
  The types this text view can read immediately from the pasteboard.
- [var writablePasteboardTypes: [NSPasteboard.PasteboardType]](nstextview/writablepasteboardtypes.md)
  The pasteboard types that can be provided from the current selection.
- [func writeSelection(to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextview/writeselection(to:type:).md)
  Writes the current selection to the specified pasteboard using the given type.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nstextview/writeselection(to:types:).md)
  Writes the current selection to the specified pasteboard under each given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/validrequestor(forsendtype:returntype:))*