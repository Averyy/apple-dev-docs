# CNDetectionType

**Framework**: Cinematic  
**Kind**: enum  
**Role**: Enumeration

The type of object detected, such as face, torso, cat, dog and so on.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
enum CNDetectionType
```

```c
enum CNDetectionType : NSInteger;
```

## Topics

### Enumeration Cases
- [CNDetectionType.autoFocus](./cndetectiontype/autofocus.md)
- [CNDetectionType.catBody](./cndetectiontype/catbody.md)
- [CNDetectionType.catHead](./cndetectiontype/cathead.md)
- [CNDetectionType.custom](./cndetectiontype/custom.md)
- [CNDetectionType.dogBody](./cndetectiontype/dogbody.md)
- [CNDetectionType.dogHead](./cndetectiontype/doghead.md)
- [CNDetectionType.fixedFocus](./cndetectiontype/fixedfocus.md)
- [CNDetectionType.humanFace](./cndetectiontype/humanface.md)
- [CNDetectionType.humanHead](./cndetectiontype/humanhead.md)
- [CNDetectionType.humanTorso](./cndetectiontype/humantorso.md)
- [CNDetectionType.sportsBall](./cndetectiontype/sportsball.md)
- [CNDetectionType.unknown](./cndetectiontype/unknown.md)
### Initializers
- [init?(rawValue: Int)](./cndetectiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Editing
- [Editing Spatial Audio with an audio mix](./editing-spatial-audio-with-an-audio-mix.md)
  Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.
- [struct CNDetection](./cndetection-swift.struct.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [struct CNDecision](./cndecision-swift.struct.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [class CNDetectionTrack](./cndetectiontrack-2bxtd.md)
  An object representing a series of detections of the same subject over time.
- [class CNFixedDetectionTrack](./cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [class CNCustomDetectionTrack](./cncustomdetectiontrack-9a2zo.md)
  An object representing a discrete detection track composed of individual detections.
- [CNDetection](./cndetection-c.class.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [CNDecision](./cndecision-c.class.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [CNDetectionTrack](./cndetectiontrack-61x7g.md)
  An object representing a series of detections of the same subject over time.
- [CNFixedDetectionTrack](./cnfixeddetectiontrack-5aei2.md)
  An object representing the fixed detection track.
- [CNCustomDetectionTrack](./cncustomdetectiontrack-891hc.md)
  An object representing a discrete detection track composed of individual detections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontype)*