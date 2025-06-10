# AVAudioSession.Orientation

**Framework**: AVFAudio  
**Kind**: struct

Constants that indicate the directions in which a data source can point, relative to the device’s natural orientation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct Orientation
```

## Topics

### Creating an Orientation
- [init(rawValue: String)](avaudiosession/orientation/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard Orientations
- [static let top: AVAudioSession.Orientation](avaudiosession/orientation/top.md)
  A data source that points upward.
- [static let bottom: AVAudioSession.Orientation](avaudiosession/orientation/bottom.md)
  A data source that points downward.
- [static let front: AVAudioSession.Orientation](avaudiosession/orientation/front.md)
  A data source that points outward from the front of the device, toward the user.
- [static let back: AVAudioSession.Orientation](avaudiosession/orientation/back.md)
  A data source that points outward from the back of the device, away from the user.
- [static let left: AVAudioSession.Orientation](avaudiosession/orientation/left.md)
  A data source that points outward to the left of the device, away from the user.
- [static let right: AVAudioSession.Orientation](avaudiosession/orientation/right.md)
  A data source that points outward to the right of the device, away from the user.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var orientation: AVAudioSession.Orientation?](avaudiosessiondatasourcedescription/orientation.md)
  The orientation of the data source relative to the device’s natural orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/orientation)*