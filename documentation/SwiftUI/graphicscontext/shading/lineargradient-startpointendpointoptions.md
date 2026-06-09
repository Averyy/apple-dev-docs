# linearGradient(_:startPoint:endPoint:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading instance that fills a linear (axial) gradient.

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
static func linearGradient(_ gradient: AnyGradient, startPoint: CGPoint, endPoint: CGPoint, options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a linear gradient.

#### Discussion

The shading instance defines an axis from `startPoint` to `endPoint` in the current user space and maps colors from `gradient` to lines perpendicular to the axis.

## Parameters

- `gradient`: An [`AnyGradient`](anygradient.md) instance that defines the colors of the gradient.
- `startPoint`: The start point of the gradient axis.
- `endPoint`: The end point of the gradient axis.
- `options`: Options that you use to configure the gradient.

## See Also

- [static radialGradient(_:center:startRadius:endRadius:options:)](graphicscontext/shading/radialgradient(_:center:startradius:endradius:options:).md)
  Returns a shading instance that fills a radial gradient.
- [static conicGradient(_:center:angle:options:)](graphicscontext/shading/conicgradient(_:center:angle:options:).md)
  Returns a shading instance that fills a conic (angular) gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/lineargradient(_:startpoint:endpoint:options:))*