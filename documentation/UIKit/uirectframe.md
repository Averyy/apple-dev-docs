# UIRectFrame(_:)

**Framework**: UIKit  
**Kind**: func

Draws a frame around the inside of the specified rectangle.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func UIRectFrame(_ rect: CGRect)
```

#### Discussion

This function draws a frame around the inside of `rect` in the stroke color of the current graphics context and using the `kCGBlendModeCopy` blend mode. The width is equal to 1.0 in the current coordinate system. Because the frame is drawn inside the rectangle, it is visible even if drawing is clipped to the rectangle. If the current graphics context is `nil`, this function does nothing.

This function may be called from any thread of your app.

## Parameters

- `rect`: The rectangle defining the area in which to draw.

## See Also

- [class UIBezierPath](uibezierpath.md)
  A path that consists of straight and curved line segments that you can render in your custom views.
- [func UIRectFill(CGRect)](uirectfill(_:).md)
  Fills the specified rectangle with the current color.
- [func UIRectFillUsingBlendMode(CGRect, CGBlendMode)](uirectfillusingblendmode(_:_:).md)
  Fills a rectangle with the current fill color using the specified blend mode.
- [func UIRectFrameUsingBlendMode(CGRect, CGBlendMode)](uirectframeusingblendmode(_:_:).md)
  Draws a frame around the inside of a rectangle using the specified blend mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectframe(_:))*