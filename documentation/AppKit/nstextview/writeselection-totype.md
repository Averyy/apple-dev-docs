# writeSelection(to:type:)

**Framework**: AppKit  
**Kind**: method

Writes the current selection to the specified pasteboard using the given type.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func writeSelection(to pboard: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the data was successfully written, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

The complete set of data types being written to `pboard` should be declared before invoking this method.

This method should be invoked only from [`writeSelection(to:types:)`](nstextview/writeselection(to:types:).md). You can override this method to add support for writing new types of data to the pasteboard. You should invoke `super`’s implementation of the method to handle any types of data your overridden version does not.

## Parameters

- `pboard`: The pasteboard to write to.
- `type`: The type of data to write.

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
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](nstextview/writeselection(to:types:).md)
  Writes the current selection to the specified pasteboard under each given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nstextview/validrequestor(forsendtype:returntype:).md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/writeselection(to:type:))*