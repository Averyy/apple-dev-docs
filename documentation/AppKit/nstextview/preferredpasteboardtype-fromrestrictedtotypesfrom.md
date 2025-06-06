# preferredPasteboardType(from:restrictedToTypesFrom:)

**Framework**: AppKit  
**Kind**: method

Returns whatever type on the pasteboard would be most preferred for copying data.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func preferredPasteboardType(from availableTypes: [NSPasteboard.PasteboardType], restrictedToTypesFrom allowedTypes: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?
```

#### Return Value

The preferred type to provide given the available types and the allowed types.

#### Discussion

You should not need to override this method. You should also not need to invoke it unless you are implementing a new type of pasteboard to handle services other than copy/paste or dragging.

## Parameters

- `availableTypes`: The types currently available on the pasteboard.
- `allowedTypes`: Types allowed in the return value. If  , any available type is allowed.

## See Also

- [func pasteAsRichText(Any?)](nstextview/pasteasrichtext(_:).md)
  This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.
- [func pasteAsPlainText(Any?)](nstextview/pasteasplaintext(_:).md)
  Inserts the contents of the pasteboard into the receiver’s text as plain text.
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
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nstextview/validrequestor(forsendtype:returntype:).md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:))*