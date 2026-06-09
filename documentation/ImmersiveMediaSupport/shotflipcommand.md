# ShotFlipCommand

**Framework**: Immersive Media Support  
**Kind**: struct

A command type to flip the video frames vertically during playback for the duration of the command.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct ShotFlipCommand
```

## Topics

### Initializers
- [init(from: any Decoder) throws](shotflipcommand/init(from:).md)
- [init(id: Int, time: CMTime, duration: CMTime, offset: CMTime?)](shotflipcommand/init(id:time:duration:offset:).md)
  Creates a command instance for a certain time, duration and offset.
### Instance Properties
- [var duration: CMTime](shotflipcommand/duration.md)
  The duration of the command.
- [var id: Int](shotflipcommand/id.md)
  A unique command ID for the immersive media file.
- [var offset: CMTime?](shotflipcommand/offset.md)
  The offset from the start time of this command.
- [var time: CMTime](shotflipcommand/time.md)
  The time this command starts during playback.
### Instance Methods
- [func encode(to: any Encoder) throws](shotflipcommand/encode(to:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflipcommand)*