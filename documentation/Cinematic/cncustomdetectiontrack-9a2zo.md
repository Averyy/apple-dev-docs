# CNCustomDetectionTrack

**Framework**: Cinematic  
**Kind**: class

An object representing a discrete detection track composed of individual detections.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class CNCustomDetectionTrack
```

## Topics

### Initializers
- [init(detections: [CNDetection], smooth: Bool)](cncustomdetectiontrack-9a2zo/init(detections:smooth:).md)
  Initializes a custom detection track object with an array of detections and optionally applying smoothing.
### Instance Properties
- [var allDetections: [CNDetection]](cncustomdetectiontrack-9a2zo/alldetections.md)
  All detected objects in the track.

## Relationships

### Inherits From
- [CNDetectionTrack](cndetectiontrack-2bxtd.md)

## See Also

- [struct CNDetection](cndetection-swift.struct.md)
  A structure that represents a detected subject, face, torso or pet at a particular time.
- [struct CNDecision](cndecision-swift.struct.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [class CNDetectionTrack](cndetectiontrack-2bxtd.md)
  An object representing a series of detections of the same subject over time.
- [class CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [enum CNDetectionType](cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cncustomdetectiontrack-9a2zo)*