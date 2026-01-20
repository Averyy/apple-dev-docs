# MPSImageKeypointRangeInfo

**Framework**: Metal Performance Shaders  
**Kind**: struct

A structure that specifies information to find the keypoints in an image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSImageKeypointRangeInfo
```

## Topics

### Instance Properties
- [var maximumKeypoints: Int](mpsimagekeypointrangeinfo/maximumkeypoints.md)
- [var minimumThresholdValue: Float](mpsimagekeypointrangeinfo/minimumthresholdvalue.md)
### Initializers
- [init()](mpsimagekeypointrangeinfo/init.md)
- [init(maximumKeypoints: Int, minimumThresholdValue: Float)](mpsimagekeypointrangeinfo/init(maximumkeypoints:minimumthresholdvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class MPSImageFindKeypoints](mpsimagefindkeypoints.md)
  A kernel that is used to find a list of keypoints.
- [struct MPSImageKeypointData](mpsimagekeypointdata.md)
  A structure that specifies keypoint information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagekeypointrangeinfo)*