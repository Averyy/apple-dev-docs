# jointLandmarks

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

The joint landmarks in normalized coordinates.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
@property (nonatomic, readonly) const simd_float2 * jointLandmarks;
```

## Discussion

The joint landmarks are normalized within the range [0..1] in the coordinate space of the current frame’s camera image, where 0 is the upper left, and 1 is the bottom right.

## See Also

### Getting Joint Landmarks
- [- landmarkForJointNamed:](./landmarkforjointnamed_.md)
  Returns the location of a joint with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton2d/jointlandmarks-3en0x)*