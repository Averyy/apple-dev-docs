# EnvironmentBlendingComponent.BlendingMode

**Framework**: RealityKit  
**Kind**: struct

A struct that encapsulates the different environment-blending modes that can be applied to an entity

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct BlendingMode
```

## Topics

### Type Properties
- [static var `default`: EnvironmentBlendingComponent.BlendingMode](environmentblendingcomponent/blendingmode/default.md)
  No special blending is applied
### Type Methods
- [static func occluded(by: EnvironmentBlendingComponent.EnvironmentType) -> EnvironmentBlendingComponent.BlendingMode](environmentblendingcomponent/blendingmode/occluded(by:).md)
  The entity will receive a depth-based occlusion treatment within the specified environment type

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/environmentblendingcomponent/blendingmode)*