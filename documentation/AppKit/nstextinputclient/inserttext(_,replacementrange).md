# insertText(_:replacementRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Inserts the given string into the receiver, replacing the specified content.

**Availability**:
- macOS

## Declaration

```swift
func insertText(_ string: Any, replacementRange: NSRange)
```

```objc
- (void) insertText:(id) string replacementRange:(NSRange) replacementRange;
```

## Mentions

- [Supporting Writing Tools via the pasteboard](../supporting-writing-tools-via-the-pasteboard.md)

#### Discussion

This method is the entry point for inserting text typed by the user and is generally not suitable for other purposes. Programmatic modification of the text is best done by operating on the text storage directly. Because this method pertains to the actions of the user, the text view must be editable for the insertion to work.

## Parameters

- `string`: The text to insert, either an `NSString` or `NSAttributedString` instance.
- `replacementRange`: The range of content to replace in the receiver’s text storage.

## See Also

### Storing text
- [func attributedString() -> NSAttributedString](./attributedstring%28%29.md)
  Returns an attributed string representing the receiver’s text storage.
- [func attributedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](./attributedsubstring%28forproposedrange,actualrange%29.md)
  Returns an attributed string derived from the given range in the receiver’s text storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/inserttext(_:replacementrange:))*