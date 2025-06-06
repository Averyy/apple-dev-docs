# markedTextRange

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

Range representing the position of the markedText.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var markedTextRange: UITextRange? { get }
```

#### Discussion

If text can be selected, it can be marked. Marked text represents provisionally inserted text that has yet to be confirmed by the user.  It requires unique visual treatment in its display.  If there is any marked text, the selection, whether a caret or an extended range, always resides within.

Setting marked text either replaces the existing marked text or, if none is present, inserts it from the current selection.

Return nil if no marked text

## See Also

- [var markedText: String?](betextinput/markedtext.md)
  String for the text that has been marked as part of an active input session
- [var attributedMarkedText: NSAttributedString?](betextinput/attributedmarkedtext.md)
  Attributed string for the text that has been marked as part of an active input session
- [var hasMarkedText: Bool](betextinput/hasmarkedtext.md)
  Indicates whether there any text is currently marked as part of an active input session
- [func setMarkedText(String?, selectedRange: NSRange)](betextinput/setmarkedtext(_:selectedrange:).md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](betextinput/setattributedmarkedtext(_:selectedrange:).md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](betextinput/unmarktext.md)
  Unmarks the currently marked text
- [func isPointNearMarkedText(CGPoint) -> Bool](betextinput/ispointnearmarkedtext(_:).md)
  Returns whether a point should be considered “near” the marked text. Used to determine whether text interaction gestures near marked text should begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/markedtextrange)*