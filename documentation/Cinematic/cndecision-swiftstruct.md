# CNDecision

**Framework**: Cinematic  
**Kind**: struct

An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct CNDecision
```

## Topics

### Initializers
- [init(time: CMTime, detectionGroupID: CNDetectionGroupID, strong: Bool)](cndecision-swift.struct/init(time:detectiongroupid:strong:).md)
  Makes a decision to focus on the detection with the given unique detection.
- [init(time: CMTime, detectionID: CNDetectionID, strong: Bool)](cndecision-swift.struct/init(time:detectionid:strong:).md)
  Makes a decision to focus on the best among those detections with the same detection group ID.
### Instance Properties
- [var focusDetectionID: CNDecision.FocusDetectionID](cndecision-swift.struct/focusdetectionid-swift.property.md)
- [var isStrongDecision: Bool](cndecision-swift.struct/isstrongdecision.md)
  A flag representing whether this is a strong decision.
- [var isUserDecision: Bool](cndecision-swift.struct/isuserdecision.md)
  A flag representing whether this is a user-created decision or a base decision.
- [var time: CMTime](cndecision-swift.struct/time.md)
  The first presentation time that the subject should be in focus.
### Enumerations
- [CNDecision.FocusDetectionID](cndecision-swift.struct/focusdetectionid-swift.enum.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Editing Spatial Audio with an audio mix](editing-spatial-audio-with-an-audio-mix.md)
  Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.
- [struct CNDetection](cndetection-swift.struct.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [class CNDetectionTrack](cndetectiontrack-2bxtd.md)
  An object representing a series of detections of the same subject over time.
- [class CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [class CNCustomDetectionTrack](cncustomdetectiontrack-9a2zo.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndecision-swift.struct)*