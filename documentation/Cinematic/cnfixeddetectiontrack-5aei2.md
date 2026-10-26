# CNFixedDetectionTrack

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object representing the fixed detection track.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNFixedDetectionTrack : CNDetectionTrack
```

## Topics

### Instance Properties
- [focusDisparity](./cnfixeddetectiontrack-5aei2/focusdisparity.md)
  The disparity to use in order to focus on the object.
- [originalDetection](./cnfixeddetectiontrack-5aei2/originaldetection.md)
  The original detection based on the fixed detection track.
### Instance Methods
- [- initWithFocusDisparity:](./cnfixeddetectiontrack-5aei2/initwithfocusdisparity_.md)
  Creates a detection track with fixed focus at the given disparity.
- [- initWithOriginalDetection:](./cnfixeddetectiontrack-5aei2/initwithoriginaldetection_.md)
  Creates a detection track with fixed focus at the disparity of an existing detection.

## Relationships

### Inherits From
- [CNDetectionTrack](./cndetectiontrack-61x7g.md)

## See Also

### Editing
- [CNDetection](./cndetection-c.class.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [CNDecision](./cndecision-c.class.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [CNDetectionTrack](./cndetectiontrack-61x7g.md)
  An object representing a series of detections of the same subject over time.
- [CNCustomDetectionTrack](./cncustomdetectiontrack-891hc.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](./cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnfixeddetectiontrack-5aei2)*