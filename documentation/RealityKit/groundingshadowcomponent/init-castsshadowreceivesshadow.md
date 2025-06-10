# init(castsShadow:receivesShadow:)

**Framework**: RealityKit  
**Kind**: init

Creates a grounding shadow component by configuring whether its entity receives shadows from other model entities with the component.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(castsShadow: Bool, receivesShadow: Bool)
```

#### Discussion

This initializer is an alternative to [`init(castsShadow:)`](groundingshadowcomponent/init(castsshadow:).md), which creates a component that, by default, configures an entity to receive grounding shadows from other model entities in the scene.

## Parameters

- `castsShadow`: A Boolean value that indicates whether the component’s   entity casts a shadow on the environment and other model entities.
- `receivesShadow`: A Boolean value that indicates whether the   component’s entity receives shadows from other model entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/groundingshadowcomponent/init(castsshadow:receivesshadow:))*