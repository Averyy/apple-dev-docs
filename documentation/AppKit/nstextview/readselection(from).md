# readSelection(from:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Reads the text view’s preferred type of data from the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
func readSelection(from pboard: NSPasteboard) -> Bool
```

```objc
- (BOOL) readSelectionFromPasteboard:(NSPasteboard *) pboard;
```

## Return Value

[`true`](../../Swift/true.md) if the data was successfully read, [`false`](../../Swift/false.md) otherwise.

## Discussion

This method invokes the [`preferredPasteboardType(from:restrictedToTypesFrom:)`](./preferredpasteboardtype%28from,restrictedtotypesfrom%29.md) method to determine the text view’s preferred type of data and then reads the data using the [`readSelection(from:type:)`](./readselection%28from,type%29.md) method.

You should not need to override this method. You might need to invoke this method if you are implementing a new type of pasteboard to handle services other than copy/paste or dragging.

## Parameters

- `pboard`: The pasteboard to read from.

## See Also

### Managing the pasteboard
- [func preferredPasteboardType(from: [NSPasteboard.PasteboardType], restrictedToTypesFrom: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?](./preferredpasteboardtype%28from,restrictedtotypesfrom%29.md)
  Returns whatever type on the pasteboard would be most preferred for copying data.
- [func readSelection(from: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](./readselection%28from,type%29.md)
  Reads data of the given type from the specified pasteboard.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/readselection(from:))*