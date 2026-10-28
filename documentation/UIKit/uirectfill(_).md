# UIRectFill(_:)

**Framework**: UIKit  
**Kind**: func  
**Role**: Function

Fills the specified rectangle with the current color.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS 2.0+

## Declaration

```swift
func UIRectFill(_ rect: CGRect)
```

```c
extern void UIRectFill(CGRect rect);
```

## Discussion

Fills the specified rectangle using the fill color of the current graphics context and the `kCGBlendModeCopy` blend mode.

This function may be called from any thread of your app.

## Parameters

- `rect`: The rectangle defining the area in which to draw.

## See Also

### Paths
- [class UIBezierPath](./uibezierpath.md)
  A path that consists of straight and curved line segments that you can render in your custom views.
- [func UIRectFillUsingBlendMode(CGRect, CGBlendMode)](./uirectfillusingblendmode%28_,_%29.md)
  Fills a rectangle with the current fill color using the specified blend mode.
- [func UIRectFrame(CGRect)](./uirectframe%28_%29.md)
  Draws a frame around the inside of the specified rectangle.
- [func UIRectFrameUsingBlendMode(CGRect, CGBlendMode)](./uirectframeusingblendmode%28_,_%29.md)
  Draws a frame around the inside of a rectangle using the specified blend mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectfill(_:))*