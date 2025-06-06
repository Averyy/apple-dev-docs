# drawAsPattern(in:)

**Framework**: UIKit  
**Kind**: method

Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drawAsPattern(in rect: CGRect)
```

#### Discussion

This method uses a Quartz pattern to tile the image in the specified rectangle. The image is tiled with no gaps and the fill color is ignored. In the default coordinate system, the image tiles are situated down and to the right of the origin of the specified rectangle. This method respects any transforms applied to the current graphics context, however.

## Parameters

- `rect`: The rectangle (in the coordinate system of the graphics context) in which to draw the image.

## See Also

- [func draw(at: CGPoint)](uiimage/draw(at:).md)
  Draws the image at the specified point in the current context.
- [func draw(at: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)](uiimage/draw(at:blendmode:alpha:).md)
  Draws the entire image at the specified point using the custom compositing options.
- [func draw(in: CGRect)](uiimage/draw(in:).md)
  Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [func draw(in: CGRect, blendMode: CGBlendMode, alpha: CGFloat)](uiimage/draw(in:blendmode:alpha:).md)
  Draws the entire image in the specified rectangle using the specified compositing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/drawaspattern(in:))*