# FadeEnvironmentCommand

**Framework**: Immersive Media Support  
**Kind**: struct

A command type for opacity fading environment backdrops during immersive media playback.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct FadeEnvironmentCommand
```

#### Overview

Opacity fade is used to apply requested opacity to the AIV environment backdrops. Fade environment commands can be absolute time based or offset based. If fade commands are absolute time based, then property time dictates the time it needs to start executing and keep fading until the duration property value. On the other hand if they are offset based, then offset property dictates the fade percentage from the start time of the fade command till the duration of the fade. If the fade has to start at time 0.0 second of the playback for duration of 1.0 seconds and if the media FPS is 90, then first frame should be accompanied with presentation metadata with fade command which has 0.011 as offset. Second frame should have fade command with offset 0.022 and so on. For the 90th frame, we should receive offset 1.0.

## Topics

### Initializers
- [init(from: any Decoder) throws](fadeenvironmentcommand/init(from:).md)
  Creates a `FadeEnvironmentCommand` instance from the specified decoder.
- [init(id: Int, time: CMTime, duration: CMTime, direction: FadeEnvironmentCommand.FadeDirection, opacity: Float, offset: CMTime?)](fadeenvironmentcommand/init(id:time:duration:direction:opacity:offset:).md)
  Creates a fade environment command instance.
### Instance Properties
- [var direction: FadeEnvironmentCommand.FadeDirection](fadeenvironmentcommand/direction.md)
  Fade direction for this command instance.
- [var duration: CMTime](fadeenvironmentcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](fadeenvironmentcommand/id.md)
  A unique command ID for the immersive media file.
- [var offset: CMTime?](fadeenvironmentcommand/offset.md)
  The offset from the start time of this command.
- [var opacity: Float](fadeenvironmentcommand/opacity.md)
  The fade opacity value between `0.0` to `1.0`. This value represents the target opacity of the environment backdrops during playback after fading completes.
- [var time: CMTime](fadeenvironmentcommand/time.md)
  The time this command starts during playback.
### Instance Methods
- [func encode(to: any Encoder) throws](fadeenvironmentcommand/encode(to:).md)
  Encodes an instance of fade environment command.
### Enumerations
- [FadeEnvironmentCommand.FadeDirection](fadeenvironmentcommand/fadedirection.md)
  A value that represents the direction of the fade environment command.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum PresentationCommand](presentationcommand.md)
  A set of properties that define the interface for a presentation command.
- [struct FadeCommand](fadecommand.md)
  A command type for color fading during immersive media playback.
- [struct SetCameraCommand](setcameracommand.md)
  A command type for immersive camera switching during playback.
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadeenvironmentcommand)*