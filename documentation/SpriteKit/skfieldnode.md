# SKFieldNode

**Framework**: SpriteKit  
**Kind**: class

A node that applies physics effects to nearby nodes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class SKFieldNode
```

## Mentions

- [Getting Started with Physics](getting-started-with-physics.md)
- [Adding Physics Fields to a Scene](adding-physics-fields-to-a-scene.md)

#### Overview

There are many different kinds of field nodes that can be created, each with different effects. The [`SKFieldNode`](skfieldnode.md) section lists the field types you can create using SpriteKit, including a type that allows you to apply custom forces to physics bodies. Instantiate the appropriate kind of field node and then add it to the scene’s node tree.

When the scene simulates physics effects, a field node applies its effect to a physics body so long as the following are true:

- The field node is in the scene’s node tree.
- The field node’s [`isEnabled`](skfieldnode/isenabled.md) property is [`true`](https://developer.apple.com/documentation/swift/true).
- The physics body is attached to a node that is in the scene’s node tree.
- The physics body is located inside the field node’s region (see [`region`](skfieldnode/region.md)).
- The physics body is not located inside the region of another field node whose [`isExclusive`](skfieldnode/isexclusive.md) property is set to [`true`](https://developer.apple.com/documentation/swift/true).
- A logical AND operation between the field node’s [`categoryBitMask`](skfieldnode/categorybitmask.md) property and the physics body’s [`fieldBitMask`](skphysicsbody/fieldbitmask.md) property results in a nonzero value.

> 💡 **Tip**:  While it is useful to know that SpriteKit measures items in the International System of Units, the precise numbers are not that important. It doesn’t matter much whether your rocket ship weights 1 kilogram or 1,000,000 kilograms, as long as the mass is consistent with other physics values used in the game. Often, proportions are more important than the actual values being used.

 While it is useful to know that SpriteKit measures items in the International System of Units, the precise numbers are not that important. It doesn’t matter much whether your rocket ship weights 1 kilogram or 1,000,000 kilograms, as long as the mass is consistent with other physics values used in the game. Often, proportions are more important than the actual values being used.

## Topics

### Getting Started with Field Nodes
- [Adding Physics Fields to a Scene](adding-physics-fields-to-a-scene.md)
  Create effects that interact with your scene’s physics bodies, such as magnetism, repulsion, friction, or a vortex.
### Creating Field Nodes
- [class func dragField() -> SKFieldNode](skfieldnode/dragfield.md)
  Creates a field node that applies a force that resists the motion of physics bodies.
- [class func electricField() -> SKFieldNode](skfieldnode/electricfield.md)
  Creates a field node that applies an electrical force proportional to the electrical charge of physics bodies.
- [class func linearGravityField(withVector: vector_float3) -> SKFieldNode](skfieldnode/lineargravityfield(withvector:).md)
  Creates a field node that accelerates physics bodies in a specific direction.
- [class func magneticField() -> SKFieldNode](skfieldnode/magneticfield.md)
  Creates a field node that applies a magnetic force based on the velocity and electrical charge of the physics bodies.
- [class func noiseField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode](skfieldnode/noisefield(withsmoothness:animationspeed:).md)
  Creates a field node that applies a randomized acceleration to physics bodies.
- [class func radialGravityField() -> SKFieldNode](skfieldnode/radialgravityfield.md)
  Creates a field node that accelerates physics bodies toward the field node.
- [class func springField() -> SKFieldNode](skfieldnode/springfield.md)
  Creates a field node that applies a spring-like force that pulls physics bodies toward the field node.
- [class func turbulenceField(withSmoothness: CGFloat, animationSpeed: CGFloat) -> SKFieldNode](skfieldnode/turbulencefield(withsmoothness:animationspeed:).md)
  Creates a field node that applies a randomized acceleration to physics bodies.
- [class func velocityField(with: SKTexture) -> SKFieldNode](skfieldnode/velocityfield(with:).md)
  Creates a field node that sets the velocity of physics bodies that enter the node’s area based on the pixel values of a texture.
- [class func velocityField(withVector: vector_float3) -> SKFieldNode](skfieldnode/velocityfield(withvector:).md)
  Creates a field node that gives physics bodies a constant velocity.
- [class func vortexField() -> SKFieldNode](skfieldnode/vortexfield.md)
  Creates a field node that applies a perpendicular force to physics bodies.
- [class func customField(evaluationBlock: SKFieldForceEvaluator) -> SKFieldNode](skfieldnode/customfield(evaluationblock:).md)
  Creates a field node that calculates and applies a custom force to the physics body.
- [typealias SKFieldForceEvaluator](skfieldforceevaluator.md)
  The definition for a custom block that processes a single physics body’s interaction with the field.
### Determining Which Physics Bodies Are Affected by the Field
- [var isEnabled: Bool](skfieldnode/isenabled.md)
  A Boolean value that indicates whether the field is active.
- [var isExclusive: Bool](skfieldnode/isexclusive.md)
  A Boolean value that indicates whether the field node should override all other field nodes that might otherwise affect physics bodies.
- [var region: SKRegion?](skfieldnode/region.md)
  The area (relative to the node’s origin) that the field affects.
- [var minimumRadius: Float](skfieldnode/minimumradius.md)
  The minimum value for distance-based effects.
- [var categoryBitMask: UInt32](skfieldnode/categorybitmask.md)
  A mask that defines which categories this field belongs to.
### Configuring the Strength of the Field
- [var strength: Float](skfieldnode/strength.md)
  The strength of the field.
- [var falloff: Float](skfieldnode/falloff.md)
  The exponent that defines the rate of decay for the strength of the field as the distance increases between the node and the physics body being affected.
### Configuring Other Field Properties
- [var animationSpeed: Float](skfieldnode/animationspeed.md)
  The rate at which a noise or turbulence field node changes.
- [var smoothness: Float](skfieldnode/smoothness.md)
  The smoothness of the noise used to generate the forces.
- [var direction: vector_float3](skfieldnode/direction.md)
  The direction of a velocity field node.
- [var texture: SKTexture?](skfieldnode/texture.md)
  A normal texture that specifies the velocities at different points in a velocity field node.

## Relationships

### Inherits From
- [SKNode](sknode.md)
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
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Getting Started with Physics](getting-started-with-physics.md)
  Simulate gravity, acceleration, collision detection, or joints.
- [class SKPhysicsWorld](skphysicsworld.md)
  The driver of the physics engine in a scene; it exposes the ability for you to configure and query the physics system.
- [class SKPhysicsBody](skphysicsbody.md)
  An object that adds physics simulation to a node.
- [class SKPhysicsContact](skphysicscontact.md)
  A description of the contact between two physics bodies.
- [protocol SKPhysicsContactDelegate](skphysicscontactdelegate.md)
  Methods your app can implement to respond when physics bodies come into contact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skfieldnode)*