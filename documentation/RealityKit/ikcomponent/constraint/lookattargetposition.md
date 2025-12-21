# lookAtTargetPosition

**Framework**: RealityKit  
**Kind**: property

The point demand which the look-at constraint uses to generate a new orientation demand.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var lookAtTargetPosition: SIMD3<Float> { get set }
```

#### Discussion

The position is in model space. The computed demand overrides the rotation part of [`target`](ikcomponent/constraint/target.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/constraint/lookattargetposition)*