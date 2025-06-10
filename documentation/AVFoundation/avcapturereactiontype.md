# AVCaptureReactionType

**Framework**: AVFoundation  
**Kind**: struct

Constants that indicate the type of reaction that an effect can perform.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
struct AVCaptureReactionType
```

## Topics

### Reaction types
- [static let balloons: AVCaptureReactionType](avcapturereactiontype/balloons.md)
  A reaction that displays balloons rising through the scene.
- [static let confetti: AVCaptureReactionType](avcapturereactiontype/confetti.md)
  A reaction that displays festive spots of color falling through the scene.
- [static let fireworks: AVCaptureReactionType](avcapturereactiontype/fireworks.md)
  A reaction that displays fireworks bursting in the background.
- [static let heart: AVCaptureReactionType](avcapturereactiontype/heart.md)
  A reaction that displays one or more heart symbols.
- [static let lasers: AVCaptureReactionType](avcapturereactiontype/lasers.md)
  A reaction that displays a bright laser show projecting into the scene.
- [static let rain: AVCaptureReactionType](avcapturereactiontype/rain.md)
  A reaction that displays a dark and stormy night.
- [static let thumbsUp: AVCaptureReactionType](avcapturereactiontype/thumbsup.md)
  A reaction that displays a thumbs-up symbol.
- [static let thumbsDown: AVCaptureReactionType](avcapturereactiontype/thumbsdown.md)
  A reaction that displays a thumbs-down symbol.
### Accessing the system image name
- [var systemImageName: String](avcapturereactiontype/systemimagename.md)
  Returns the name of a system image that displays the recommended iconography for a specified reaction type.
### Initializers
- [init(rawValue: String)](avcapturereactiontype/init(rawvalue:).md)
  Creates a reaction type with a string value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var reactionType: AVCaptureReactionType](avcapturereactioneffectstate/reactiontype.md)
  The type of reaction.
- [var startTime: CMTime](avcapturereactioneffectstate/starttime.md)
  The presentation time of the first frame where the system renders the effect.
- [var endTime: CMTime](avcapturereactioneffectstate/endtime.md)
  The presentation time of the first frame following the end of a reaction effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturereactiontype)*