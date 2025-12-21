# parentFromJointTransform

**Framework**: ARKit  
**Kind**: property

The transform from the joint to its parent joint’s coordinate system.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var parentFromJointTransform: simd_float4x4 { get }
```

#### Discussion

The root joint’s [`parentFromJointTransform`](handskeleton/joint/parentfromjointtransform.md) is an identity matrix.

## See Also

- [var anchorFromJointTransform: simd_float4x4](handskeleton/joint/anchorfromjointtransform.md)
  The position and orientation of this joint relative to the base joint of the skeleton.
- [var isTracked: Bool](handskeleton/joint/istracked.md)
  A Boolean value that indicates whether ARKit tracks a hand joint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint/parentfromjointtransform)*