# FadeCommand

**Framework**: Immersive Media Support  
**Kind**: struct

A command type for color fading during immersive media playback.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct FadeCommand
```

#### Overview

Color fades are used to either fading in into the video frame from the requested color or fading out of the video frame to the requested color. The fade commands are usually used for fading in at the start of the playback and fading out at the end of the playback. These commands are also used during immersive camera view switches during the playback.

Fade commands can be absolute time based or offset based. If fade commands are absolute time based, then property time dictates the time it needs to start executing and keep fading until the duration property value. On the other hand if they are offset based, then offset property dictates the fade percentage from the start time of the fade command till the duration of the fade. If the fade has to start at time 0.0 second of the playback for duration of 1.0 seconds and if the media FPS is 90, then first frame should be accompanied with presentation metadata with fade command which has 0.011 as offset. Second frame should have fade command with offset 0.022 and so on. For the 90th frame, we should receive offset 1.0.

## Topics

### Initializers
- [init(from: any Decoder) throws](fadecommand/init(from:).md)
- [init(id: Int, time: CMTime, duration: CMTime, direction: FadeCommand.FadeDirection, color: simd_float3, offset: CMTime?)](fadecommand/init(id:time:duration:direction:color:offset:).md)
  Initializes a color fade command.
### Instance Properties
- [var color: simd_float3?](fadecommand/color.md)
  The fade color value between 0.0 to 1.0 for each color channel. If color is set to black, and the direction is `in`, then it fades from black color to the video frame.
- [var direction: FadeCommand.FadeDirection](fadecommand/direction.md)
  Fade direction for this command instance.
- [var duration: CMTime](fadecommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](fadecommand/id.md)
  A unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](fadecommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var time: CMTime](fadecommand/time.md)
  The time this command starts during playback.
### Instance Methods
- [func encode(to: any Encoder) throws](fadecommand/encode(to:).md)
### Enumerations
- [FadeCommand.FadeDirection](fadecommand/fadedirection.md)
  A value representing the direction of the fade command.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [enum PresentationCommand](presentationcommand.md)
  A set of properties that define the interface for a presentation command.
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

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/fadecommand)*