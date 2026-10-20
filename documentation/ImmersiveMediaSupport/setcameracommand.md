# SetCameraCommand

**Framework**: Immersive Media Support  
**Kind**: struct  
**Role**: Structure

A command type for immersive camera switching during playback.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
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
- [init(from: any Decoder) throws](./setcameracommand/init%28from%29.md)
- [init(id: Int, time: CMTime, cameraID: String)](./setcameracommand/init%28id,time,cameraid%29.md)
  Creates a command with a specific ID, cameraID and start time.
- [init(id: Int, time: CMTime, cameraID: String, overrides: SetCameraCommand.Overrides?)](./setcameracommand/init%28id,time,cameraid,overrides%29.md)
  Creates a command with a specific ID, cameraID, start time and override parameters.
### Instance Properties
- [var cameraID: String](./setcameracommand/cameraid.md)
  The camera ID to use for the duration of this command.
- [var duration: CMTime](./setcameracommand/duration.md)
  The duration of the command.
- [var id: Int](./setcameracommand/id.md)
  A unique command ID for the entire immersive media file.
- [var offset: CMTime?](./setcameracommand/offset.md)
  Reserved for later use.
- [var time: CMTime](./setcameracommand/time.md)
  The time this command starts during playback.
- [var overrides: SetCameraCommand.Overrides?](./setcameracommand/overrides-swift.property.md)
  The override parameters for the camera.
### Instance Methods
- [func encode(to: any Encoder) throws](./setcameracommand/encode%28to%29.md)
### Structures
- [SetCameraCommand.Overrides](./setcameracommand/overrides-swift.struct.md)
  Override camera/venue params

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
- [struct ShotFlopCommand](./shotflopcommand.md)
  A command type to flip the video frames horizontally (mirrored horizontally) during playback for the duration of the command.
- [struct ShotFlipCommand](./shotflipcommand.md)
  A command type to flip the video frames vertically during playback for the duration of the command.
- [struct PresentationDescriptor](./presentationdescriptor.md)
  A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.
- [class PresentationDescriptorReader](./presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/setcameracommand)*