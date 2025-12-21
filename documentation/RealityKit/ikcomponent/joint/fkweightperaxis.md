# fkWeightPerAxis

**Framework**: RealityKit  
**Kind**: property

The per-axis weight of the source animation demand on the joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var fkWeightPerAxis: SIMD3<Float> { get set }
```

#### Discussion

This value is in the closed range `[0, 1]`, where `0` means no influence, and `1` is the maximum influence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/joint/fkweightperaxis)*