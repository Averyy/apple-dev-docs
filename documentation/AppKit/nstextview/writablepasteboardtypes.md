# writablePasteboardTypes

**Framework**: AppKit  
**Kind**: property

The pasteboard types that can be provided from the current selection.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var writablePasteboardTypes: [NSPasteboard.PasteboardType] { get }
```

#### Discussion

An array of strings describing the types that can be written to the pasteboard immediately, or an array with no members if the text view has no text or no selection.

Overriders can copy the result from super and add their own new types.

## See Also

- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:).md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
- [func readSelection(from: NSPasteboard) -> Bool](nstextview/readselection(from:).md)
  Reads the text view’s preferred type of data from the specified pasteboard.
- [func readSelection(from: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextview/readselection(from:type:).md)
  Reads data of the given type from the specified pasteboard.
- [var readablePasteboardTypes: [NSPasteboard.PasteboardType]](nstextview/readablepasteboardtypes.md)
  The types this text view can read immediately from the pasteboard.
- [func writeSelection(to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](nstextview/writeselection(to:type:).md)
  Writes the current selection to the specified pasteboard using the given type.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nstextview/writeselection(to:types:).md)
  Writes the current selection to the specified pasteboard under each given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nstextview/validrequestor(forsendtype:returntype:).md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/writablepasteboardtypes)*