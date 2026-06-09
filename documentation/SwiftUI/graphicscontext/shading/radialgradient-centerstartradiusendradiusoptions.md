# radialGradient(_:center:startRadius:endRadius:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills a radial gradient.

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
static func radialGradient(_ gradient: AnyGradient, center: CGPoint, startRadius: CGFloat, endRadius: CGFloat, options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a radial gradient.

## Parameters

- `gradient`: An [`AnyGradient`](anygradient.md) instance that defines the colors of the gradient.
- `center`: The point in the current user space on which SwiftUI centers the gradient.
- `startRadius`: The distance from the center where the gradient starts.
- `endRadius`: The distance from the center where the gradient ends.
- `options`: Options that you use to configure the gradient.

## See Also

- [static linearGradient(_:startPoint:endPoint:options:)](graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:).md)
  Returns a shading instance that fills a linear (axial) gradient.
- [static conicGradient(_:center:angle:options:)](graphicscontext/shading/conicgradient(_:center:angle:options:).md)
  Returns a shading instance that fills a conic (angular) gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:))*