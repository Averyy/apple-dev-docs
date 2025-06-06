# SKEmitterNode

**Framework**: SpriteKit  
**Kind**: class

A source of various particle effects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
@MainActor
class SKEmitterNode
```

## Mentions

- [Using Keyframe Sequence to effect Custom Interpolation](using-keyframe-sequence-to-effect-custom-interpolation.md)
- [Creating Particle Effects](creating-particle-effects.md)
- [Animating Particle Properties Across Disparate Values](animating-particle-properties-across-disparate-values.md)
- [Animate the Warping of a Sprite](animate-the-warping-of-a-sprite.md)

#### Overview

A [`SKEmitterNode`](skemitternode.md) object is a node that automatically creates and renders small particle sprites. Particles are privately owned by [`SpriteKit`](SpriteKit.md)—your game cannot access the generated sprites. For example, you cannot add physics shapes to particles. Emitter nodes are often used to create smoke, fire, sparks, and other particle effects. A  is similar to an [`SKSpriteNode`](skspritenode.md) object; it renders a textured or untextured image that is sized, colorized, and blended into the scene. However, particles differ from sprites in two important ways:

- A particle’s texture is always stretched uniformly.
- Particles are not represented by objects in SpriteKit. This means you cannot perform node-related tasks on particles, nor can you associate physics bodies with particles to make them interact with other content. Although there is no visible class representing particles added by the emitter node, you can think of a particle as having properties like any other object.

Particles are purely visual objects, and their behavior is entirely defined by the emitter node that created them. The emitter node contains many properties to control the behavior of the particles it generates, including:

- The birth rate and lifetime of the particle. You can also specify the order in which the particles are rendered and the maximum number of particles that are created before the emitter turns itself off.
- The starting values of the particle, including its position, orientation, color, and size. You can choose to have these starting values randomized.
- The changes to apply to the particle over its lifetime. Typically, these are specified as a rate of change over time. For example, you might specify that a particle rotates at a particular rate, in radians per second. The emitter automatically updates the particle data for each frame. In most cases, you can also create more sophisticated behaviors using keyframe sequences. For example, you might specify a keyframe sequence for a particle so that it starts out small, scales up to a larger size, then shrinks before dying.

## Topics

### First Steps
- [Creating Particle Effects](creating-particle-effects.md)
  Add particle effects to your app by creating repeatable particles in Xcode’s editor, or in code.
### Choosing Which Node in the Scene Emits Particles
- [Changing the Location of Particles in Your Scene](changing-the-location-of-particles-in-your-scene.md)
  Set a target node from which SpriteKit creates particles.
- [var targetNode: SKNode?](skemitternode/targetnode.md)
  The target node that renders the emitter’s particles.
### Controlling When Particles Are Created
- [func advanceSimulationTime(TimeInterval)](skemitternode/advancesimulationtime(_:).md)
  Advances the emitter particle simulation.
- [func resetSimulation()](skemitternode/resetsimulation.md)
  Removes all existing particles and restarts the simulation.
- [var particleBirthRate: CGFloat](skemitternode/particlebirthrate.md)
  The rate at which new particles are created.
- [var numParticlesToEmit: Int](skemitternode/numparticlestoemit.md)
  The number of particles the emitter should emit before stopping.
### Controlling the Rendering Order of an Emitter’s Particles
- [var particleRenderOrder: SKParticleRenderOrder](skemitternode/particlerenderorder.md)
  The order in which the emitter’s particles are rendered.
- [enum SKParticleRenderOrder](skparticlerenderorder.md)
  The order to use when the emitter’s particles are rendered.
### Controlling Particle Lifetime
- [var particleLifetime: CGFloat](skemitternode/particlelifetime.md)
  The average lifetime of a particle, in seconds.
- [var particleLifetimeRange: CGFloat](skemitternode/particlelifetimerange.md)
  The range of allowed random values for a particle’s lifetime.
### Controlling Particle Position
- [var particlePosition: CGPoint](skemitternode/particleposition.md)
  The average starting position for a particle.
- [var particlePositionRange: CGVector](skemitternode/particlepositionrange.md)
  The range of allowed random values for a particle’s position.
- [var particleZPosition: CGFloat](skemitternode/particlezposition.md)
  The average starting depth of a particle.
- [var particleZPositionRange: CGFloat](skemitternode/particlezpositionrange.md)
  The range of allowed random values for a particle’s depth.
### Controlling Particle Velocity and Acceleration
- [var particleSpeed: CGFloat](skemitternode/particlespeed.md)
  The average initial speed of a new particle, in points per second.
- [var particleSpeedRange: CGFloat](skemitternode/particlespeedrange.md)
  The range of allowed random values for a particle’s initial speed.
- [var emissionAngle: CGFloat](skemitternode/emissionangle.md)
  The average initial direction of a particle, expressed as an angle in radians.
- [var emissionAngleRange: CGFloat](skemitternode/emissionanglerange.md)
  The range of allowed random values for a particle’s initial direction, expressed as an angle in radians.
- [var xAcceleration: CGFloat](skemitternode/xacceleration.md)
  The acceleration to apply to a particle’s horizontal velocity.
- [var yAcceleration: CGFloat](skemitternode/yacceleration.md)
  The acceleration to apply to a particle’s vertical velocity.
- [var particleZPositionSpeed: CGFloat](skemitternode/particlezpositionspeed.md)
  The speed at which the particle’s depth changes.
### Adjusting a Particle’s Rotation
- [var particleRotation: CGFloat](skemitternode/particlerotation.md)
  The average initial rotation of a particle, expressed as an angle in radians.
- [var particleRotationRange: CGFloat](skemitternode/particlerotationrange.md)
  The range of allowed random values for a particle’s initial rotation, expressed as an angle in radians.
- [var particleRotationSpeed: CGFloat](skemitternode/particlerotationspeed.md)
  The speed at which a particle rotates, expressed in radians per second.
### Scaling Particles by a Factor
- [var particleScale: CGFloat](skemitternode/particlescale.md)
  The average initial scale factor of a particle.
- [var particleScaleRange: CGFloat](skemitternode/particlescalerange.md)
  The range of allowed random values for a particle’s initial scale.
- [var particleScaleSpeed: CGFloat](skemitternode/particlescalespeed.md)
  The rate at which a particle’s scale factor changes per second.
- [var particleScaleSequence: SKKeyframeSequence?](skemitternode/particlescalesequence.md)
  The sequence used to specify the scale factor of a particle over its lifetime.
### Changing a Particle’s Source Image and Size
- [var particleTexture: SKTexture?](skemitternode/particletexture.md)
  The texture to use to render a particle.
- [var particleSize: CGSize](skemitternode/particlesize.md)
  The starting size of each particle.
### Configuring Particle Color
- [var particleColorSequence: SKKeyframeSequence?](skemitternode/particlecolorsequence.md)
  The sequence used to specify the color components of a particle over its lifetime.
- [var particleColor: UIColor](skemitternode/particlecolor.md)
  The average initial color for a particle.
- [var particleColorAlphaRange: CGFloat](skemitternode/particlecoloralpharange.md)
  The range of allowed random values for the alpha component of a particle’s initial color.
- [var particleColorBlueRange: CGFloat](skemitternode/particlecolorbluerange.md)
  The range of allowed random values for the blue component of a particle’s initial color.
- [var particleColorGreenRange: CGFloat](skemitternode/particlecolorgreenrange.md)
  The range of allowed random values for the green component of a particle’s initial color.
- [var particleColorRedRange: CGFloat](skemitternode/particlecolorredrange.md)
  The range of allowed random values for the red component of a particle’s initial color.
- [var particleColorAlphaSpeed: CGFloat](skemitternode/particlecoloralphaspeed.md)
  The rate at which the alpha component of a particle’s color changes per second.
- [var particleColorBlueSpeed: CGFloat](skemitternode/particlecolorbluespeed.md)
  The rate at which the blue component of a particle’s color changes per second.
- [var particleColorGreenSpeed: CGFloat](skemitternode/particlecolorgreenspeed.md)
  The rate at which the green component of a particle’s color changes per second.
- [var particleColorRedSpeed: CGFloat](skemitternode/particlecolorredspeed.md)
  The rate at which the red component of a particle’s color changes per second.
### Controlling How the Texture is Blended with Particle Color
- [var particleColorBlendFactorSequence: SKKeyframeSequence?](skemitternode/particlecolorblendfactorsequence.md)
  The sequence used to specify the color blend factor of a particle over its lifetime.
- [var particleColorBlendFactor: CGFloat](skemitternode/particlecolorblendfactor.md)
  The average starting value for the color blend factor.
- [var particleColorBlendFactorRange: CGFloat](skemitternode/particlecolorblendfactorrange.md)
  The range of allowed random values for a particle’s starting color blend factor.
- [var particleColorBlendFactorSpeed: CGFloat](skemitternode/particlecolorblendfactorspeed.md)
  The rate at which the color blend factor changes per second.
### Blending Particles with the Framebuffer
- [var particleBlendMode: SKBlendMode](skemitternode/particleblendmode.md)
  The blending mode used to blend particles into the framebuffer.
- [var particleAlphaSequence: SKKeyframeSequence?](skemitternode/particlealphasequence.md)
  The sequence used to specify the alpha value of a particle over its lifetime.
- [var particleAlpha: CGFloat](skemitternode/particlealpha.md)
  The average starting alpha value for a particle.
- [var particleAlphaRange: CGFloat](skemitternode/particlealpharange.md)
  The range of allowed random values for a particle’s starting alpha value.
- [var particleAlphaSpeed: CGFloat](skemitternode/particlealphaspeed.md)
  The rate at which the alpha value of a particle changes per second.
### Animating Particles
- [Animating Particle Properties Across Disparate Values](animating-particle-properties-across-disparate-values.md)
  Supply keyframe sequences to do linear or nonlinear particle animations.
- [var particleAction: SKAction?](skemitternode/particleaction.md)
  An action executed by new particles.
### Applying Physics Fields to the Particles
- [var fieldBitMask: UInt32](skemitternode/fieldbitmask.md)
  A mask that defines which categories of physics fields can exert forces on the particles.
### Taking Full Control of Particle Drawing with a Shader
- [Getting Started with Particle Shaders](getting-started-with-particle-shaders.md)
  Provide custom shader code to alter a particle’s look.
- [var shader: SKShader?](skemitternode/shader.md)
  A custom shader used to determine how particles are rendered.
- [var attributeValues: [String : SKAttributeValue]](skemitternode/attributevalues.md)
  The values of each attribute associated with the node’s attached shader.
- [func setValue(SKAttributeValue, forAttribute: String)](skemitternode/setvalue(_:forattribute:).md)
  Sets an attribute value for an attached shader.
- [func value(forAttributeNamed: String) -> SKAttributeValue?](skemitternode/value(forattributenamed:).md)
  Gets the value of a shader attribute.
### Maximizing Particle Run-Time Performance
- [Optimizing Emitter Node Performance](optimizing-emitter-node-performance.md)
  Use proven methods to rapidly create and play back performant particle effects.

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

- [Maximizing Node Drawing Performance](maximizing-node-drawing-performance.md)
  Structure your nodes for maximum performance.
- [class SKSpriteNode](skspritenode.md)
  An image or solid color.
- [class SKShapeNode](skshapenode.md)
  A mathematical shape that can be stroked or filled.
- [class SKLabelNode](sklabelnode.md)
  A graphical element that draws text.
- [class SKVideoNode](skvideonode.md)
  A graphical element that plays video content.
- [class SKTileMapNode](sktilemapnode.md)
  A two-dimensional array of images.
- [class SK3DNode](sk3dnode.md)
  3D SceneKit content drawn as a flattened sprite.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skemitternode)*