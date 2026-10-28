# writeSelection(to:types:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the current selection to the specified pasteboard under each given type.

**Availability**:
- macOS

## Declaration

```swift
func writeSelection(to pboard: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool
```

```objc
- (BOOL) writeSelectionToPasteboard:(NSPasteboard *) pboard types:(NSArray<NSString *> *) types;
```

## Return Value

[`true`](../../Swift/true.md) if the data for any single type was successfully written, [`false`](../../Swift/false.md) otherwise.

## Discussion

This method declares the data types on `pboard` and then invokes [`writeSelection(to:type:)`](./writeselection%28to,type%29.md) or the delegate method [`textView(_:write:at:to:type:)`](../nstextviewdelegate/textview%28_,write,at,to,type%29.md) for each type in the `types` array.

You should not need to override this method. You might need to invoke this method if you are implementing a new type of pasteboard to handle services other than copy/paste or dragging.

## Parameters

- `pboard`: The pasteboard to write to.
- `types`: An array of strings describing the types of data to write.

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
- [func writeSelection(to: NSPasteboard, type: NSPasteboard.PasteboardType) -> Bool](./writeselection%28to,type%29.md)
  Writes the current selection to the specified pasteboard using the given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](./validrequestor%28forsendtype,returntype%29.md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/writeselection(to:types:))*