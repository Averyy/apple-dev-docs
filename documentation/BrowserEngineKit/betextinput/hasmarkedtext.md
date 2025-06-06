# hasMarkedText

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

Indicates whether there any text is currently marked as part of an active input session

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var hasMarkedText: Bool { get }
```

## See Also

- [var markedText: String?](betextinput/markedtext.md)
  String for the text that has been marked as part of an active input session
- [var attributedMarkedText: NSAttributedString?](betextinput/attributedmarkedtext.md)
  Attributed string for the text that has been marked as part of an active input session
- [var markedTextRange: UITextRange?](betextinput/markedtextrange.md)
  Range representing the position of the markedText.
- [func setMarkedText(String?, selectedRange: NSRange)](betextinput/setmarkedtext(_:selectedrange:).md)
  Inserts the provided text and marks it to indicate that it is part of an active input session.
- [func setAttributedMarkedText(NSAttributedString?, selectedRange: NSRange)](betextinput/setattributedmarkedtext(_:selectedrange:).md)
  Inserts the provided styled text and marks it to indicate that it is part of an active input session.
- [func unmarkText()](betextinput/unmarktext.md)
  Unmarks the currently marked text
- [func isPointNearMarkedText(CGPoint) -> Bool](betextinput/ispointnearmarkedtext(_:).md)
  Returns whether a point should be considered “near” the marked text. Used to determine whether text interaction gestures near marked text should begin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/hasmarkedtext)*