# spring()

**Framework**: SceneKit  
**Kind**: method

Creates a field that pulls objects toward its center with a spring-like force.

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
class func spring() -> SCNPhysicsField
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](scnnode/physicsfield.md) property of an [`SCNNode`](scnnode.md) object.

#### Discussion

The force a spring field applies to objects in its area of effect is linearly proportional to the distance from the object to the center of the field. (That is, the field behaves according to Hooke’s Law of real-world spring forces.) An object placed at the center of the field and moved away will oscillate around the center, with a period of oscillation that is proportional to the object’s mass. The field’s [`strength`](scnphysicsfield/strength.md) property scales the magnitude of the spring effect—a larger strength simulates a stiffer spring.

The default [`falloffExponent`](scnphysicsfield/falloffexponent.md) value for a spring field is `1.0`, indicating that the field’s effect diminishes linearly with distance from its center.

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
- [class func electric() -> SCNPhysicsField](scnphysicsfield/electric.md)
  Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.
- [class func magnetic() -> SCNPhysicsField](scnphysicsfield/magnetic.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/spring())*