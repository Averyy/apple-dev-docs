# init(time:detectionID:strong:)

**Framework**: Cinematic  
**Kind**: init

Makes a decision to focus on the best among those detections with the same detection group ID.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
init(time: CMTime, detectionID: CNDetectionID, strong isStrong: Bool)
```

#### Discussion

A strong decision keeps focus for as long as possible on the detected subject.

## Parameters

- `time`: The first presentation time which the subject should be in focus.
- `detectionID`: A unique number representing the detection to focus on if this is a group decision.
- `isStrong`: A flag representing whether this is a strong decision or not. A strong decision keeps focus for as long as possible.

## See Also

- [init(time: CMTime, detectionGroupID: CNDetectionGroupID, strong: Bool)](cndecision-swift.struct/init(time:detectiongroupid:strong:).md)
  Makes a decision to focus on the detection with the given unique detection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndecision-swift.struct/init(time:detectionid:strong:))*