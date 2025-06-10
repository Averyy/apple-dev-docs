# SCNPhysicsField

**Framework**: SceneKit  
**Kind**: class

An object that applies forces, such as gravitation, electromagnetism, and turbulence, to physics bodies within a certain area of effect.

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
class SCNPhysicsField
```

#### Overview

You can create many types of field effects, such as gravitation, electromagnetism, and turbulence. To add a field effect to a scene, you create a physics field of the type you want to use and then attach it to the [`physicsField`](scnnode/physicsfield.md) property of a node in the scene.

Physics fields can affect both [`SCNPhysicsBody`](scnphysicsbody.md) objects and the particles spawned by [`SCNParticleSystem`](scnparticlesystem.md) objects.

## Topics

### Creating Physics Fields
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
- [class func electric() -> SCNPhysicsField](scnphysicsfield/electric.md)
  Creates a field that attracts or repels objects based on their electrical charge and on their distance from the field’s center.
- [class func magnetic() -> SCNPhysicsField](scnphysicsfield/magnetic.md)
  Creates a field that attracts or repels objects based on their electrical charge, velocity, and distance from the field’s axis.
### Creating Custom Physics Fields
- [class func customField(evaluationBlock: SCNFieldForceEvaluator) -> SCNPhysicsField](scnphysicsfield/customfield(evaluationblock:).md)
  Creates a field that runs the specified block to determine the force a field applies to each object in its area of effect.
### Specifying a Field’s Area of Effect
- [var halfExtent: SCNVector3](scnphysicsfield/halfextent.md)
  A location marking the end of the field’s area of effect.
- [var scope: SCNPhysicsFieldScope](scnphysicsfield/scope.md)
  The area affected by the field, either inside or outside its region.
- [var usesEllipsoidalExtent: Bool](scnphysicsfield/usesellipsoidalextent.md)
  A Boolean value that determines whether the field’s area of effect is shaped like a box or ellipsoid.
- [var offset: SCNVector3](scnphysicsfield/offset.md)
  The offset of the field’s center within its area of effect.
- [var direction: SCNVector3](scnphysicsfield/direction.md)
  The field’s directional axis.
### Specifying a Field’s Behavior
- [var strength: CGFloat](scnphysicsfield/strength.md)
  A multiplier for the force that the field applies to objects in its area of effect.
- [var falloffExponent: CGFloat](scnphysicsfield/falloffexponent.md)
  An exponent that determines how the field’s strength diminishes with distance.
- [var minimumDistance: CGFloat](scnphysicsfield/minimumdistance.md)
  The minimum value for distance-based effects.
- [var isActive: Bool](scnphysicsfield/isactive.md)
  A Boolean value that determines whether the field’s effect is enabled.
- [var isExclusive: Bool](scnphysicsfield/isexclusive.md)
  A Boolean value that determines whether the field overrides other fields whose areas of effect it overlaps.
### Choosing Physics Bodies to Be Affected by the Field
- [var categoryBitMask: Int](scnphysicsfield/categorybitmask.md)
  A mask that defines which categories this physics field belongs to.
### Constants
- [typealias SCNFieldForceEvaluator](scnfieldforceevaluator.md)
  The signature for a block that SceneKit calls to determine the effect of a custom field on an object.
- [enum SCNPhysicsFieldScope](scnphysicsfieldscope.md)
  Options for defining the region of space affected by a physics field, used by the [`scope`](scnphysicsfield/scope.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class SCNPhysicsWorld](scnphysicsworld.md)
  The global simulation of collisions, gravity, joints, and other physics effects in a scene.
- [class SCNPhysicsBehavior](scnphysicsbehavior.md)
  The abstract superclass for joints, vehicle simulations, and other high-level behaviors that incorporate multiple physics bodies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsfield)*