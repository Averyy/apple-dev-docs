# highlightedTextColor

**Framework**: UIKit  
**Kind**: property

The highlight color for the label’s text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var highlightedTextColor: UIColor? { get set }
```

#### Discussion

Subclasses that use labels to implement a type of text button can use the value in this property when drawing the pressed state for the button. The label uses this value to display text whenever the [`isHighlighted`](uilabel/ishighlighted.md) property is [`true`](https://developer.apple.com/documentation/Swift/true).

The default value of this property is `nil`.

## See Also

- [var isHighlighted: Bool](uilabel/ishighlighted.md)
  A Boolean value that determines whether the label draws its text with a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/highlightedtextcolor)*