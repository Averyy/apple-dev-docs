# PresentationCommand

**Framework**: Immersive Media Support  
**Kind**: protocol

A set of properties that define the interface for a presentation command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
protocol PresentationCommand : Decodable, Encodable, Sendable
```

#### Overview

These are commands that dictate part of the presentation of the video frames during immersive media playback. These commands have all the necessary properties like command identifier, command type, command time in seconds (when it needs to be processed), command duration in seconds, command offset from the start of the command time (if they are offset based), a flag to indicate if commands are offset based or not, command argument list, which might carry additional properties based on the type of the presentation command.

## Topics

### Instance Properties
- [var duration: CMTime](presentationcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](presentationcommand/id.md)
  An unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](presentationcommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var time: CMTime](presentationcommand/time.md)
  The time this command starts during playback.
- [var type: PresentationCommandType](presentationcommand/type.md)
  The command type. See [`PresentationCommandType`](presentationcommandtype.md) for the current set of valid command types.

## Relationships

### Inherits From
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [FadeCommand](fadecommand.md)
- [FadeEnvironmentCommand](fadeenvironmentcommand.md)
- [SetCameraCommand](setcameracommand.md)
- [ShotFlopCommand](shotflopcommand.md)

## See Also

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
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationcommand)*