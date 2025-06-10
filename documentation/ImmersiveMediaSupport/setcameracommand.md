# SetCameraCommand

**Framework**: Immersive Media Support  
**Kind**: struct

A command type for immersive camera switching during playback.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct SetCameraCommand
```

#### Overview

The property `cameraID` has been added to this type to hold camera identifier string, so that we can switch from one immersive camera to another using these camera identifiers.

## Topics

### Initializers
- [init(from: any Decoder) throws](setcameracommand/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(time: CMTime, cameraID: String)](setcameracommand/init(time:cameraid:).md)
  Initializes a setCamera command with a specific cameraID and start time.
### Instance Properties
- [var cameraID: String](setcameracommand/cameraid.md)
  The cameraID to be used for the duration of this command.
- [var duration: CMTime](setcameracommand/duration.md)
  The duration of the command - this can be .zero if the command has no duration
- [var id: Int](setcameracommand/id.md)
  An unique command id. Ids should be unique for the whole Immersive Media file.
- [var offset: CMTime?](setcameracommand/offset.md)
  Not used - setCamera commands don’t use offsets.
- [var time: CMTime](setcameracommand/time.md)
  The time this command starts during playback.
- [var type: PresentationCommandType](setcameracommand/type.md)
  The command type (.setCamera).
### Instance Methods
- [func encode(to: any Encoder) throws](setcameracommand/encode(to:).md)
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
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [enum PresentationCommandType](presentationcommandtype.md)
  Values that represent the type of presentation command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand)*