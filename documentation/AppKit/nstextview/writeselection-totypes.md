# writeSelection(to:types:)

**Framework**: AppKit  
**Kind**: method

Writes the current selection to the specified pasteboard under each given type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func writeSelection(to pboard: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the data for any single type was successfully written, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

This method declares the data types on `pboard` and then invokes [`writeSelection(to:type:)`](nstextview/writeselection(to:type:).md) or the delegate method [`textView(_:write:at:to:type:)`](nstextviewdelegate/textview(_:write:at:to:type:).md) for each type in the `types` array.

You should not need to override this method. You might need to invoke this method if you are implementing a new type of pasteboard to handle services other than copy/paste or dragging.

## Parameters

- `pboard`: The pasteboard to write to.
- `types`: An array of strings describing the types of data to write.

## See Also

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
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nstextview/validrequestor(forsendtype:returntype:).md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/writeselection(to:types:))*