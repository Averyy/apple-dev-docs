# MPSImageKeypointRangeInfo

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

A structure that specifies information to find the keypoints in an image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSImageKeypointRangeInfo
```

```c
typedef struct { ... } MPSImageKeypointRangeInfo;
```

## Topics

### Instance Properties
- [var maximumKeypoints: Int](./mpsimagekeypointrangeinfo/maximumkeypoints.md)
- [var minimumThresholdValue: Float](./mpsimagekeypointrangeinfo/minimumthresholdvalue.md)
### Initializers
- [init()](./mpsimagekeypointrangeinfo/init%28%29.md)
- [init(maximumKeypoints: Int, minimumThresholdValue: Float)](./mpsimagekeypointrangeinfo/init%28maximumkeypoints,minimumthresholdvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Keypoints
- [class MPSImageFindKeypoints](./mpsimagefindkeypoints.md)
  A kernel that is used to find a list of keypoints.
- [struct MPSImageKeypointData](./mpsimagekeypointdata.md)
  A structure that specifies keypoint information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagekeypointrangeinfo)*