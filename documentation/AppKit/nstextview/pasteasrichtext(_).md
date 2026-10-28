# pasteAsRichText(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.

**Availability**:
- macOS

## Declaration

```swift
func pasteAsRichText(_ sender: Any?)
```

```objc
- (void) pasteAsRichText:(id) sender;
```

## Discussion

The text is inserted at the insertion point if there is one, otherwise replacing the selection.

## Parameters

- `sender`: The control that sent the message; may be `nil`.

## See Also

### Related Documentation
- [func insertText(Any)](./inserttext%28_%29.md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
### Clicking and pasting
- [func clicked(onLink: Any, at: Int)](./clicked%28onlink,at%29.md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
- [func pasteAsPlainText(Any?)](./pasteasplaintext%28_%29.md)
  Inserts the contents of the pasteboard into the receiver’s text as plain text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/pasteasrichtext(_:))*