# readSelection(from:)

**Framework**: AppKit  
**Kind**: method

Reads the text view’s preferred type of data from the specified pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func readSelection(from pboard: NSPasteboard) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the data was successfully read, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

This method invokes the [`preferredPasteboardType(from:restrictedToTypesFrom:)`](nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:).md) method to determine the text view’s preferred type of data and then reads the data using the [`readSelection(from:type:)`](nstextview/readselection(from:type:).md) method.

You should not need to override this method. You might need to invoke this method if you are implementing a new type of pasteboard to handle services other than copy/paste or dragging.

## Parameters

- `pboard`: The pasteboard to read from.

## See Also

- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:).md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/readselection(from:))*