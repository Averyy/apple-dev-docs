# PresentationDescriptor

**Framework**: Immersive Media Support  
**Kind**: struct

A structure that represents dynamic metadata used during playback or when outputting the metadata track for an immersive video file.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct PresentationDescriptor
```

## Topics

### Initializers
- [init(commands: [PresentationCommand])](presentationdescriptor/init(commands:).md)
  Creates an instance containing the commands specified in the given array
- [init(duration: CMTime?, commands: [PresentationCommand])](presentationdescriptor/init(duration:commands:).md)
  Creates an instance containing the commands specified in the array
### Instance Properties
- [var commands: [PresentationCommand]](presentationdescriptor/commands.md)
  An array of presentation commands that needs to be processed for the `duration` time.
- [var duration: CMTime?](presentationdescriptor/duration.md)
  The total duration for which the presentation commands needs to be processed.

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
- [class PresentationDescriptorReader](presentationdescriptorreader.md)
  An object that provides the functionality required to understand and process immersive presentation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/presentationdescriptor)*