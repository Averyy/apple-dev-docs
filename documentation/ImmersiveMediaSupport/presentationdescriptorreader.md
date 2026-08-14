# PresentationDescriptorReader

**Framework**: Immersive Media Support  
**Kind**: class

An object that provides the functionality required to understand and process immersive presentation commands.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class PresentationDescriptorReader
```

#### Overview

Immersive commands are packed as an array of [`PresentationCommand`](presentationcommand.md) objects contained in a [`PresentationDescriptor`](presentationdescriptor.md). This object is used during an Immersive Video playback as a source of rendering values its published variables, or the application can pull presentation commands by time to write an output metadata track.

## Topics

### Initializers
- [init(presentationDescriptor: PresentationDescriptor, isSideloaded: Bool)](presentationdescriptorreader/init(presentationdescriptor:issideloaded:).md)
  Initializes an instance that contains the specified presentation descriptor.
### Instance Properties
- [var cameraID: String?](presentationdescriptorreader/cameraid.md)
  The current camera ID string of the immersive camera to use when rendering playback for the PTS specified in the last call to the update method.
- [var colorFade: simd_float3](presentationdescriptorreader/colorfade.md)
  The current fade color for color fading of the video frames during playback for the PTS specified in the last call to the update method.
- [var colorFadeOpacity: Float](presentationdescriptorreader/colorfadeopacity.md)
  The current color fade opacity of the video frames during playback for the PTS specified in the last call to the update method.
- [var environmentFadeOpacity: Float](presentationdescriptorreader/environmentfadeopacity.md)
  The current opacity of the environment backdrops during playback for the PTS specified in the last call to the update method.
- [var isShotFlopped: Bool](presentationdescriptorreader/isshotflopped.md)
  A Boolean value that indicates whether to horizontally flip the video frame for the PTS specified in the last call to the update method.
- [var isSideloaded: Bool](presentationdescriptorreader/issideloaded.md)
  A Boolean value that indicates whether the reader input is sideloaded or is it set during playback.
- [var presentationCommands: [PresentationCommand]](presentationdescriptorreader/presentationcommands.md)
  The active presentation commands for the PTS specified in the last call to the update method.
- [var presentationDescriptor: PresentationDescriptor](presentationdescriptorreader/presentationdescriptor.md)
  The presentation descriptor that contains the presentation commands to process.
- [var cameraOverrides: SetCameraCommand.Overrides?](presentationdescriptorreader/cameraoverrides.md)
  The current camera params which would override static metadata to use when rendering playback for the PTS specified in the last call to the update method.
- [var isShotFlipped: Bool](presentationdescriptorreader/isshotflipped.md)
  A Boolean value that indicates whether to vertically flip the video frame for the PTS specified in the last call to the update method.
### Instance Methods
- [func metadataItem(frameTimeRange: CMTimeRange) throws -> AVMetadataItem?](presentationdescriptorreader/metadataitem(frametimerange:).md)
  Builds a metadata item containing the presentation commands active at the start of the specified frame’s time range.
- [func metadataTrack(timeRange: CMTimeRange?) throws -> [AVMetadataItem]](presentationdescriptorreader/metadatatrack(timerange:).md)
  Retrieves all metadata items to write to an output metadata track, optionally clipped to a segment time range. Pass a `timeRange` to produce one item per segment (e.g. per IDR group or per fixed-length interval).
- [func outputPresentationCommands(for: CMTime) -> [PresentationCommand]?](presentationdescriptorreader/outputpresentationcommands(for:).md)
  This function returns all presentation commands to be muxed into an MOV during an `AVAssetWriter` session. Don’t use this function for playback rendering.
- [func processPresentationCommands(for: CMTime)](presentationdescriptorreader/processpresentationcommands(for:).md)
  Processes the commands and updates the publishers exported by this reader when called by the application (e.g. render/playback loop)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Escapable](../swift/escapable.md)
- [Observable](../observation/observable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [enum PresentationCommand](presentationcommand.md)
  A set of properties that define the interface for a presentation command.
- [struct FadeCommand](fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct FadeEnvironmentCommand](fadeenvironmentcommand.md)
  A command type for opacity fading environment backdrops during immersive media playback.
- [struct SetCameraCommand](setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct ShotFlipCommand](shotflipcommand.md)
  A command type to flip the video frames vertically during playback for the duration of the command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader)*