# vortex()

**Framework**: SceneKit  
**Kind**: method

Creates a field whose forces circulate around an axis.

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
class func vortex() -> SCNPhysicsField
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](scnnode/physicsfield.md) property of an [`SCNNode`](scnnode.md) object.

#### Discussion

The force on an object in a vortex field is tangential to the line from the object’s position to the field’s axis and proportional to the object’s mass. (The field’s axis is a line that is parallel to its [`direction`](scnphysicsfield/direction.md) vector and that passes through its center. For details, see the [`offset`](scnphysicsfield/offset.md) property.) For example, when a vortex field’s area of effect contains many objects, the resulting scene resembles a tornado: The objects simultaneously revolve around and fly away from the field’s center.

By default, a vortex circulates counterclockwise relative to its [`direction`](scnphysicsfield/direction.md) vector. To make it circulate clockwise, set the field’s [`strength`](scnphysicsfield/strength.md) property to a negative value.

The default [`falloffExponent`](scnphysicsfield/falloffexponent.md) value for a vortex field is `0.0`, indicating that the field’s effect is constant throughout its area of effect.

## See Also

- [class func drag() -> SCNPhysicsField](scnphysicsfield/drag.md)
  Creates a field that slows any object in its area of effect with a force proportional to the object’s velocity.
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
- [class func electric() -> SCNPhysicsField](scnphysicsfield/electric.md)
  Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.
- [class func magnetic() -> SCNPhysicsField](scnphysicsfield/magnetic.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/vortex())*