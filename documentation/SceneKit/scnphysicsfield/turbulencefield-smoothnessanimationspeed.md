# turbulenceField(smoothness:animationSpeed:)

**Framework**: SceneKit  
**Kind**: method

Creates a field that applies random forces to objects in its area of effect, with magnitudes proportional to those objects’ velocities.

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
class func turbulenceField(smoothness: CGFloat, animationSpeed speed: CGFloat) -> SCNPhysicsField
```

#### Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](scnnode/physicsfield.md) property of an [`SCNNode`](scnnode.md) object.

#### Discussion

Like a noise field, a turbulence field applies forces in random directions to the objects that it affects. Unlike a noise field, a turbulence field applies a force whose magnitude is proportional to the speed of each affected object. For example, an object passing through a noise field shakes as it travels through the field, but an object passing through a turbulence field shakes more violently the faster it travels. The field’s [`strength`](scnphysicsfield/strength.md) property scales the magnitude of the turbulence effect.

The default [`falloffExponent`](scnphysicsfield/falloffexponent.md) value for a turbulence field is `0.0`, indicating that the field’s effect is constant throughout its area of effect.

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
- [class func noiseField(smoothness: CGFloat, animationSpeed: CGFloat) -> SCNPhysicsField](scnphysicsfield/noisefield(smoothness:animationspeed:).md)
  Creates a field that applies random forces to objects in its area of effect.
- [class func spring() -> SCNPhysicsField](scnphysicsfield/spring.md)
  Creates a field that pulls objects toward its center with a spring-like force.
- [class func electric() -> SCNPhysicsField](scnphysicsfield/electric.md)
  Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.
- [class func magnetic() -> SCNPhysicsField](scnphysicsfield/magnetic.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/turbulencefield(smoothness:animationspeed:))*