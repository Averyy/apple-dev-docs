# writeSelection(to:types:)

**Framework**: AppKit  
**Kind**: method

Writes the current selection to the pasteboard.

**Availability**:
- macOS ?+

## Declaration

```swift
optional func writeSelection(to pboard: NSPasteboard, types: [NSPasteboard.PasteboardType]) -> Bool
```

## Mentions

- [Supporting Writing Tools via the pasteboard](supporting-writing-tools-via-the-pasteboard.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if your implementation was able to write one or more types to the pasteboard; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

A [`writeSelection(to:types:)`](nsservicesmenurequestor/writeselection(to:types:).md) message is sent to the first responder when the user chooses a command from the Services menu, but only if the receiver didn’t return `nil` to a previous [`validRequestor(forSendType:returnType:)`](nsresponder/validrequestor(forsendtype:returntype:).md) message.

After your method writes the data to the pasteboard, a remote message is sent to the application that provides the service the user requested. If the service provider supplies return data to replace the selection, the first responder will then receive a [`readSelection(from:)`](nsservicesmenurequestor/readselection(from:).md) message.

## Parameters

- `pboard`: The pasteboard to receive your data.
- `types`: An array of   objects listing the types of data that you should write to the pasteboard. You should write data to the pasteboard for as many of the types as you support.

## See Also

- [func validRequestor(forSendType: NSPasteboard.PasteboardType?, returnType: NSPasteboard.PasteboardType?) -> Any?](nsresponder/validrequestor(forsendtype:returntype:).md)
  Overridden by subclasses to determine what services are available.
- [func readSelection(from: NSPasteboard) -> Bool](nsservicesmenurequestor/readselection(from:).md)
  Reads data from the pasteboard and uses it to replace the current selection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsservicesmenurequestor/writeselection(to:types:))*