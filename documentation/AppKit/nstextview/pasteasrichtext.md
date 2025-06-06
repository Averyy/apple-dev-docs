# pasteAsRichText(_:)

**Framework**: AppKit  
**Kind**: method

This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func pasteAsRichText(_ sender: Any?)
```

#### Discussion

The text is inserted at the insertion point if there is one, otherwise replacing the selection.

## Parameters

- `sender`: The control that sent the message; may be  .

## See Also

- [func insertText(Any)](nstextview/inserttext(_:).md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
- [func clicked(onLink: Any, at: Int)](nstextview/clicked(onlink:at:).md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
- [func pasteAsPlainText(Any?)](nstextview/pasteasplaintext(_:).md)
  Inserts the contents of the pasteboard into the receiver’s text as plain text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/pasteasrichtext(_:))*