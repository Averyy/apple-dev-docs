# unmarkText()

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Unmarks the marked text.

**Availability**:
- macOS ?+

## Declaration

```swift
func unmarkText()
```

#### Discussion

The receiver removes any marking from pending input text and disposes of the marked text as it wishes. The text view should accept the marked text as if it had been inserted normally. If there is no marked text, the invocation of this method has no effect.

## See Also

- [func hasMarkedText() -> Bool](nstextinputclient/hasmarkedtext.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func markedRange() -> NSRange](nstextinputclient/markedrange.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](nstextinputclient/selectedrange.md)
  Returns the range of selected text.
- [func setMarkedText(Any, selectedRange: NSRange, replacementRange: NSRange)](nstextinputclient/setmarkedtext(_:selectedrange:replacementrange:).md)
  Replaces a specified range in the receiver’s text storage with the given string and sets the selection.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](nstextinputclient/validattributesformarkedtext.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/unmarktext())*