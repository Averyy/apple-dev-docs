# anchorFromJointTransform

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The position and orientation of this joint relative to the base joint of the skeleton.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var anchorFromJointTransform: simd_float4x4 { get }
```

## See Also

### Tracking the position of hand joints
- [var parentFromJointTransform: simd_float4x4](./parentfromjointtransform.md)
  The transform from the joint to its parent joint’s coordinate system.
- [var isTracked: Bool](./istracked.md)
  A Boolean value that indicates whether ARKit tracks a hand joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint/anchorfromjointtransform)*