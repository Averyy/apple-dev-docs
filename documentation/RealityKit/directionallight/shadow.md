# shadow

**Framework**: RealityKit  
**Kind**: property

The shadow settings for a directional light.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency var shadow: DirectionalLightComponent.Shadow? { get set }
```

#### Discussion

Set this value to `nil` to remove shadows.

## See Also

- [var light: DirectionalLightComponent](directionallight/light.md)
  A directional light component for the entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallight/shadow)*