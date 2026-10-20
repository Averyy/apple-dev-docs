# writeSelection(to:types:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the current selection to the pasteboard.

**Availability**:
- macOS

## Declaration

```swift
optional func writeSelection(to pboard: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool
```

```objc
- (BOOL) writeSelectionToPasteboard:(NSPasteboard *) pboard types:(NSArray<NSString *> *) types;
```

## Mentions

- [Supporting Writing Tools via the pasteboard](../supporting-writing-tools-via-the-pasteboard.md)

#### Return Value

[`true`](../../Swift/true.md) if your implementation was able to write one or more types to the pasteboard; otherwise, [`false`](../../Swift/false.md).

#### Discussion

A [`writeSelection(to:types:)`](./writeselection%28to,types%29.md) message is sent to the first responder when the user chooses a command from the Services menu, but only if the receiver didn’t return `nil` to a previous [`validRequestor(forSendType:returnType:)`](../nsresponder/validrequestor%28forsendtype,returntype%29.md) message.

After your method writes the data to the pasteboard, a remote message is sent to the application that provides the service the user requested. If the service provider supplies return data to replace the selection, the first responder will then receive a [`readSelection(from:)`](./readselection%28from%29.md) message.

## Parameters

- `pboard`: The pasteboard to receive your data.
- `types`: An array of `NSString` objects listing the types of data that you should write to the pasteboard. You should write data to the pasteboard for as many of the types as you support.

## See Also

### Related Documentation
- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](../nsresponder/validrequestor%28forsendtype,returntype%29.md)
  Overridden by subclasses to determine what services are available.
### Working with Pasteboards
- [func readSelection(from: NSPasteboard) -> Bool](./readselection%28from%29.md)
  Reads data from the pasteboard and uses it to replace the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/writeselection(to:types:))*