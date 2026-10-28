# markedTextRange

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A range that represents the position of the marked text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var markedTextRange: UITextRange? { get }
```

```objc
@property (nonatomic, readonly, nullable) UITextRange * markedTextRange;
```

## Discussion

Return `nil` if no marked text exists.

Marked text represents provisionally inserted text that a person needs to confirm before you commit it to the document. You display marked text with a distinct visual look. The selection needs to reside in market text, if any exists.

When you commit marked text to the document, replace any existing marked text. If no marked text is present, insert the market text into the document at the location of the current selection.

## See Also

### Managing marked text
- [var hasMarkedText: Bool](./hasmarkedtext.md)
  A Boolean value that indicates if marked text exists for an active input session.
- [func unmarkText()](./unmarktext%28%29.md)
  Unmarks the currently marked text.
- [func isPointNearMarkedText(CGPoint) -> Bool](./ispointnearmarkedtext%28_%29.md)
  Provides a Boolean value that indicates if a point is near marked text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/markedtextrange)*