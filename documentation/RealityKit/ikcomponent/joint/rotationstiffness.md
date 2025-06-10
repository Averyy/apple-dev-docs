# rotationStiffness

**Framework**: RealityKit  
**Kind**: property

The per-axis rotational stiffness of the joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var rotationStiffness: SIMD3<Float> { get set }
```

#### Discussion

A joint with higher stiffness will rotate less to reach demands.

This value is in the closed range `[0, 1]`, where `0` means the joint is free to rotate, and `1` allows no movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikcomponent/joint/rotationstiffness)*