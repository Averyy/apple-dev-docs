# ShotFlopCommand

**Framework**: Immersive Media Support  
**Kind**: struct

A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct ShotFlopCommand
```

## Topics

### Initializers
- [init(from: any Decoder) throws](shotflopcommand/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(time: CMTime, duration: CMTime, offset: CMTime?)](shotflopcommand/init(time:duration:offset:).md)
  Initializes a shotFlop command for a certain time, duration and offset.
### Instance Properties
- [var duration: CMTime](shotflopcommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](shotflopcommand/id.md)
  An unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](shotflopcommand/offset.md)
  Some commands control animations by repeating the command for the whole duration, and specifying the offset of the animation from the start time of this presentation command.
- [var time: CMTime](shotflopcommand/time.md)
  The time this command starts during playback.
- [var type: PresentationCommandType](shotflopcommand/type.md)
  The command type (.shotFlop).
### Instance Methods
- [func encode(to: any Encoder) throws](shotflopcommand/encode(to:).md)
  Encodes this value into the given encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [PresentationCommand](presentationcommand.md)
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
- [enum PresentationCommandType](presentationcommandtype.md)
  Values that represent the type of presentation command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/shotflopcommand)*