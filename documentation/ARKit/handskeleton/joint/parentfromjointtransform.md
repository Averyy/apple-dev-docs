# parentFromJointTransform

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The transform from the joint to its parent joint’s coordinate system.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var parentFromJointTransform: simd_float4x4 { get }
```

## Discussion

The root joint’s [`parentFromJointTransform`](./parentfromjointtransform.md) is an identity matrix.

## See Also

### Tracking the position of hand joints
- [var anchorFromJointTransform: simd_float4x4](./anchorfromjointtransform.md)
  The position and orientation of this joint relative to the base joint of the skeleton.
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether ARKit tracks a hand joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint/parentfromjointtransform)*