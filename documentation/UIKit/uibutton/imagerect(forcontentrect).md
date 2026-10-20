# imageRect(forContentRect:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle in which the receiver draws its image.

**Availability**:
- iOS 2.0+ - Deprecated in 15.0
- iPadOS 2.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- tvOS 2.0+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`layoutSubviews()`](../uiview/layoutsubviews%28%29.md) instead.

## Declaration

```swift
func imageRect(forContentRect contentRect: CGRect) -> CGRect
```

```objc
- (CGRect) imageRectForContentRect:(CGRect) contentRect;
```

#### Return Value

The rectangle in which the receiver draws its image.

## Parameters

- `contentRect`: The content rectangle for the receiver.

## See Also

### Deprecated dimensions
- [func backgroundRect(forBounds: CGRect) -> CGRect](./backgroundrect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its background.
- [func contentRect(forBounds: CGRect) -> CGRect](./contentrect%28forbounds%29.md)
  Returns the rectangle in which the receiver draws its entire content.
- [func titleRect(forContentRect: CGRect) -> CGRect](./titlerect%28forcontentrect%29.md)
  Returns the rectangle in which the receiver draws its title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/imagerect(forcontentrect:))*