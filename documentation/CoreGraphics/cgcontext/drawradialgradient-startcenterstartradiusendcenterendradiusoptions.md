# drawRadialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)

**Framework**: Core Graphics  
**Kind**: method

Paints a gradient fill that varies along the area defined by the provided starting and ending circles.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func drawRadialGradient(_ gradient: CGGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: CGGradientDrawingOptions)
```

#### Discussion

The color at location 0 in the CGGradient object is mapped to the circle defined by `startCenter` and `startRadius`. The color at location 1 in the CGGradient object is mapped to the circle defined by `endCenter` and `endRadius`. Colors are linearly interpolated between the starting and ending circles based on the location values of the gradient. The option flags control whether the gradient is drawn before the start point or after the end point.

## Parameters

- `gradient`: A CGGradient object.
- `startCenter`: The coordinate that defines the center of the starting circle.
- `startRadius`: The radius of the starting circle.
- `endCenter`: The coordinate that defines the center of the ending circle.
- `endRadius`: The radius of the ending circle.
- `options`: Option flags (  or  ) that control whether the gradient is drawn before the starting circle or after the ending circle.

## See Also

- [func drawLinearGradient(CGGradient, start: CGPoint, end: CGPoint, options: CGGradientDrawingOptions)](cgcontext/drawlineargradient(_:start:end:options:).md)
  Paints a gradient fill that varies along the line defined by the provided starting and ending points.
- [struct CGGradientDrawingOptions](cggradientdrawingoptions.md)
  Drawing locations for gradients.
- [func drawShading(CGShading)](cgcontext/drawshading(_:).md)
  Fills the clipping path of a context with the specified shading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/drawradialgradient(_:startcenter:startradius:endcenter:endradius:options:))*