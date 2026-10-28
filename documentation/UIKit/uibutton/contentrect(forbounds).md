# contentRect(forBounds:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in which the receiver draws its entire content.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 2.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`layoutSubviews()`](../uiview/layoutsubviews%28%29.md) instead.

## Declaration

```swift
func contentRect(forBounds bounds: CGRect) -> CGRect
```

```objc
- (CGRect) contentRectForBounds:(CGRect) bounds;
```

## Return Value

The rectangle in which the receiver draws its entire content.

## Discussion

The content rectangle is the area needed to display the image and title including any padding and adjustments for alignment and other settings.

## Parameters

- `bounds`: The bounding rectangle for the receiver.

## See Also

### Related Documentation
- [var contentEdgeInsets: UIEdgeInsets](./contentedgeinsets.md)
  The inset or outset margins for the rectangle surrounding all of the button’s content.
### Deprecated dimensions
- [func backgroundRect(forBounds: CGRect) -> CGRect](./backgroundrect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its background.
- [func titleRect(forContentRect: CGRect) -> CGRect](./titlerect%28forcontentrect%29.md)
  Returns the rectangle in which the receiver draws its title.
- [func imageRect(forContentRect: CGRect) -> CGRect](./imagerect%28forcontentrect%29.md)
  Returns the rectangle in which the receiver draws its image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/contentrect(forbounds:))*