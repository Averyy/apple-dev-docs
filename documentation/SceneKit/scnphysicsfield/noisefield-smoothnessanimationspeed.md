# noiseField(smoothness:animationSpeed:)

**Framework**: SceneKit  
**Kind**: method

Creates a field that applies random forces to objects in its area of effect.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class func noiseField(smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](scnnode/physicsfield.md) property of an [`SCNNode`](scnnode.md) object.

#### Discussion

Use this field type to simulate effects involving random motion, such as fireflies or gently falling snow.

In calculating the direction and strength of the field’s effect on an object, SceneKit uses a Perlin simplex noise function. This function produces a velocity field that varies over time.

The default [`falloffExponent`](scnphysicsfield/falloffexponent.md) value for a noise field is `0.0`, indicating that the field’s effect is constant throughout its area of effect. This field type ignores the field’s [`direction`](scnphysicsfield/direction.md) property.

## Parameters

- `smoothness`: The amount of randomness in the field. A value of   specifies maximum noise, and a value of   specifies no noise at all.
- `speed`: The field’s variation over time. Specify   for a static field.

## See Also

- [class func drag() -> SCNPhysicsField](scnphysicsfield/drag.md)
  Creates a field that slows any object in its area of effect with a force proportional to the object’s velocity.
- [class func vortex() -> SCNPhysicsField](scnphysicsfield/vortex.md)
  Creates a field whose forces circulate around an axis.
- [class func radialGravity() -> SCNPhysicsField](scnphysicsfield/radialgravity.md)
  Creates a field that accelerates objects toward its center.
- [class func linearGravity() -> SCNPhysicsField](scnphysicsfield/lineargravity.md)
  Creates a field that accelerates objects in a specific direction.
- [class func turbulenceField(smoothness: CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField](scnphysicsfield/turbulencefield(smoothness:animationspeed:).md)
  Creates a field that applies random forces to objects in its area of effect, with magnitudes proportional to those objects’ velocities.
- [class func spring() -> SCNPhysicsField](scnphysicsfield/spring.md)
  Creates a field that pulls objects toward its center with a spring-like force.
- [class func electric() -> SCNPhysicsField](scnphysicsfield/electric.md)
  Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.
- [class func magnetic() -> SCNPhysicsField](scnphysicsfield/magnetic.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/noisefield(smoothness:animationspeed:))*