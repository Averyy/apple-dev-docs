# bestDetection(for:)

**Framework**: Cinematic  
**Kind**: method

The best detection to focus on in a frame among those within the given detection group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
func bestDetection(for detectionGroupID: CNDetectionGroupID) -> CNDetection?
```

#### Return Value

An object representing the best detection to focus on in a frame among those within the given detection group.

#### Discussion

Some types of detections also include a detection group ID that associates related detections, such as a face and torso, of the same person.

## Parameters

- `detectionGroupID`: Associates related detections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscript-1ispe/frame/bestdetection(for:))*