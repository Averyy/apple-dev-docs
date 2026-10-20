# readSelection(from:type:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reads data of the given type from the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
func readSelection(from pboard: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) readSelectionFromPasteboard:(NSPasteboard *) pboard type:(NSPasteboardType) type;
```

#### Return Value

[`true`](../../Swift/true.md) if the data was successfully read, [`false`](../../Swift/false.md) otherwise.

#### Discussion

The new data is placed at the current insertion point, replacing the current selection if one exists.

You should override this method to read pasteboard types other than the default types. Use the [`rangeForUserTextChange`](./rangeforusertextchange.md) method to obtain the range of characters (if any) to be replaced by the new data.

## Parameters

- `pboard`: The pasteboard to read from.
- `type`: The type of data to read.

## See Also

### Related Documentation
- [var rangeForUserTextChange: NSRange](./rangeforusertextchange.md)
  The range of characters affected by a method that changes characters (as opposed to attributes).
### Managing the pasteboard
- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](./preferredpasteboardtype%28from,restrictedtotypesfrom%29.md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
- [func readSelection(from: NSPasteboard) -> Bool](./readselection%28from%29.md)
  Reads the text view’s preferred type of data from the specified pasteboard.
- [var readablePasteboardTypes: [NSPasteboard.PasteboardType]](./readablepasteboardtypes.md)
  The types this text view can read immediately from the pasteboard.
- [var writablePasteboardTypes: [NSPasteboard.PasteboardType]](./writablepasteboardtypes.md)
  The pasteboard types that can be provided from the current selection.
- [func writeSelection(to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](./writeselection%28to,type%29.md)
  Writes the current selection to the specified pasteboard using the given type.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](./writeselection%28to,types%29.md)
  Writes the current selection to the specified pasteboard under each given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](./validrequestor%28forsendtype,returntype%29.md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/readselection(from:type:))*