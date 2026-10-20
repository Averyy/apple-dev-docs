# vortex()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a field whose forces circulate around an axis.

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
class func vortex() -> SCNPhysicsField
```

```objc
+ (SCNPhysicsField *) vortexField;
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](../scnnode/physicsfield.md) property of an [`SCNNode`](../scnnode.md) object.

#### Discussion

The force on an object in a vortex field is tangential to the line from the object’s position to the field’s axis and proportional to the object’s mass. (The field’s axis is a line that is parallel to its [`direction`](./direction.md) vector and that passes through its center. For details, see the [`offset`](./offset.md) property.) For example, when a vortex field’s area of effect contains many objects, the resulting scene resembles a tornado: The objects simultaneously revolve around and fly away from the field’s center.

By default, a vortex circulates counterclockwise relative to its [`direction`](./direction.md) vector. To make it circulate clockwise, set the field’s [`strength`](./strength.md) property to a negative value.

The default [`falloffExponent`](./falloffexponent.md) value for a vortex field is `0.0`, indicating that the field’s effect is constant throughout its area of effect.

## See Also

### Creating Physics Fields
- [class func drag() -> SCNPhysicsField](./drag%28%29.md)
  Creates a field that slows any object in its area of effect with a force proportional to the object’s velocity.
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
- [class func magnetic() -> SCNPhysicsField](./magnetic%28%29.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/vortex())*