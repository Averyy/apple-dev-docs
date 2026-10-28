# pasteAsPlainText(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Inserts the contents of the pasteboard into the receiver’s text as plain text.

**Availability**:
- macOS

## Declaration

```swift
func pasteAsPlainText(_ sender: Any?)
```

```objc
- (void) pasteAsPlainText:(id) sender;
```

## Discussion

This method behaves analogously to [`insertText(_:)`](./inserttext%28_%29.md).

## Parameters

- `sender`: The control that sent the message; may be `nil`.

## See Also

### Related Documentation
- [func insertText(Any)](./inserttext%28_%29.md)
  Inserts `aString` into the receiver’s text at the insertion point if there is one, otherwise replacing the selection.
### Clicking and pasting
- [func clicked(onLink: Any, at: Int)](./clicked%28onlink,at%29.md)
  Causes the text view to act as if the user clicked on some text with the given link as the value of a link attribute associated with the text.
- [func pasteAsRichText(Any?)](./pasteasrichtext%28_%29.md)
  This action method inserts the contents of the pasteboard into the receiver’s text as rich text, maintaining its attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextview/pasteasplaintext(_:))*