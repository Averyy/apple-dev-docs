# textRect(forBounds:limitedToNumberOfLines:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the label’s text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func textRect(forBounds bounds: CGRect, limitedToNumberOfLines numberOfLines: Int) -> CGRect
```

```objc
- (CGRect) textRectForBounds:(CGRect) bounds limitedToNumberOfLines:(NSInteger) numberOfLines;
```

#### Return Value

The computed drawing rectangle for the label’s text.

#### Discussion

Override this method in subclasses that require changes in the label’s bounding rectangle to occur before the system performs other text layout calculations. Use the value in the `numberOfLines` parameter to limit the height of the returned rectangle to the specified number of lines of text.

The system may call this method if there was a prior call to the [`sizeToFit()`](../uiview/sizetofit%28%29.md) or [`sizeThatFits(_:)`](../uiview/sizethatfits%28_%29.md) method. Note that labels in [`UITableViewCell`](../uitableviewcell.md) objects have sizes based on cell dimensions, and not on a requested size.

## Parameters

- `bounds`: The bounding rectangle of the label.
- `numberOfLines`: The maximum number of lines to use for the label. The value `0` indicates the label has no maximum number of lines and the rectangle should encompass all of the text.

## See Also

### Drawing and positioning overrides
- [func drawText(in: CGRect)](./drawtext%28in%29.md)
  Draws the label’s text, or its shadow, in the specified rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/textrect(forbounds:limitedtonumberoflines:))*