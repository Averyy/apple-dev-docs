# pasteAsPlainText(_:)

**Framework**: AppKit  
**Kind**: method

Inserts the contents of the pasteboard into the receiver’s text as plain text.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func pasteAsPlainText(_ sender: Any?)
```

#### Discussion

This method behaves analogously to [`insertText(_:)`](nstextview/inserttext(_:).md).

## Parameters

- `sender`: The control that sent the message; may be  .

## See Also

- [func insertText(Any)](nstextview/inserttext(_:).md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
- [func clicked(onLink: Any, at: Int)](nstextview/clicked(onlink:at:).md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
- [func pasteAsRichText(Any?)](nstextview/pasteasrichtext(_:).md)
  This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/pasteasplaintext(_:))*