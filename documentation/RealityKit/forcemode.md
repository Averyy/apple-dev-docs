# ForceMode

**Framework**: RealityKit  
**Kind**: enum

The options that control how physics system applies the forces.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
enum ForceMode
```

#### Overview

`ForceMode` allows you to customize how the physics system applies the force-like vector quantity that you set via [`setForce(_:index:)`](forceeffectparameters/setforce(_:index:).md) and [`setTorque(_:index:)`](forceeffectparameters/settorque(_:index:).md). For example, [`ForceMode.force`](forcemode/force.md) indicates the vector quantity has the unit of force, which is the most common choice. You can use [`ForceMode.acceleration`](forcemode/acceleration.md) to exert a constant acceleration on rigid bodies regardless of their mass.

## Topics

### Operators
- [static func == (ForceMode, ForceMode) -> Bool](forcemode/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Enumeration Cases
- [ForceMode.acceleration](forcemode/acceleration.md)
  A direct adjustment to a body’s linear or angular acceleration, independent of its mass or inertia.
- [ForceMode.force](forcemode/force.md)
  A constant force or torque applied to a body, influencing motion over time.
- [ForceMode.impulse](forcemode/impulse.md)
  A direct adjustment to a body’s linear or angular momentum.
- [ForceMode.velocity](forcemode/velocity.md)
  A direct adjustment to a body’s linear or angular velocity, independent of its mass or inertia.
### Initializers
- [init(from: any Decoder) throws](forcemode/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Properties
- [var hashValue: Int](forcemode/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](forcemode/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](forcemode/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](forcemode/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [protocol ForceEffectProtocol](forceeffectprotocol.md)
  A protocol that defines a custom force effect.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [protocol ForceEffectBase](forceeffectbase.md)
  The base protocol for the wrapping force effect structure containing common parameters for all force-effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forcemode)*