# projectionTransform(_:)

**Framework**: SwiftUI  
**Kind**: method

Returns a filter that transforms the rasterized form of subsequent graphics primitives.

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
static func projectionTransform(_ matrix: ProjectionTransform) -> GraphicsContext.Filter
```

#### Return Value

A filter that applies a transform.

## Parameters

- `matrix`: A projection transform to apply to the rasterized   form of graphics primitives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/graphicscontext/filter/projectiontransform(_:))*