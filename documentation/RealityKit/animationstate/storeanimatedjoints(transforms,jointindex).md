# storeAnimatedJoints(transforms:jointIndex:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Stores a subset of animated joints.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@discardableResult
func storeAnimatedJoints(transforms: [Transform], jointIndex: Int) -> Bool
```

Available when `Value` is `JointTransforms`.

## Discussion

See [`storeAnimatedValue(_:)`](../animationstateprotocol/storeanimatedvalue%28_%29.md) for more about returning an animation result to the animation system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/animationstate/storeanimatedjoints(transforms:jointindex:))*