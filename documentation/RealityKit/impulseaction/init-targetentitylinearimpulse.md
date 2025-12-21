# init(targetEntity:linearImpulse:)

**Framework**: RealityKit  
**Kind**: init

Creates a new impulse action.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(targetEntity: ActionEntityResolution = .sourceEntity, linearImpulse: SIMD3<Float> = [0, 1, 0])
```

## Parameters

- `targetEntity`: The entity that the impulse acts upon.
- `linearImpulse`: The impulse in newton seconds (in physics simulation space).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/impulseaction/init(targetentity:linearimpulse:))*