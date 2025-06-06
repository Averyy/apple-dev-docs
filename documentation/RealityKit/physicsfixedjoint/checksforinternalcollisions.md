# checksForInternalCollisions

**Framework**: RealityKit  
**Kind**: property

A Boolean that indicates whether the joint checks and reports collisions between the two entity instances.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let checksForInternalCollisions: Bool
```

#### Discussion

The entities that [`PhysicsFixedJoint`](physicsfixedjoint.md) references are not checked or reported, so this property only returns `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsfixedjoint/checksforinternalcollisions)*