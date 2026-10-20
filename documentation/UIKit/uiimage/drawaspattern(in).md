# drawAsPattern(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Draws a tiled Quartz pattern using the receiver’s contents as the tile pattern.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drawAsPattern(in rect: CGRect)
```

```objc
- (void) drawAsPatternInRect:(CGRect) rect;
```

#### Discussion

This method uses a Quartz pattern to tile the image in the specified rectangle. The image is tiled with no gaps and the fill color is ignored. In the default coordinate system, the image tiles are situated down and to the right of the origin of the specified rectangle. This method respects any transforms applied to the current graphics context, however.

## Parameters

- `rect`: The rectangle (in the coordinate system of the graphics context) in which to draw the image.

## See Also

### Drawing images
- [func draw(at: CGPoint)](./draw%28at%29.md)
  Draws the image at the specified point in the current context.
- [func draw(at: CGPoint, blendMode: CGBlendMode, alpha: CGFloat)](./draw%28at,blendmode,alpha%29.md)
  Draws the entire image at the specified point using the custom compositing options.
- [func draw(in: CGRect)](./draw%28in%29.md)
  Draws the entire image in the specified rectangle, scaling it as necessary to fit.
- [func draw(in: CGRect, blendMode: CGBlendMode, alpha: CGFloat)](./draw%28in,blendmode,alpha%29.md)
  Draws the entire image in the specified rectangle using the specified compositing options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/drawaspattern(in:))*