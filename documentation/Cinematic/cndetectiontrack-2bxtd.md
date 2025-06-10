# CNDetectionTrack

**Framework**: Cinematic  
**Kind**: class

An object representing a series of detections of the same subject over time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class CNDetectionTrack
```

## Topics

### Instance Properties
- [var detectionGroupID: CNDetectionGroupID](cndetectiontrack-2bxtd/detectiongroupid.md)
  The detection group ID of the subject detected by the track.
- [var detectionID: CNDetectionID](cndetectiontrack-2bxtd/detectionid.md)
  The unique ID of the subject detected during this track.
- [var detectionType: CNDetectionType](cndetectiontrack-2bxtd/detectiontype.md)
  The type of object that’s detected.
- [var isDiscrete: Bool](cndetectiontrack-2bxtd/isdiscrete.md)
  A flag determining if the detection track has discrete detections, otherwise continuous.
- [var isUserCreated: Bool](cndetectiontrack-2bxtd/isusercreated.md)
  A flag indicating if the client created the detection track.
### Instance Methods
- [func detection(atOrBefore: CMTime) -> CNDetection?](cndetectiontrack-2bxtd/detection(atorbefore:).md)
  Returns the array of detections in the detection track before a given time.
- [func detection(nearest: CMTime) -> CNDetection?](cndetectiontrack-2bxtd/detection(nearest:).md)
  Returns the array of detections in the detection track nearest a given time.
- [func detections(in: CMTimeRange) -> [CNDetection]](cndetectiontrack-2bxtd/detections(in:).md)
  Returns the array of detections in the detection track within the given time range.

## Relationships

### Inherited By
- [CNCustomDetectionTrack](cncustomdetectiontrack-9a2zo.md)
- [CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)

## See Also

- [Editing Spatial Audio with an audio mix](editing-spatial-audio-with-an-audio-mix.md)
  Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.
- [struct CNDetection](cndetection-swift.struct.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [struct CNDecision](cndecision-swift.struct.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [class CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [class CNCustomDetectionTrack](cncustomdetectiontrack-9a2zo.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetectiontrack-2bxtd)*