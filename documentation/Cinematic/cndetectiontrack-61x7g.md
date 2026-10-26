# CNDetectionTrack

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object representing a series of detections of the same subject over time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNDetectionTrack : NSObject
```

## Topics

### Instance Properties
- [detectionGroupID](./cndetectiontrack-61x7g/detectiongroupid.md)
  The detection group ID of the subject detected by the track.
- [detectionID](./cndetectiontrack-61x7g/detectionid.md)
  The unique ID of the subject detected during this track.
- [detectionType](./cndetectiontrack-61x7g/detectiontype.md)
  The type of object that’s detected.
- [discrete](./cndetectiontrack-61x7g/discrete.md)
  A flag determining if the detection track has discrete detections, otherwise continuous.
- [userCreated](./cndetectiontrack-61x7g/usercreated.md)
  A flag indicating if the client created the detection track.
### Instance Methods
- [- detectionAtOrBeforeTime:](./cndetectiontrack-61x7g/detectionatorbeforetime_.md)
  Returns the array of detections in the detection track before a given time.
- [- detectionNearestTime:](./cndetectiontrack-61x7g/detectionnearesttime_.md)
  Returns the array of detections in the detection track nearest a given time.
- [- detectionsInTimeRange:](./cndetectiontrack-61x7g/detectionsintimerange_.md)
  Returns the array of detections in the detection track within the given time range.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CNCustomDetectionTrack](./cncustomdetectiontrack-891hc.md)
- [CNFixedDetectionTrack](./cnfixeddetectiontrack-5aei2.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Editing
- [CNDetection](./cndetection-c.class.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [CNDecision](./cndecision-c.class.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [CNFixedDetectionTrack](./cnfixeddetectiontrack-5aei2.md)
  An object representing the fixed detection track.
- [CNCustomDetectionTrack](./cncustomdetectiontrack-891hc.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](./cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-61x7g)*