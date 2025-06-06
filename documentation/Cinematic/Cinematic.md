# Cinematic

**Framework**: Cinematic  
**Kind**: module

Integrate playback and editing of assets captured in Cinematic mode into your app.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+

#### Overview

The Cinematic framework enables you to add professional-level editing and playback features to movies, recorded with the Camera app’s Cinematic mode, to your apps. These are the same features used in applications such as Final Cut Pro, Photos, and iMovie. For example, this enables your apps to change focus distance and aperture in movies, creating a bokeh effect, even after recording.

## Topics

### Essentials
- [Playing and editing Cinematic mode video](playing-and-editing-cinematic-mode-video.md)
  Play and edit Cinematic mode video with an adjustable depth of field and focus points.
- [class CNScript](cnscript-1ispe.md)
  A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.
### Reading and rendering
- [class CNAssetInfo](cnassetinfo-2ata2.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [class CNCompositionInfo](cncompositioninfo-7eunn.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [class CNRenderingSession](cnrenderingsession-1hzh8.md)
  An object representing the context in which rendering occurs.
### Editing
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
- [enum CNDetectionType](cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.
### Custom Object Tracking
- [struct CNBoundsPrediction](cnboundsprediction-swift.struct.md)
  A structure representing the bounds of the predicted subject.
- [class CNObjectTracker](cnobjecttracker-1n598.md)
  An object that converts a normalized point or rectangle into a detection track that tracks an object over time.
### Structures
- [struct CNCinematicError](cncinematicerror.md)
### Reference
- [Cinematic Enumerations](cinematic-enumerations.md)
- [Cinematic Constants](cinematic-constants.md)
- [Cinematic Data Types](cinematic-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Cinematic)*