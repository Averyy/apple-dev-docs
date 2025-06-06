# drawShading(_:)

**Framework**: Core Graphics  
**Kind**: method

Fills the clipping path of a context with the specified shading.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drawShading(_ shading: CGShading)
```

#### Discussion

The preferred way to draw gradients is to use a CGGradient object. See [`CGGradient`](cggradient.md).

## Parameters

- `shading`: A shading object. The shading object is retained; upon return, you may safely release it.

## See Also

- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:).md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](cgcontext/drawlineargradient(_:start:end:options:).md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](cgcontext/drawlineargradient(_:start:end:options:).md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:).md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [struct CGGradientDrawingOptions](cggradientdrawingoptions.md)
  Drawing locations for gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/drawshading(_:))*