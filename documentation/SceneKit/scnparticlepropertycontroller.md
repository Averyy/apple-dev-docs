# SCNParticlePropertyController

**Framework**: SceneKit  
**Kind**: class

An animation for a single property of the individual particles rendered by a particle system.

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
class SCNParticlePropertyController
```

#### Overview

Use particle property controllers to change the properties of individual particles in an [`SCNParticleSystem`](scnparticlesystem.md) object over time, with Core Animation semantics. For example, by associating a keyframe animation with a particle system’s [`color`](scnparticlesystem/particleproperty/color.md) property, you can create a flame effect with particles that change from blue to white to orange as they rise.

A particle property controller animates a property of individual particles rendered by the particle system. By comparison, implicitly or explicitly animating properties of a [`SCNParticleSystem`](scnparticlesystem.md) object affects the system as a whole. Consider the keyframe animation of colors described above—if you apply this animation directly to a particle system instead of using a property controller, all particles rendered by the system change color together instead of each one changing color as it rises.

Core Animation animations in SceneKit typically animate a change to a property as a function of time. By default, property controllers animate a particle property this way. However, by changing the [`inputMode`](scnparticlepropertycontroller/inputmode.md) property you can also create animations that animate a particle property as a function of distance from a specified node or of the value of another particle property. For example, you can use this option to make particles change color as they speed up and slow down.

For more details about particle systems and particle properties, see [`SCNParticleSystem`](scnparticlesystem.md).

## Topics

### Creating a Property Controller
- [convenience init(animation: CAAnimation)](scnparticlepropertycontroller/init(animation:).md)
  Creates a particle property controller with the specified Core Animation animation.
### Managing the Controller’s Animation
- [var animation: CAAnimation](scnparticlepropertycontroller/animation.md)
  The Core Animation object defining the behavior of the property animation.
- [var inputMode: SCNParticleInputMode](scnparticlepropertycontroller/inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputBias: CGFloat](scnparticlepropertycontroller/inputbias.md)
  An offset to add to the input value of the controller’s animation.
- [var inputScale: CGFloat](scnparticlepropertycontroller/inputscale.md)
  A factor for multiplying the input value of the controller’s animation.
- [var inputOrigin: SCNNode?](scnparticlepropertycontroller/inputorigin.md)
  A node whose distance to each particle provides input values for the controller’s animation.
- [var inputProperty: SCNParticleSystem.ParticleProperty?](scnparticlepropertycontroller/inputproperty.md)
  A particle property that provides input values for this property controller’s animation.
### Constants
- [enum SCNParticleInputMode](scnparticleinputmode.md)
  Options for the input value of the property controller’s animation, used by the [`inputMode`](scnparticlepropertycontroller/inputmode.md) property.

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

- [class SCNParticleSystem](scnparticlesystem.md)
  An object that animates and renders a system of small image sprites using a high-level simulation whose general behavior you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller)*