# CNDecision

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNDecision : NSObject
```

## Topics

### Instance Properties
- [detectionGroupID](./cndecision-c.class/detectiongroupid.md)
  A unique number representing the detection to focus on if this is a group decision.
- [detectionID](./cndecision-c.class/detectionid.md)
  The unique ID representing the detection to focus on if this isn’t a group decision.
- [groupDecision](./cndecision-c.class/groupdecision.md)
  A flag representing whether this is a group decision.
- [strongDecision](./cndecision-c.class/strongdecision.md)
  A flag representing whether this is a strong decision.
- [time](./cndecision-c.class/time.md)
  The first presentation time that the subject should be in focus.
- [userDecision](./cndecision-c.class/userdecision.md)
  A flag representing whether this is a user-created decision or a base decision.
### Instance Methods
- [- initWithTime:detectionGroupID:strong:](./cndecision-c.class/initwithtime_detectiongroupid_strong_.md)
  Makes a decision to focus on the detection with the given unique detection.
- [- initWithTime:detectionID:strong:](./cndecision-c.class/initwithtime_detectionid_strong_.md)
  Makes a decision to focus on the best among those detections with the same detection group ID.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Editing
- [CNDetection](./cndetection-c.class.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [CNDetectionTrack](./cndetectiontrack-61x7g.md)
  An object representing a series of detections of the same subject over time.
- [CNFixedDetectionTrack](./cnfixeddetectiontrack-5aei2.md)
  An object representing the fixed detection track.
- [CNCustomDetectionTrack](./cncustomdetectiontrack-891hc.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](./cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndecision-c.class)*