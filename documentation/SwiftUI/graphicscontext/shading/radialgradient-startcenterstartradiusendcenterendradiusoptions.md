# radialGradient(_:startCenter:startRadius:endCenter:endRadius:options:)

**Framework**: SwiftUI  
**Kind**: method

Returns a shading that fills a two-point radial gradient.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
static func radialGradient(_ gradient: AnyGradient, startCenter: CGPoint, startRadius: CGFloat, endCenter: CGPoint, endRadius: CGFloat, options: GraphicsContext.GradientOptions = GradientOptions()) -> GraphicsContext.Shading
```

#### Return Value

A shading instance filled with a radial gradient.

## Parameters

- `gradient`: An [`AnyGradient`](anygradient.md) instance that defines the colors of the gradient.
- `startCenter`: The strat point in the current user space on which SwiftUI centers the gradient.
- `startRadius`: The distance from the center where the gradient starts.
- `endCenter`: The end point in the current user space on which SwiftUI centers the gradient.
- `endRadius`: The distance from the center where the gradient ends.
- `options`: Options that you use to configure the gradient.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/shading/radialgradient(_:startcenter:startradius:endcenter:endradius:options:))*