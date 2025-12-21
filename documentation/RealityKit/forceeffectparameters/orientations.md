# orientations

**Framework**: RealityKit  
**Kind**: property

The orientations of all rigid bodies under the influence of the effect, or nil if rotational information was not requested.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
let orientations: UnsafeForceEffectBuffer<simd_quatf>?
```

#### Discussion

The orientation is relative to the effect’s transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/forceeffectparameters/orientations)*