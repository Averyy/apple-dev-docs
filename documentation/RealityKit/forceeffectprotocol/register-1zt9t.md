# register(_:)

**Framework**: RealityKit  
**Kind**: method

Registers the custom effect.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency static func register(_ updateHandler: (@MainActor (inout ForceEffectEvent<Self>) -> Void)? = nil)
```

#### Discussion

If a handler is specified, the physics system calls the handler and ignores the update function.

## Parameters

- `updateHandler`: A closure that computes custom forces for rigid bodies.

## See Also

- [func update(parameters: inout ForceEffectParameters)](forceeffectprotocol/update(parameters:).md)
  Defines how the custom force effect computes forces at each physics simulation step.
- [struct PhysicsBodyParameterTypes](physicsbodyparametertypes.md)
  Defines which rigid body inputs are required by a force effect’s update handler.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [struct ForceEffectEvent](forceeffectevent.md)
  A struct that defines the arguments to the custom force effect update closure.
- [struct UnsafeForceEffectBuffer](unsafeforceeffectbuffer.md)
  Provides access to physics body parameters from the effect’s update function or event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectprotocol/register(_:)-1zt9t)*