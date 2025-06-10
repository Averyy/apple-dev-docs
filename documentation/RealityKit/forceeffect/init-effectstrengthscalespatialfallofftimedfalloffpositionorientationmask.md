# init(effect:strengthScale:spatialFalloff:timedFalloff:position:orientation:mask:)

**Framework**: RealityKit  
**Kind**: init

Creates a ForceEffect struct.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(effect: ForceEffectType, strengthScale: Double = 1.0, spatialFalloff: SpatialForceFalloff? = nil, timedFalloff: TimedForceFalloff? = nil, position: SIMD3<Float> = SIMD3<Float>(0, 0, 0), orientation: simd_quatf = simd_quaternion(0, 0, 0, 1), mask: CollisionGroup = .all)
```

## Parameters

- `effect`: Effect specific parameters.
- `strengthScale`: Scales the overall strength of the effect.
- `spatialFalloff`: The falloff function parameters used to attenuate the force based on distance from the effect origin.
- `timedFalloff`: The falloff function parameters used to attenuate the force based on time.
- `position`: The position  of the effect relative to the effect entity’s transform.
- `orientation`: The orientation of the effect relative to the effect entity’s transform.
- `mask`: The mask used to select which groups of rigid bodies the effect should be applied to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffect/init(effect:strengthscale:spatialfalloff:timedfalloff:position:orientation:mask:))*