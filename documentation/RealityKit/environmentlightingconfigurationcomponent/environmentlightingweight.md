# environmentLightingWeight

**Framework**: RealityKit  
**Kind**: property

A value that controls the environment-lighting contribution to an entity’s lighting.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var environmentLightingWeight: Float
```

#### Discussion

The weight is a floating-point value in the range `[0.0, 1.0]`.

- A value of `1.0` indicates the entity receives the full environment-lighting contribution.
- A value of `0.0` indicates the entity receives no light from its environment. The entity still receives lighting from other sources, such as directional, point, and spot lights.
- The default value is `1.0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentlightingconfigurationcomponent/environmentlightingweight)*