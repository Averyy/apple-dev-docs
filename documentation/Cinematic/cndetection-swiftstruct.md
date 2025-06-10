# CNDetection

**Framework**: Cinematic  
**Kind**: struct

A structure that represents a detected subject, face, torso or pet at a particular time.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct CNDetection
```

#### Overview

Specifies the type, distance bounds, and time of the detection. Detections obtained from the Cinematic script include a unique number that can tracks the detection over time.

Some types of detections also include a unique group number that associates related detections (for example, the face and torso of the same person).

## Topics

### Initializers
- [init(time: CMTime, detectionType: CNDetectionType, normalizedRect: CGRect, focusDisparity: Float)](cndetection-swift.struct/init(time:detectiontype:normalizedrect:focusdisparity:).md)
  Creates a Cinematic detection of a subject.
### Instance Properties
- [var detectionGroupID: CNDetectionGroupID?](cndetection-swift.struct/detectiongroupid.md)
  A unique number representing the detection to focus on if this is a group decision.
- [var detectionID: CNDetectionID?](cndetection-swift.struct/detectionid.md)
  An unique identifier assigned by the Cinematic script to all detections of the same subject and detection type across time.
- [var detectionType: CNDetectionType](cndetection-swift.struct/detectiontype.md)
  The type of object detected, such as the face, torso, cat, dog, and so on.
- [var focusDisparity: Float](cndetection-swift.struct/focusdisparity.md)
  The disparity to use in order to focus on the object.
- [var normalizedRect: CGRect](cndetection-swift.struct/normalizedrect.md)
  The rectangle within the image where the object occurs, normalized such that (0.0, 0.0) is the top-left and (1.0, 1.0) is the bottom-right.
- [var time: CMTime](cndetection-swift.struct/time.md)
  The first presentation time which the subject should be in focus.
### Type Methods
- [static func accessibilityLabel(for: CNDetectionType) -> String](cndetection-swift.struct/accessibilitylabel(for:).md)
  A localized accessibility label converting a specific detection type into a broad category such as a person, pet, and so on.
- [static func disparity(in: CGRect, sourceDisparity: CVPixelBuffer, detectionType: CNDetectionType, priorDisparity: Float?) -> Float](cndetection-swift.struct/disparity(in:sourcedisparity:detectiontype:priordisparity:).md)
  Determines the disparity to use to focus on the object in the rectangle.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Editing Spatial Audio with an audio mix](editing-spatial-audio-with-an-audio-mix.md)
  Add Spatial Audio editing capabilities with the Audio Mix API in the Cinematic framework.
- [struct CNDecision](cndecision-swift.struct.md)
  An object that represents a decision to focus on a particular detection, or group of detections, at a particular time.
- [class CNDetectionTrack](cndetectiontrack-2bxtd.md)
  An object representing a series of detections of the same subject over time.
- [class CNFixedDetectionTrack](cnfixeddetectiontrack-93rrw.md)
  An object representing the fixed detection track.
- [class CNCustomDetectionTrack](cncustomdetectiontrack-9a2zo.md)
  An object representing a discrete detection track composed of individual detections.
- [enum CNDetectionType](cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cndetection-swift.struct)*