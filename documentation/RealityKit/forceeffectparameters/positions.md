# positions

**Framework**: RealityKit  
**Kind**: property

The positions of all rigid bodies under the influence of the effect, or nil if positional information was not requested.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
let positions: UnsafeForceEffectBuffer<SIMD3<Float>>?
```

#### Discussion

The position is located at each body’s center of mass, relative to the origin of the effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectparameters/positions)*