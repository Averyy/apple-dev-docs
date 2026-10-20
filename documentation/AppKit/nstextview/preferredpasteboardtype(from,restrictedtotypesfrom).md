# preferredPasteboardType(from:restrictedToTypesFrom:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns whatever type on the pasteboard would be most preferred for copying data.

**Availability**:
- macOS

## Declaration

```swift
func preferredPasteboardType(from availableTypes: [NSPasteboard.PasteboardType], restrictedToTypesFrom allowedTypes: [NSPasteboard.PasteboardType]?) -> NSPasteboard.PasteboardType?
```

```objc
- (NSPasteboardType) preferredPasteboardTypeFromArray:(NSArray<NSString *> *) availableTypes restrictedToTypesFromArray:(NSArray<NSString *> *) allowedTypes;
```

#### Return Value

The preferred type to provide given the available types and the allowed types.

#### Discussion

You should not need to override this method. You should also not need to invoke it unless you are implementing a new type of pasteboard to handle services other than copy/paste or dragging.

## Parameters

- `availableTypes`: The types currently available on the pasteboard.
- `allowedTypes`: Types allowed in the return value. If `nil`, any available type is allowed.

## See Also

### Related Documentation
- [func pasteAsRichText(Any?)](./pasteasrichtext%28_%29.md)
  This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.
- [func pasteAsPlainText(Any?)](./pasteasplaintext%28_%29.md)
  Inserts the contents of the pasteboard into the receiver’s text as plain text.
### Managing the pasteboard
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
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](./writeselection%28to,types%29.md)
  Writes the current selection to the specified pasteboard under each given type.
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](./validrequestor%28forsendtype,returntype%29.md)
  Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/preferredpasteboardtype(from:restrictedtotypesfrom:))*