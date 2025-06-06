# update(parameters:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Defines how the custom force effect computes forces at each physics simulation step.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func update(parameters: inout ForceEffectParameters)
```

## Parameters

- `parameters`: On input, the rigid body parameters declared in  .   On output, the computed forces and torques.

## See Also

- [static func register(((inout ForceEffectEvent<Self>) -> Void)?)](forceeffectprotocol/register(_:)-1zt9t.md)
  Registers the custom effect.
- [struct PhysicsBodyParameterTypes](physicsbodyparametertypes.md)
  Defines which rigid body inputs are required by a force effect’s update handler.
- [struct ForceEffectParameters](forceeffectparameters.md)
  The force effect input data to the effect’s update handler or closure.
- [struct ForceEffectEvent](forceeffectevent.md)
  A struct that defines the arguments to the custom force effect update closure.
- [struct UnsafeForceEffectBuffer](unsafeforceeffectbuffer.md)
  Provides access to physics body parameters from the effect’s update function or event handler.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectprotocol/update(parameters:))*