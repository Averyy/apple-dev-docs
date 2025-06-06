# rotationStiffness

**Framework**: RealityKit  
**Kind**: property

The per-axis rotational stiffness of the joint.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var rotationStiffness: SIMD3<Float>
```

#### Discussion

A joint with higher stiffness rotates less to reach demands.

Values are in the closed range `[0, 1]`, where `0` means free to rotate, and `1` is no movement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/ikrig/joint/rotationstiffness)*