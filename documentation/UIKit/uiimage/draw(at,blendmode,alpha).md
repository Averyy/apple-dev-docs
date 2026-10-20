# draw(at:blendMode:alpha:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws the entire image at the specified point using the custom compositing options.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func draw(at point: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)
```

```objc
- (void) drawAtPoint:(CGPoint) point blendMode:(CGBlendMode) blendMode alpha:(CGFloat) alpha;
```

#### Discussion

This method draws the entire image in the current graphics context, respecting the image’s orientation setting. In the default coordinate system, images are situated down and to the right of the specified point. This method respects any transforms applied to the current graphics context, however.

## Parameters

- `point`: The point at which to draw the top-left corner of the image.
- `blendMode`: The blend mode to use when compositing the image.
- `alpha`: The desired opacity of the image, specified as a value between 0.0 and 1.0. A value of 0.0 renders the image totally transparent while 1.0 renders it fully opaque. Values larger than 1.0 are interpreted as 1.0.

## See Also

### Drawing images
- [func draw(at: CGPoint)](./draw%28at%29.md)
  Draws the image at the specified point in the current context.
- [func draw(in: CGRect)](./draw%28in%29.md)
  Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [func draw(in: CGRect, blendMode: CGBlendMode, alpha: CGFloat)](./draw%28in,blendmode,alpha%29.md)
  Draws the entire image in the specified rectangle using the specified compositing options.
- [func drawAsPattern(in: CGRect)](./drawaspattern%28in%29.md)
  Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/draw(at:blendmode:alpha:))*