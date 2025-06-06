# isHighlighted

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the label draws its text with a highlight.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isHighlighted: Bool { get set }
```

#### Discussion

Setting this property causes the label to redraw with the appropriate highlight state. A subclass implementing a text button might set this property to [`true`](https://developer.apple.com/documentation/swift/true) when the user presses the button and set it to [`false`](https://developer.apple.com/documentation/swift/false) at other times. In order for the label to draw the highlight, the [`highlightedTextColor`](uilabel/highlightedtextcolor.md) property must contain a non-`nil` value.

The default value of this property is [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [var highlightedTextColor: UIColor?](uilabel/highlightedtextcolor.md)
  The highlight color for the label’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/ishighlighted)*