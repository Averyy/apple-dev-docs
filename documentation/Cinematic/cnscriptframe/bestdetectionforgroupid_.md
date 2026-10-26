# bestDetectionForGroupID:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

The best detection to focus on in a frame among those within the given detection group.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (CNDetection *) bestDetectionForGroupID:(CNDetectionGroupID) detectionGroupID;
```

#### Return Value

An object representing the best detection to focus on in a frame among those within the given detection group.

#### Discussion

Some types of detections also include a detection group ID that associates related detections, such as a face and torso, of the same person.

## Parameters

- `detectionGroupID`: Associates related detections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnscriptframe/bestdetectionforgroupid:)*