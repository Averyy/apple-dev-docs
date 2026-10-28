# initWithTime:detectionID:strong:

**Framework**: Cinematic  
**Kind**: method  
**Role**: Instance Method

Makes a decision to focus on the best among those detections with the same detection group ID.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
- (instancetype) initWithTime:(CMTime) time detectionID:(CNDetectionID) detectionID strong:(BOOL) isStrong;
```

## Return Value

Creates an object representing a decision to focus on the detection with the given detection ID.

## Discussion

A strong decision keeps focus for as long as possible on the detected subject.

## Parameters

- `time`: The first presentation time which the subject should be in focus.
- `detectionID`: A unique number representing the detection to focus on if this is a group decision.
- `isStrong`: A flag representing whether this is a strong decision or not. A strong decision keeps focus for as long as possible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndecision-c.class/initwithtime:detectionid:strong:)*