# MPSImageKeypointData

**Framework**: Metal Performance Shaders  
**Kind**: struct  
**Role**: Structure

A structure that specifies keypoint information.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MPSImageKeypointData
```

```c
typedef struct { ... } MPSImageKeypointData;
```

## Topics

### Instance Properties
- [var keypointColorValue: Float](./mpsimagekeypointdata/keypointcolorvalue.md)
- [var keypointCoordinate: vector_ushort2](./mpsimagekeypointdata/keypointcoordinate.md)
### Initializers
- [init()](./mpsimagekeypointdata/init%28%29.md)
- [init(keypointCoordinate: vector_ushort2, keypointColorValue: Float)](./mpsimagekeypointdata/init%28keypointcoordinate,keypointcolorvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Keypoints
- [class MPSImageFindKeypoints](./mpsimagefindkeypoints.md)
  A kernel that is used to find a list of keypoints.
- [struct MPSImageKeypointRangeInfo](./mpsimagekeypointrangeinfo.md)
  A structure that specifies information to find the keypoints in an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagekeypointdata)*