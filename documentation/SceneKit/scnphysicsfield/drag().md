# drag()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Type Method

Creates a field that slows any object in its area of effect with a force proportional to the object’s velocity.

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
class func drag() -> SCNPhysicsField
```

```objc
+ (SCNPhysicsField *) dragField;
```

## Return Value

A physics field object. To use the field in a scene, attach it to the [`physicsField`](../scnnode/physicsfield.md) property of an [`SCNNode`](../scnnode.md) object.

## Discussion

Like the [`damping`](../scnphysicsbody/damping.md) and [`angularDamping`](../scnphysicsbody/angulardamping.md) properties of a physics body, drag fields can simulate effects such as fluid friction or air resistance. Unlike those properties, drag fields can simulate different intensities of fluid friction in different areas of your scene. For example, you can use a drag field to represent underwater areas.

The default [`falloffExponent`](./falloffexponent.md) value for a drag field is `0.0`, indicating that the field’s effect is constant throughout its area of effect.

## See Also

### Creating Physics Fields
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
- [class func magnetic() -> SCNPhysicsField](./magnetic%28%29.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield/drag())*