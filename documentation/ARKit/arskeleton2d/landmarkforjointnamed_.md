# landmarkForJointNamed:

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Returns the location of a joint with a given name.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+

## Declaration

```objc
- (simd_float2) landmarkForJointNamed:(ARSkeletonJointName) jointName;
```

## Return Value

Landmark in normalized image coordinates.

## Discussion

Joint landmarks are normalized within the range [0..1] and are in the coordinate space of the current frame’s camera image, where 0 is the upper left, and 1 is the bottom right. If an invalid joint name is passed the returned point will be filled with `NaN` values.

## Parameters

- `jointName`: The name of the joint.

## See Also

### Getting Joint Landmarks
- [jointLandmarks](./jointlandmarks-3en0x.md)
  The joint landmarks in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arskeleton2d/landmarkforjointnamed:)*