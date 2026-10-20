# AVAudioSession.Orientation

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Constants that indicate the directions in which a data source can point, relative to the device’s natural orientation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct Orientation
```

```c
typedef NSString * AVAudioSessionOrientation;
```

## Topics

### Creating an orientation
- [init(rawValue: String)](./orientation/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting standard orientations
- [static let top: AVAudioSession.Orientation](./orientation/top.md)
  A data source that points upward.
- [static let bottom: AVAudioSession.Orientation](./orientation/bottom.md)
  A data source that points downward.
- [static let front: AVAudioSession.Orientation](./orientation/front.md)
  A data source that points outward from the front of the device, toward the user.
- [static let back: AVAudioSession.Orientation](./orientation/back.md)
  A data source that points outward from the back of the device, away from the user.
- [static let left: AVAudioSession.Orientation](./orientation/left.md)
  A data source that points outward to the left of the device, away from the user.
- [static let right: AVAudioSession.Orientation](./orientation/right.md)
  A data source that points outward to the right of the device, away from the user.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Retrieving the data source orientation
- [var orientation: AVAudioSession.Orientation?](../avaudiosessiondatasourcedescription/orientation.md)
  The orientation of the data source relative to the device’s natural orientation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/orientation)*