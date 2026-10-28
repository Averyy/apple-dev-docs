# writeSelection(to:type:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the current selection to the specified pasteboard using the given type.

**Availability**:
- macOS

## Declaration

```swift
func writeSelection(to pboard: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool
```

```objc
- (BOOL) writeSelectionToPasteboard:(NSPasteboard *) pboard type:(NSPasteboardType) type;
```

## Return Value

[`true`](../../Swift/true.md) if the data was successfully written, [`false`](../../Swift/false.md) otherwise.

## Discussion

The complete set of data types being written to `pboard` should be declared before invoking this method.

This method should be invoked only from [`writeSelection(to:types:)`](./writeselection%28to,types%29.md). You can override this method to add support for writing new types of data to the pasteboard. You should invoke `super`’s implementation of the method to handle any types of data your overridden version does not.

## Parameters

- `pboard`: The pasteboard to write to.
- `type`: The type of data to write.

## See Also

### Managing the pasteboard
- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](./preferredpasteboardtype%28from,restrictedtotypesfrom%29.md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
- [func readSelection(from: NSPasteboard) -> Bool](./readselection%28from%29.md)
  Reads the text view’s preferred type of data from the specified pasteboard.
- [func readSelection(from: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](./readselection%28from,type%29.md)
  Reads data of the given type from the specified pasteboard.
- [var readablePasteboardTypes: [NSPasteboard.PasteboardType]](./readablepasteboardtypes.md)
  The types this text view can read immediately from the pasteboard.
- [var writablePasteboardTypes: [NSPasteboard.PasteboardType]](./writablepasteboardtypes.md)
  The pasteboard types that can be provided from the current selection.
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](./writeselection%28to,types%29.md)
  Writes the current selection to the specified pasteboard under each given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](./validrequestor%28forsendtype,returntype%29.md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/writeselection(to:type:))*