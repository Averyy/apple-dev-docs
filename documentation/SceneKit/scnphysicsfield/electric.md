# electric()

**Framework**: SceneKit  
**Kind**: method

Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func electric() -> SCNPhysicsField
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](scnnode/physicsfield.md) property of an [`SCNNode`](scnnode.md) object.

#### Discussion

Use this field type to make objects behave differently from one another when they enter a region, or to make an object’s behavior different from its mass-based behavior. An electric field behaves according to the first part of the Lorentz force equation modeling real-world electromagnetic forces—the field applies a force whose magnitude is proportional to electric charge and distance.

By default, physics bodies and particle systems have no electric charge, so they are unaffected by electric and magnetic fields. Use the [`charge`](scnphysicsbody/charge.md) property of a physics body or the [`particleCharge`](scnparticlesystem/particlecharge.md) property of a particle system to add charge-based behavior.

When the field’s [`strength`](scnphysicsfield/strength.md) value is positive (the default), it attracts bodies whose charge is negative and repels bodies whose charge is positive. To reverse this behavior, set the field’s [`strength`](scnphysicsfield/strength.md) property to a negative value.

The default [`falloffExponent`](scnphysicsfield/falloffexponent.md) value for an electric field is `2.0`, indicating that the field’s effect diminishes with the square of its distance from its center.

## See Also

- [class func drag() -> SCNPhysicsField](scnphysicsfield/drag.md)
  Creates a field that slows any object in its area of effect with a force proportional to the object’s velocity.
- [class func vortex() -> SCNPhysicsField](scnphysicsfield/vortex.md)
  Creates a field whose forces circulate around an axis.
- [class func radialGravity() -> SCNPhysicsField](scnphysicsfield/radialgravity.md)
  Creates a field that accelerates objects toward its center.
- [class func linearGravity() -> SCNPhysicsField](scnphysicsfield/lineargravity.md)
  Creates a field that accelerates objects in a specific direction.
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField](scnphysicsfield/noisefield(smoothness:animationspeed:).md)
  Creates a field that applies random forces to objects in its area of effect.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField](scnphysicsfield/turbulencefield(smoothness:animationspeed:).md)
  Creates a field that applies random forces to objects in its area of effect, with magnitudes proportional to those objects’ velocities.
- [class func spring() -> SCNPhysicsField](scnphysicsfield/spring.md)
  Creates a field that pulls objects toward its center with a spring-like force.
- [class func magnetic() -> SCNPhysicsField](scnphysicsfield/magnetic.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/electric())*