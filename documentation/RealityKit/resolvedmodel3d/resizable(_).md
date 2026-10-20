# resizable(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Allows this model to resize itself to fit its container.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func resizable(_ isResizable: Bool = true) -> ResolvedModel3D
```

#### Discussion

> **Note**: By default, `Model3D` sizes itself based on the intrinsic size of the underlying model file. Setting this will scale the model to fit its container instead. To preserve the intrinsic aspect ratio of the model, use https://developer.apple.com/documentation/SwiftUI/View/aspectRatio(_:contentMode:).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/resizable(_:))*