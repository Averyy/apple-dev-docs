# draw(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws the entire image in the specified rectangle, scaling it as necessary to fit.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func draw(in rect: CGRect)
```

```objc
- (void) drawInRect:(CGRect) rect;
```

#### Discussion

This method draws the entire image in the current graphics context, respecting the image’s orientation setting. In the default coordinate system, images are situated down and to the right of the origin of the specified rectangle. This method respects any transforms applied to the current graphics context, however.

This method draws the image at full opacity using the [`CGBlendMode.normal`](../../CoreGraphics/cgblendmode/normal.md) blend mode.

## Parameters

- `rect`: The rectangle (in the coordinate system of the graphics context) in which to draw the image.

## See Also

### Drawing images
- [func draw(at: CGPoint)](./draw%28at%29.md)
  Draws the image at the specified point in the current context.
- [func draw(at: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)](./draw%28at,blendmode,alpha%29.md)
  Draws the entire image at the specified point using the custom compositing options.
- [func draw(in: CGRect, blendMode: CGBlendMode, alpha: CGFloat)](./draw%28in,blendmode,alpha%29.md)
  Draws the entire image in the specified rectangle using the specified compositing options.
- [func drawAsPattern(in: CGRect)](./drawaspattern%28in%29.md)
  Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/draw(in:))*