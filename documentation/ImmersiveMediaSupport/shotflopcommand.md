# ShotFlopCommand

**Framework**: Immersive Media Support  
**Kind**: struct  
**Role**: Structure

A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct ShotFlopCommand
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./shotflopcommand/init%28from%29.md)
- [init(id: Int, time: CMTime, duration: CMTime, offset: CMTime?)](./shotflopcommand/init%28id,time,duration,offset%29.md)
  Creates a command instance for a certain time, duration and offset.
### Instance Properties
- [var duration: CMTime](./shotflopcommand/duration.md)
  The duration of the command.
- [var id: Int](./shotflopcommand/id.md)
  A unique command ID for the immersive media file.
- [var offset: CMTime?](./shotflopcommand/offset.md)
  The offset from the start time of this command.
- [var time: CMTime](./shotflopcommand/time.md)
  The time this command starts during playback.
### Instance Methods
- [func encode(to: any Encoder) throws](./shotflopcommand/encode%28to%29.md)

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Presentation commands
- [enum PresentationCommand](./presentationcommand.md)
  A set of properties that define the interface for a presentation command.
- [struct FadeCommand](./fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct FadeEnvironmentCommand](./fadeenvironmentcommand.md)
  A command type for opacity fading environment backdrops during immersive media playback.
- [struct SetCameraCommand](./setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlipCommand](./shotflipcommand.md)
  A command type to flip the video frames vertically during playback for the duration of the command.
- [struct PresentationDescriptor](./presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](./presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflopcommand)*