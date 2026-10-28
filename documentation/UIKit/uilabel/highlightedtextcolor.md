# highlightedTextColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The highlight color for the label’s text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var highlightedTextColor: UIColor? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIColor * highlightedTextColor;
```

## Discussion

Subclasses that use labels to implement a type of text button can use the value in this property when drawing the pressed state for the button. The label uses this value to display text whenever the [`isHighlighted`](./ishighlighted.md) property is [`true`](../../Swift/true.md).

The default value of this property is `nil`.

## See Also

### Managing highlight values
- [var isHighlighted: Bool](./ishighlighted.md)
  A Boolean value that determines whether the label draws its text with a highlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/highlightedtextcolor)*