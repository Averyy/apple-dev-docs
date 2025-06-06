# init(pin0:pin1:linearLimit:checksForInternalCollisions:)

**Framework**: RealityKit  
**Kind**: init

Creates a new prismatic joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(pin0: GeometricPin, pin1: GeometricPin, linearLimit: ClosedRange<Float>? = nil, checksForInternalCollisions: Bool = false)
```

## Parameters

- `pin0`: The local position and orientation on the first entity.
- `pin1`: The local position and orientation on the second entity.
- `linearLimit`: A limit of the the translation of   from    in the direction of the x-axis of  .
- `checksForInternalCollisions`: A Boolean that indicates whether the joint   checks for collisions between the two   instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsprismaticjoint/init(pin0:pin1:linearlimit:checksforinternalcollisions:))*