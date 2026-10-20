# PhysicsJoints

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A collection of physics joints.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct PhysicsJoints
```

## Topics

### Initializers
- [init(any Sequence<any PhysicsJoint>)](./physicsjoints/init%28_%29.md)

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/bidirectionalcollection.md)
- [Collection](../Swift/collection.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [MutableCollection](../Swift/mutablecollection.md)
- [RangeReplaceableCollection](../Swift/rangereplaceablecollection.md)
- [Sequence](../Swift/sequence.md)

## See Also

### Built-in joint types
- [struct PhysicsRevoluteJoint](./physicsrevolutejoint.md)
  A joint that allows one degree of rotational freedom between two entity pins, similar to a door swinging on its hinges.
- [struct PhysicsPrismaticJoint](./physicsprismaticjoint.md)
  A joint that allows movement along a straight line, similar to a sliding drawer.
- [struct PhysicsSphericalJoint](./physicssphericaljoint.md)
  A spherical joint that allows free rotational movement between two entities’ pins.
- [struct PhysicsCustomJoint](./physicscustomjoint.md)
  A joint with six degrees of freedom that can be individually specified.
- [struct PhysicsDistanceJoint](./physicsdistancejoint.md)
  A joint that maintains a minimum and maximum distance between two entity pins.
- [struct PhysicsFixedJoint](./physicsfixedjoint.md)
  A joint that rigidly connects two entity pins, with zero degrees of freedom.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoints)*