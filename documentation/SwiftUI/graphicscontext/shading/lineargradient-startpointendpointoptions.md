# linearGradient(_:startPoint:endPoint:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills a linear (axial) gradient.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static func linearGradient(_ gradient: Gradient, startPoint: CGPoint, endPoint: CGPoint, options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a linear gradient.

#### Discussion

The shading instance defines an axis from `startPoint` to `endPoint` in the current user space and maps colors from `gradient` to lines perpendicular to the axis.

## Parameters

- `gradient`: A   instance that defines the colors   of the gradient.
- `startPoint`: The start point of the gradient axis.
- `endPoint`: The end point of the gradient axis.
- `options`: Options that you use to configure the gradient.

## See Also

- [static func radialGradient(Gradient, center: CGPoint, startRadius: CGFloat, endRadius: CGFloat, options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading](graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:).md)
  Returns a shading instance that fills a radial gradient.
- [static func conicGradient(Gradient, center: CGPoint, angle: Angle, options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading](graphicscontext/shading/conicgradient(_:center:angle:options:).md)
  Returns a shading instance that fills a conic (angular) gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:))*