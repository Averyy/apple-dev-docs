# isTracked

**Framework**: ARKit  
**Kind**: property

A Boolean value that indicates whether ARKit tracks a hand joint.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var isTracked: Bool { get }
```

#### Discussion

When the environment provides insufficient lighting, or if an object occludes the hand joint, `isTracked` may return `false`. Even under these circumstances, ARKit returns a plausible transform for the joint.

Check for `isTracked` when you require high accuracy for the joint transform. Don’t check for this property in situations where you expect to occlude hand joints, such as in a custom gesture implementation.

## See Also

- [var anchorFromJointTransform: simd_float4x4](handskeleton/joint/anchorfromjointtransform.md)
  The position and orientation of this joint relative to the base joint of the skeleton.
- [var parentFromJointTransform: simd_float4x4](handskeleton/joint/parentfromjointtransform.md)
  The transform from the joint to its parent joint’s coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handskeleton/joint/istracked)*