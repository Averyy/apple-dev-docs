# UIRectFillUsingBlendMode(_:_:)

**Framework**: UIKit  
**Kind**: func

Fills a rectangle with the current fill color using the specified blend mode.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 2.0+

## Declaration

```swift
func UIRectFillUsingBlendMode(_ rect: CGRect, _ blendMode: CGBlendMode)
```

#### Discussion

This function draws the rectangle in the current graphics context. If the current graphics context is `nil`, this function does nothing.

This function may be called from any thread of your app.

## Parameters

- `rect`: The rectangle defining the area in which to draw.
- `blendMode`: The blend mode to use during drawing.

## See Also

- [class UIBezierPath](uibezierpath.md)
  A path that consists of straight and curved line segments that you can render in your custom views.
- [func UIRectFill(CGRect)](uirectfill(_:).md)
  Fills the specified rectangle with the current color.
- [func UIRectFrame(CGRect)](uirectframe(_:).md)
  Draws a frame around the inside of the specified rectangle.
- [func UIRectFrameUsingBlendMode(CGRect, CGBlendMode)](uirectframeusingblendmode(_:_:).md)
  Draws a frame around the inside of a rectangle using the specified blend mode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uirectfillusingblendmode(_:_:))*