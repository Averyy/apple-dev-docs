# PresentationDescriptorReader

**Framework**: Immersive Media Support  
**Kind**: class

An object that provides the functionality required to understand and process immersive presentation commands.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
class PresentationDescriptorReader
```

#### Overview

Immersive commands are packed as an array of [`PresentationCommand`](presentationcommand.md) objects contained in a [`PresentationDescriptor`](presentationdescriptor.md). This object is used during an Immersive Video playback as a source of rendering values its published variables, or the application can pull presentation commands by time to write an output metadata track.

## Topics

### Initializers
- [init(presentationDescriptor: PresentationDescriptor, isSideloaded: Bool)](presentationdescriptorreader/init(presentationdescriptor:issideloaded:).md)
  Initializes an instance containing the specified presentation descriptor.
### Instance Properties
- [var cameraID: String?](presentationdescriptorreader/cameraid.md)
  The current camera ID string of the ImmersiveCamera that needs to be rendered during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var colorFade: simd_float3](presentationdescriptorreader/colorfade.md)
  The current fade color for color fading of the video frames during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var colorFadeOpacity: Float](presentationdescriptorreader/colorfadeopacity.md)
  The current color fade opacity of the video frames during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var environmentFadeOpacity: Float](presentationdescriptorreader/environmentfadeopacity.md)
  The current opacity of the environment backdrops during playback for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var isShotFlopped: Bool](presentationdescriptorreader/isshotflopped.md)
  The flag to indicate if the video frame needs to be shot flopped (Horizontally flipped) or not for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var isSideloaded: Bool](presentationdescriptorreader/issideloaded.md)
  The flag to indicate if the reader input is sideloaded or is it set during playback.
- [var presentationCommands: [any PresentationCommand]](presentationdescriptorreader/presentationcommands.md)
  All the presentationCommands active for the PTS specified in the last call to [`update(presentationTimeStamp:)`](presentationdescriptorreader/update(presentationtimestamp:).md)
- [var presentationDescriptor: PresentationDescriptor](presentationdescriptorreader/presentationdescriptor.md)
  The presentationDescriptor containing all the presentation commands that need to be processed.
### Instance Methods
- [func outputPresentationCommands(for: CMTime, including: [PresentationCommandType]) -> [any PresentationCommand]?](presentationdescriptorreader/outputpresentationcommands(for:including:).md)
  This function returns all presentation commands to be muxed into an MOV during an AVAssetWriter session. It’s not supposed to be used for playback rendering.
- [func update(presentationTimeStamp: CMTime)](presentationdescriptorreader/update(presentationtimestamp:).md)
  Update is called by the application (e.g. render/playback loop) to update the publishers exported by PresentationDescriptorReader

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Observable](../Observation/Observable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol PresentationCommand](presentationcommand.md)
  A set of properties that define the interface for a presentation command.
- [struct FadeCommand](fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct FadeEnvironmentCommand](fadeenvironmentcommand.md)
  A command type for opacity fading environment backdrops during immersive media playback.
- [struct SetCameraCommand](setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [enum PresentationCommandType](presentationcommandtype.md)
  Values that represent the type of presentation command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptorreader)*