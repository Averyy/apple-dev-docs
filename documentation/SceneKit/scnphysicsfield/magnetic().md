# magnetic()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
class func magnetic() -> SCNPhysicsField
```

```objc
+ (SCNPhysicsField *) magneticField;
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](../scnnode/physicsfield.md) property of an [`SCNNode`](../scnnode.md) object.

#### Discussion

Use this field type to make objects behave differently from one another when they enter a region, or to make an object’s behavior different from its mass based behavior. A magnetic field behaves according to the second part of the Lorentz force equation modeling real-world electromagnetic forces—the field applies a force determined by the cross product of an object’s velocity vector and the magnetic field vector at the object’s location, with magnitude proportional to the object’s electric charge.

By default, physics bodies and particle systems have no electric charge, so they are unaffected by electric and magnetic fields. Use the [`charge`](../scnphysicsbody/charge.md) property of a physics body or the [`particleCharge`](../scnparticlesystem/particlecharge.md) property of a particle system to add charge-based behavior.

When the field’s [`strength`](./strength.md) value is positive (the default), the magnetic field vectors circulate counterclockwise relative to the field’s [`direction`](./direction.md) vector. (That is, the magnetic field models a real-world magnetic field created by current in a wire oriented in the field’s direction.) To make field vectors circulate clockwise, set the field’s [`strength`](./strength.md) property to a negative value.

> **Note**:  This [`SCNPhysicsField`](../scnphysicsfield.md) option models the real-world physics effect of magnetic fields on moving, electrically charged bodies, not the behavior of permanent magnets or electromagnets. To make objects in your scene simply attract or repel one another, use a different field type. For example, a field created by the [`radialGravity()`](./radialgravity%28%29.md) method attracts or repels all dynamic bodies near it according to its [`strength`](./strength.md) property, and a field created by the [`electric()`](./electric%28%29.md) method selectively attracts or repels bodies according to their electric charge.

The default [`falloffExponent`](./falloffexponent.md) value for a magnetic field is `2.0`, indicating that the field’s effect diminishes with the square of distance from its center.

## See Also

### Creating Physics Fields
- [class func drag() -> SCNPhysicsField](./drag%28%29.md)
  Creates a field that slows any object in its area of effect with a force proportional to the object’s velocity.
- [class func vortex() -> SCNPhysicsField](./vortex%28%29.md)
  Creates a field whose forces circulate around an axis.
- [class func radialGravity() -> SCNPhysicsField](./radialgravity%28%29.md)
  Creates a field that accelerates objects toward its center.
- [class func linearGravity() -> SCNPhysicsField](./lineargravity%28%29.md)
  Creates a field that accelerates objects in a specific direction.
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField](./noisefield%28smoothness,animationspeed%29.md)
  Creates a field that applies random forces to objects in its area of effect.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField](./turbulencefield%28smoothness,animationspeed%29.md)
  Creates a field that applies random forces to objects in its area of effect, with magnitudes proportional to those objects’ velocities.
- [class func spring() -> SCNPhysicsField](./spring%28%29.md)
  Creates a field that pulls objects toward its center with a spring-like force.
- [class func electric() -> SCNPhysicsField](./electric%28%29.md)
  Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/magnetic())*