# init(bounds:rate:distanceOffset:)

**Framework**: RealityKit  
**Kind**: init

Creates a spatial force falloff.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
init(bounds: ForceEffectBounds, rate: Double = 1.0, distanceOffset: Double = 0)
```

#### Discussion

- When the rate is , no falloff occurs. (Rigid bodies outside the bounds are culled.)
- When the rate is , falloff occurs slower and is sublinear.
- When the rate is , falloff is linear.
- When the rate is , falloff occurs faster and is nonlinear.

## Parameters

- `bounds`: The spatial bounds used to compute the strength falloff.
- `rate`: The rate at which the effect’s strength diminishes.
- `distanceOffset`: The offset from the origin where fall begins.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialforcefalloff/init(bounds:rate:distanceoffset:))*