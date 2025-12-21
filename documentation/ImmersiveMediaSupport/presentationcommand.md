# PresentationCommand

**Framework**: Immersive Media Support  
**Kind**: enum

A set of properties that define the interface for a presentation command.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum PresentationCommand
```

#### Overview

These are commands that dictate part of the presentation of the video frames during immersive media playback. These commands have all the necessary properties like command identifier, command type, command time in seconds (when it needs to be processed), command duration in seconds, command offset from the start of the command time (if they are offset based), a flag to indicate if commands are offset based or not, command argument list, which might carry additional properties based on the type of the presentation command.

## Topics

### Instance Properties
- [var duration: CMTime](presentationcommand/duration.md)
- [var id: Int](presentationcommand/id.md)
- [var offset: CMTime?](presentationcommand/offset.md)
- [var time: CMTime](presentationcommand/time.md)
### Enumeration Cases
- [PresentationCommand.fade(_:)](presentationcommand/fade(_:).md)
  A value that represents a command that adds fade-in and fade-out effects during scene transitions.
- [case fadeEnvironment(FadeEnvironmentCommand)](presentationcommand/fadeenvironment(_:).md)
  A value that represents a command that adds fade-in and fade-out effects to backdrop transitions.
- [PresentationCommand.setCamera(_:)](presentationcommand/setcamera(_:).md)
  A value that represents a command that specifies the camera ID for a specific frame during playback.
- [PresentationCommand.shotFlop(_:)](presentationcommand/shotflop(_:).md)
  A value that represents a command that mirrors a whole frame horizontally for the duration of the command.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct FadeCommand](fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct FadeEnvironmentCommand](fadeenvironmentcommand.md)
  A command type for opacity fading environment backdrops during immersive media playback.
- [struct SetCameraCommand](setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationcommand)*