# CNDetection

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

A structure that represents a detected subject, face, torso or pet at a particular time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNDetection : NSObject
```

#### Overview

Specifies the type, distance bounds, and time of the detection. Detections obtained from the Cinematic script include a unique number that can tracks the detection over time.

Some types of detections also include a unique group number that associates related detections (for example, the face and torso of the same person).

## Topics

### Instance Properties
- [detectionGroupID](./cndetection-c.class/detectiongroupid.md)
  A unique number representing the detection to focus on if this is a group decision.
- [detectionID](./cndetection-c.class/detectionid.md)
  An unique identifier assigned by the Cinematic script to all detections of the same subject and detection type across time.
- [detectionType](./cndetection-c.class/detectiontype.md)
  The type of object detected, such as the face, torso, cat, dog, and so on.
- [focusDisparity](./cndetection-c.class/focusdisparity.md)
  The disparity to use in order to focus on the object.
- [normalizedRect](./cndetection-c.class/normalizedrect.md)
  The rectangle within the image where the object occurs, normalized such that (0.0, 0.0) is the top-left and (1.0, 1.0) is the bottom-right.
- [time](./cndetection-c.class/time.md)
  The first presentation time which the subject should be in focus.
### Instance Methods
- [- initWithTime:detectionType:normalizedRect:focusDisparity:](./cndetection-c.class/initwithtime_detectiontype_normalizedrect_focusdisparity_.md)
  Creates a Cinematic detection of a subject.
### Type Methods
- [+ accessibilityLabelForDetectionType:](./cndetection-c.class/accessibilitylabelfordetectiontype_.md)
  A localized accessibility label converting a specific detection type into a broad category such as a person, pet, and so on.
- [+ disparityInNormalizedRect:sourceDisparity:detectionType:priorDisparity:](./cndetection-c.class/disparityinnormalizedrect_sourcedisparity_detectiontype_priordisparity_.md)
  Determines the disparity to use to focus on the object in the rectangle.
- [+ isValidDetectionGroupID:](./cndetection-c.class/isvaliddetectiongroupid_.md)
  Determines whether a given detection group ID is valid.
- [+ isValidDetectionID:](./cndetection-c.class/isvaliddetectionid_.md)
  Determines whether a given detection ID is valid.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)

## See Also

### Editing
- [CNDecision](./cndecision-c.class.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [CNDetectionTrack](./cndetectiontrack-61x7g.md)
  An object representing a series of detections of the same subject over time.
- [CNFixedDetectionTrack](./cnfixeddetectiontrack-5aei2.md)
  An object representing the fixed detection track.
- [CNCustomDetectionTrack](./cncustomdetectiontrack-891hc.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](./cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetection-c.class)*