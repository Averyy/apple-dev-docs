# PhysicsMaterialResource

**Framework**: RealityKit  
**Kind**: class

Material properties, like friction, of a physically simulated object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency class PhysicsMaterialResource
```

## Topics

### Using the default material resource
- [static let `default`: PhysicsMaterialResource](physicsmaterialresource/default.md)
  A default material resource.
### Creating a custom material resource
- [static func generate(friction: Float, restitution: Float) -> PhysicsMaterialResource](physicsmaterialresource/generate(friction:restitution:).md)
  Generates a new material with the given characteristics.
- [static func generate(staticFriction: Float, dynamicFriction: Float, restitution: Float) -> PhysicsMaterialResource](physicsmaterialresource/generate(staticfriction:dynamicfriction:restitution:).md)
  Creates a new material with the specified static friction, dynamic friction, and restitution.

## Relationships

### Conforms To
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct PhysicsBodyComponent](physicsbodycomponent.md)
  A component that defines an entity’s behavior in physics body simulations.
- [enum PhysicsBodyMode](physicsbodymode.md)
  The ways that a physics body can move in response to physical forces.
- [struct PhysicsMassProperties](physicsmassproperties.md)
  Mass properties of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsmaterialresource)*