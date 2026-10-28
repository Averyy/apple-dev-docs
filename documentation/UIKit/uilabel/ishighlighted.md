# isHighlighted

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the label draws its text with a highlight.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var isHighlighted: Bool { get set }
```

```objc
@property (nonatomic, getter=isHighlighted) BOOL highlighted;
```

## Discussion

Setting this property causes the label to redraw with the appropriate highlight state. A subclass implementing a text button might set this property to [`true`](../../Swift/true.md) when the user presses the button and set it to [`false`](../../Swift/false.md) at other times. In order for the label to draw the highlight, the [`highlightedTextColor`](./highlightedtextcolor.md) property must contain a non-`nil` value.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Managing highlight values
- [var highlightedTextColor: UIColor?](./highlightedtextcolor.md)
  The highlight color for the label’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/ishighlighted)*