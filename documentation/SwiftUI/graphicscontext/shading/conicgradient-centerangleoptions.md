# conicGradient(_:center:angle:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills a conic (angular) gradient.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func conicGradient(_ gradient: AnyGradient, center: CGPoint, angle: Angle = Angle(), options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a conic gradient.

## Parameters

- `gradient`: An [`AnyGradient`](anygradient.md) instance that defines the colors of the gradient.
- `center`: The point in the current user space on which SwiftUI centers the gradient.
- `angle`: The angle about the center that SwiftUI uses to start and finish the gradient. The gradient sweeps all the way around the center.
- `options`: Options that you use to configure the gradient.

## See Also

- [static linearGradient(_:startPoint:endPoint:options:)](graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:).md)
  Returns a shading instance that fills a linear (axial) gradient.
- [static radialGradient(_:center:startRadius:endRadius:options:)](graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:).md)
  Returns a shading instance that fills a radial gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/conicgradient(_:center:angle:options:))*