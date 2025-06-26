# PresentationCommand

**Framework**: Immersive Media Support  
**Kind**: enum

A set of properties that define the interface for a presentation command.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
  A value representing a command that is used during scene transitions. This command adds a fade in / fade out during playback.
- [case fadeEnvironment(FadeEnvironmentCommand)](presentationcommand/fadeenvironment(_:).md)
  A value representing a command that is used during backdrop transitions. This command adds a fade in / fade out for the backdrop during playback.
- [PresentationCommand.setCamera(_:)](presentationcommand/setcamera(_:).md)
  A value representing a command that specifies the camera ID to be used for a specific frame during playback.
- [PresentationCommand.shotFlop(_:)](presentationcommand/shotflop(_:).md)
  A value representing a command that causes the whole frame to be mirrored horizontally for the duration of the command.
### Initializers
- [init(from: any Decoder) throws](presentationcommand/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](presentationcommand/encode(to:).md)
  Encodes this value into the given encoder.

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