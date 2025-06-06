# conicGradient(_:center:angle:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills a conic (angular) gradient.

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
static func conicGradient(_ gradient: Gradient, center: CGPoint, angle: Angle = Angle(), options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a conic gradient.

## Parameters

- `gradient`: A   instance that defines the colors   of the gradient.
- `center`: The point in the current user space on which SwiftUI   centers the gradient.
- `angle`: The angle about the center that SwiftUI uses to start and   finish the gradient. The gradient sweeps all the way around the   center.
- `options`: Options that you use to configure the gradient.

## See Also

- [static func linearGradient(Gradient, startPoint: CGPoint, endPoint: CGPoint, options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading](graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:).md)
  Returns a shading instance that fills a linear (axial) gradient.
- [static func radialGradient(Gradient, center: CGPoint, startRadius: CGFloat, endRadius: CGFloat, options: GraphicsContext.GradientOptions) -> GraphicsContext.Shading](graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:).md)
  Returns a shading instance that fills a radial gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/conicgradient(_:center:angle:options:))*