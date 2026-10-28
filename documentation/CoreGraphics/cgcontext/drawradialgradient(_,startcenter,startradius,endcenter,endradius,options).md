# drawRadialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)

**Framework**: Core Graphics  
**Kind**: method  
**Role**: Instance Method

Paints a gradient fill that varies along the area defined by the provided starting and ending circles.

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
func drawRadialGradient(_ gradient: CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)
```

```c
extern void CGContextDrawRadialGradient(CGContextRef c, CGGradientRef gradient, CGPoint startCenter, CGFloat startRadius, CGPoint endCenter, CGFloat endRadius, CGGradientDrawingOptions options);
```

## Discussion

The color at location 0 in the CGGradient object is mapped to the circle defined by `startCenter` and `startRadius`. The color at location 1 in the CGGradient object is mapped to the circle defined by `endCenter` and `endRadius`. Colors are linearly interpolated between the starting and ending circles based on the location values of the gradient. The option flags control whether the gradient is drawn before the start point or after the end point.

## Parameters

- `gradient`: A CGGradient object.
- `startCenter`: The coordinate that defines the center of the starting circle.
- `startRadius`: The radius of the starting circle.
- `endCenter`: The coordinate that defines the center of the ending circle.
- `endRadius`: The radius of the ending circle.
- `options`: Option flags ([`drawsBeforeStartLocation`](../cggradientdrawingoptions/drawsbeforestartlocation.md) or [`drawsAfterEndLocation`](../cggradientdrawingoptions/drawsafterendlocation.md)) that control whether the gradient is drawn before the starting circle or after the ending circle.

## See Also

### Drawing Gradients and Shadings
- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](./drawlineargradient%28_,start,end,options%29.md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [struct CGGradientDrawingOptions](../cggradientdrawingoptions.md)
  Drawing locations for gradients.
- [func drawShading(CGShading)](./drawshading%28_%29.md)
  Fills the clipping path of a context with the specified shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:))*