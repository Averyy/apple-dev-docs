# CNCustomDetectionTrack

**Framework**: Cinematic  
**Kind**: class  
**Role**: Class

An object representing a discrete detection track composed of individual detections.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```objc
@interface CNCustomDetectionTrack : CNDetectionTrack
```

## Topics

### Instance Properties
- [allDetections](./cncustomdetectiontrack-891hc/alldetections.md)
  All detected objects in the track.
### Instance Methods
- [- initWithDetections:smooth:](./cncustomdetectiontrack-891hc/initwithdetections_smooth_.md)
  Initializes a custom detection track with an array of detections, optionally applying smoothing.

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
- [CNFixedDetectionTrack](./cnfixeddetectiontrack-5aei2.md)
  An object representing the fixed detection track.
- [enum CNDetectionType](./cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cncustomdetectiontrack-891hc)*