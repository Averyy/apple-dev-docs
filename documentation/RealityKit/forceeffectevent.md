# ForceEffectEvent

**Framework**: RealityKit  
**Kind**: struct

A struct that defines the arguments to the custom force effect update closure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
struct ForceEffectEvent<ForceEffectType> where ForceEffectType : ForceEffectProtocol
```

#### Overview

If you register your custom force effect using a closure, you can access the force effect’s property and [`ForceEffectParameters`](forceeffectparameters.md) from this struct.

## Topics

### Instance Properties
- [var effect: ForceEffectType](forceeffectevent/effect.md)
  The force effect to update.
- [var parameters: ForceEffectParameters](forceeffectevent/parameters.md)
  Physics body parameters.

## See Also

- [func update(parameters: inout ForceEffectParameters)](forceeffectprotocol/update(parameters:).md)
  Defines how the custom force effect computes forces at each physics simulation step.
- [static func register(((inout ForceEffectEvent<Self>) -> Void)?)](forceeffectprotocol/register(_:)-1zt9t.md)
  Registers the custom effect.
- [struct PhysicsBodyParameterTypes](physicsbodyparametertypes.md)
  Defines which rigid body inputs are required by a force effect’s update handler.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [struct UnsafeForceEffectBuffer](unsafeforceeffectbuffer.md)
  Provides access to physics body parameters from the effect’s update function or event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectevent)*