# landmark(for:)

**Framework**: ARKit  
**Kind**: method

Returns the location of a joint with a given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```swift
@nonobjc
func landmark(for jointName: ARSkeleton.JointName) -> simd_float2?
```

#### Discussion

Joint landmarks are normalized within the range [0..1] and are in the coordinate space of the current frame’s camera image, where 0 is the upper left, and 1 is the bottom right.

## See Also

- [var jointLandmarks: [simd_float2]](arskeleton2d/jointlandmarks-12vkw.md)
  The joint landmarks in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton2d/landmark(for:))*