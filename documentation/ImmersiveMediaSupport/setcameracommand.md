# SetCameraCommand

**Framework**: Immersive Media Support  
**Kind**: struct

A command type for immersive camera switching during playback.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct SetCameraCommand
```

#### Overview

The property `cameraID` has been added to this type to hold camera identifier string, so that we can switch from one immersive camera to another using these camera identifiers.

## Topics

### Initializers
- [init(from: any Decoder) throws](setcameracommand/init(from:).md)
- [init(id: Int, time: CMTime, cameraID: String)](setcameracommand/init(id:time:cameraid:).md)
  Creates a command with a specific ID, cameraID and start time.
### Instance Properties
- [var cameraID: String](setcameracommand/cameraid.md)
  The camera ID to use for the duration of this command.
- [var duration: CMTime](setcameracommand/duration.md)
  The duration of the command.
- [var id: Int](setcameracommand/id.md)
  A unique command ID for the entire immersive media file.
- [var offset: CMTime?](setcameracommand/offset.md)
  Reserved for later use.
- [var time: CMTime](setcameracommand/time.md)
  The time this command starts during playback.
### Instance Methods
- [func encode(to: any Encoder) throws](setcameracommand/encode(to:).md)

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
- [struct ShotFlopCommand](shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct PresentationDescriptor](presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand)*