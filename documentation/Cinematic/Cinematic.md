# Cinematic

**Framework**: Cinematic  
**Kind**: module  
**Role**: Framework

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
- [Playing and editing Cinematic mode video](./playing-and-editing-cinematic-mode-video.md)
  Play and edit Cinematic mode video with an adjustable depth of field and focus points.
- [class CNScript](./cnscript-1ispe.md)
  A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.
- [CNScript](./cnscript-9e1zn.md)
  A collection of focus decisions, focus transitions, detections, and detection tracks associated with a movie captured in Cinematic mode and methods to change them.
- [CNScriptChanges](./cnscriptchanges.md)
  An object that represents a snapshot of the changes made to a movie script, including the added user decisions and detection tracks.
- [CNScriptFrame](./cnscriptframe.md)
  An object that represents what to focus on, and where to focus, in a given movie frame.
### Reading and rendering
- [class CNAssetInfo](./cnassetinfo-2ata2.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [class CNCompositionInfo](./cncompositioninfo-7eunn.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [class CNRenderingSession](./cnrenderingsession-1hzh8.md)
  An object representing the context in which rendering occurs.
- [CNAssetInfo](./cnassetinfo-8ja4t.md)
  An object that provides Cinematic-specific information about an asset, including its tracks.
- [CNCompositionInfo](./cncompositioninfo-vzoh.md)
  An object that enables you to add the appropriate number of tracks for a Cinematic asset.
- [CNRenderingSession](./cnrenderingsession-8yghc.md)
  An object representing the context in which rendering occurs.
- [CNRenderingSessionAttributes](./cnrenderingsessionattributes.md)
  A structure for movie-wide attributes required for proper rendering.
- [CNRenderingSessionFrameAttributes](./cnrenderingsessionframeattributes.md)
  Creates an object with the per frame attributes that control the appearance of a single frame of the Cinematic movie.
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
- [enum CNDetectionType](./cndetectiontype.md)
  The type of object detected, such as face, torso, cat, dog and so on.
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
### Custom Object Tracking
- [struct CNBoundsPrediction](./cnboundsprediction-swift.struct.md)
  A structure representing the bounds of the predicted subject.
- [class CNObjectTracker](./cnobjecttracker-1n598.md)
  An object that converts a normalized point or rectangle into a detection track that tracks an object over time.
- [CNObjectTracker](./cnobjecttracker-7aliq.md)
  An object that converts a normalized point or rectangle into a detection track that tracks an object over time.
- [CNBoundsPrediction](./cnboundsprediction-c.class.md)
  An object representing the bounds of the predicted subject.
### Structures
- [struct CNCinematicError](./cncinematicerror.md)
### Reference
- [Cinematic Enumerations](./cinematic-enumerations.md)
- [Cinematic Constants](./cinematic-constants.md)
- [Cinematic Data Types](./cinematic-data-types.md)
### Classes
- [class CNAssetPreprocessConfiguration](./cnassetpreprocessconfiguration-5u7dk.md)
- [class CNAssetSpatialAudioInfo](./cnassetspatialaudioinfo-7hdev.md)
- [class CNImageRenderingSession](./cnimagerenderingsession.md)
  A session for rendering a shallow depth-of-field (SDoF) effect onto still images using Metal.
- [class CNImageRenderingSessionConfiguration](./cnimagerenderingsessionconfiguration.md)
  Configuration for a CNImageRenderingSession, specifying the rendering quality and algorithm version.
- [CNAssetPreprocessConfiguration](./cnassetpreprocessconfiguration-7xlwe.md)
- [CNAssetSpatialAudioInfo](./cnassetspatialaudioinfo-57yc5.md)
### Enumerations
- [enum CNCinematicCapability](./cncinematiccapability.md)
- [enum CNCinematicResourceVersion](./cncinematicresourceversion.md)
- [enum CNResourceStatus](./cnresourcestatus.md)
- [enum CNSpatialAudioContentType](./cnspatialaudiocontenttype.md)
- [enum CNSpatialAudioRenderingStyle](./cnspatialaudiorenderingstyle.md)
### Macros
- [CN_CINEMATIC_EXTERN](./cn_cinematic_extern.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/Cinematic)*