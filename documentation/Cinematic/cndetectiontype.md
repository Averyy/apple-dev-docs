# CNDetectionType

**Framework**: Cinematic  
**Kind**: enum

The type of object detected, such as face, torso, cat, dog and so on.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
enum CNDetectionType
```

## Topics

### Enumeration Cases
- [CNDetectionType.autoFocus](cndetectiontype/autofocus.md)
- [CNDetectionType.catBody](cndetectiontype/catbody.md)
- [CNDetectionType.catHead](cndetectiontype/cathead.md)
- [CNDetectionType.custom](cndetectiontype/custom.md)
- [CNDetectionType.dogBody](cndetectiontype/dogbody.md)
- [CNDetectionType.dogHead](cndetectiontype/doghead.md)
- [CNDetectionType.fixedFocus](cndetectiontype/fixedfocus.md)
- [CNDetectionType.humanFace](cndetectiontype/humanface.md)
- [CNDetectionType.humanHead](cndetectiontype/humanhead.md)
- [CNDetectionType.humanTorso](cndetectiontype/humantorso.md)
- [CNDetectionType.sportsBall](cndetectiontype/sportsball.md)
- [CNDetectionType.unknown](cndetectiontype/unknown.md)
### Initializers
- [init?(rawValue: Int)](cndetectiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct CNDetection](cndetection-swift.struct.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [struct CNDecision](cndecision-swift.struct.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [class CNDetectionTrack](cndetectiontrack-2bxtd.md)
  An object representing a series of detections of the same subject over time.
- [class CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [class CNCustomDetectionTrack](cncustomdetectiontrack-9a2zo.md)
  An object representing a discrete detection track composed of individual detections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontype)*