# setMarkedText(_:selectedRange:replacementRange:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Replaces a specified range in the receiver’s text storage with the given string and sets the selection.

**Availability**:
- macOS ?+

## Declaration

```swift
func setMarkedText(_ string: Any, selectedRange: NSRange, replacementRange: NSRange)
```

#### Discussion

If there is no marked text, the current selection is replaced. If there is no selection, the string is inserted at the insertion point.

When `aString` is an `NSString` object, the receiver is expected to render the marked text with distinguishing appearance (for example, `NSTextView` renders with [`markedTextAttributes`](nstextview/markedtextattributes.md)).

## Parameters

- `string`: The string to insert. Can be either an   or   instance.
- `selectedRange`: The range to set as the selection, computed from the beginning of the inserted string.
- `replacementRange`: The range to replace, computed from the beginning of the marked text.

## See Also

- [func hasMarkedText() -> Bool](nstextinputclient/hasmarkedtext.md)
  Returns a Boolean value indicating whether the receiver has marked text.
- [func markedRange() -> NSRange](nstextinputclient/markedrange.md)
  Returns the range of the marked text.
- [func selectedRange() -> NSRange](nstextinputclient/selectedrange.md)
  Returns the range of selected text.
- [func unmarkText()](nstextinputclient/unmarktext.md)
  Unmarks the marked text.
- [func validAttributesForMarkedText() -> [NSAttributedString.Key]](nstextinputclient/validattributesformarkedtext.md)
  Returns an array of attribute names recognized by the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinputclient/setmarkedtext(_:selectedrange:replacementrange:))*