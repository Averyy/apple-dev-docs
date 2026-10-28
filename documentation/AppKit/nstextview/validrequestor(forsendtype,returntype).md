# validRequestor(forSendType:returnType:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns `self` if the text view can provide and accept the specified data types, or `nil` if it can’t.

**Availability**:
- macOS

## Declaration

```swift
func validRequestor(forSendType sendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?
```

```objc
- (id) validRequestorForSendType:(NSPasteboardType) sendType returnType:(NSPasteboardType) returnType;
```

## Return Value

`self` if `sendType` specifies a type of data the text view can put on the pasteboard and `returnType` contains a type of data the text view can read from the pasteboard; otherwise `nil`.

## Parameters

- `sendType`: The type of data requested.
- `returnType`: The type of data that will be returned.

## See Also

### Related Documentation
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](../nsresponder/validrequestor%28forsendtype,returntype%29.md)
  Overridden by subclasses to determine what services are available.
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
- [func writeSelection(to: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool](./writeselection%28to,types%29.md)
  Writes the current selection to the specified pasteboard under each given type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/validrequestor(forsendtype:returntype:))*