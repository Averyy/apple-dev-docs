# ForceEffectParameters

**Framework**: RealityKit  
**Kind**: struct

The force effect input data to the effect’s update handler or closure.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct ForceEffectParameters
```

## Topics

### Instance Properties
- [let angularVelocities: UnsafeForceEffectBuffer<SIMD3<Float>>?](forceeffectparameters/angularvelocities.md)
  The angular velocities of all rigid bodies under the influence of the effect, or nil if angular velocity information was not requested.
- [let distances: UnsafeForceEffectBuffer<Float>?](forceeffectparameters/distances.md)
  The distance from the effect to each rigid body’s center of mass, or nil if distance information was not requested.
- [let elapsedTime: TimeInterval](forceeffectparameters/elapsedtime.md)
  The amount of time that has elapsed since the force effect was started.
- [let entity: Entity](forceeffectparameters/entity.md)
  The entity containing the force effect.
- [let fixedDeltaTime: TimeInterval](forceeffectparameters/fixeddeltatime.md)
  The fixed delta time between simulation steps.
- [let inertiaTensors: UnsafeForceEffectBuffer<simd_float3x3>?](forceeffectparameters/inertiatensors.md)
  The inertia tensor based on the current rigid body’s orientation, or nil if inertia tensor information was not requested.
- [let masses: UnsafeForceEffectBuffer<Float>?](forceeffectparameters/masses.md)
  The mass of each rigid body, or nil if mass information was not requested or force mode does not require it.
- [let orientations: UnsafeForceEffectBuffer<simd_quatf>?](forceeffectparameters/orientations.md)
  The orientations of all rigid bodies under the influence of the effect, or nil if rotational information was not requested.
- [let physicsBodyCount: Int](forceeffectparameters/physicsbodycount.md)
  The number of physics bodies to be updated.
- [let positions: UnsafeForceEffectBuffer<SIMD3<Float>>?](forceeffectparameters/positions.md)
  The positions of all rigid bodies under the influence of the effect, or nil if positional information was not requested.
- [let velocities: UnsafeForceEffectBuffer<SIMD3<Float>>?](forceeffectparameters/velocities.md)
  The velocities of all rigid bodies under the influence of the effect, or nil if velocity information was not requested.
### Instance Methods
- [func setForce(SIMD3<Float>, index: Int)](forceeffectparameters/setforce(_:index:).md)
  Sets the force for each rigid body.
- [func setTorque(SIMD3<Float>, index: Int)](forceeffectparameters/settorque(_:index:).md)
  Sets the torque for each rigid body.

## See Also

- [protocol ForceEffectProtocol](forceeffectprotocol.md)
  A protocol that defines a custom force effect.
- [enum ForceMode](forcemode.md)
  The options that control how physics system applies the forces.
- [protocol ForceEffectBase](forceeffectbase.md)
  The base protocol for the wrapping force effect structure containing common parameters for all force-effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectparameters)*