# drawLinearGradient(_:start:end:options:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Paints a gradient fill that varies along the line defined by the provided starting and ending points.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drawLinearGradient(_ gradient: CGGradient, start startPoint: CGPoint, end endPoint: CGPoint, options: CGGradientDrawingOptions)
```

```c
extern void CGContextDrawLinearGradient(CGContextRef c, CGGradientRef gradient, CGPoint startPoint, CGPoint endPoint, CGGradientDrawingOptions options);
```

## Discussion

The color at location 0 in the CGGradient object is mapped to the starting point. The color at location 1 in the CGGradient object is mapped to the ending point. Colors are linearly interpolated between these two points based on the location values of the gradient. The option flags control whether the gradient is drawn before the start point or after the end point.

## Parameters

- `gradient`: A gradient object.
- `startPoint`: The coordinate that defines the starting point of the gradient.
- `endPoint`: The coordinate that defines the ending point of the gradient.
- `options`: Option flags ([`drawsBeforeStartLocation`](../cggradientdrawingoptions/drawsbeforestartlocation.md) or [`drawsAfterEndLocation`](../cggradientdrawingoptions/drawsafterendlocation.md)) that control whether the fill is extended beyond the starting or ending point.

## See Also

### Drawing Gradients and Shadings
- [func drawRadialGradient(CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)](./drawradialgradient%28_,startcenter,startradius,endcenter,endradius,options%29.md)
  Paints a gradient fill that varies along the area defined by the provided starting and ending circles.
- [struct CGGradientDrawingOptions](../cggradientdrawingoptions.md)
  Drawing locations for gradients.
- [func drawShading(CGShading)](./drawshading%28_%29.md)
  Fills the clipping path of a context with the specified shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/drawlineargradient(_:start:end:options:))*