# position

**Framework**: RealityKit  
**Kind**: property

A position representing the estimated point of contact.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
let position: SIMD3<Float>
```

#### Discussion

The point is an average calculated from the intersecting shapes. It’s specified in the coordinate space of the physics simulation, which means it’s relative to [`nearestSimulationEntity(for:)`](physicssimulationcomponent/nearestsimulationentity(for:).md). If the physics origin is `nil`, the point is given in world space.

## See Also

- [let impulse: Float](collisionevents/began/impulse.md)
  The total impulse in this collision pair obtained by adding up all the individual impulses applied at each contact point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionevents/began/position)*