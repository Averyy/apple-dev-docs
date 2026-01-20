# MPSImageKeypointData

**Framework**: Metal Performance Shaders  
**Kind**: struct

A structure that specifies keypoint information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSImageKeypointData
```

## Topics

### Instance Properties
- [var keypointColorValue: Float](mpsimagekeypointdata/keypointcolorvalue.md)
- [var keypointCoordinate: vector_ushort2](mpsimagekeypointdata/keypointcoordinate.md)
### Initializers
- [init()](mpsimagekeypointdata/init.md)
- [init(keypointCoordinate: vector_ushort2, keypointColorValue: Float)](mpsimagekeypointdata/init(keypointcoordinate:keypointcolorvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class MPSImageFindKeypoints](mpsimagefindkeypoints.md)
  A kernel that is used to find a list of keypoints.
- [struct MPSImageKeypointRangeInfo](mpsimagekeypointrangeinfo.md)
  A structure that specifies information to find the keypoints in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagekeypointdata)*