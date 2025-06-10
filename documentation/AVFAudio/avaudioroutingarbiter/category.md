# AVAudioRoutingArbiter.Category

**Framework**: AVFAudio  
**Kind**: enum

Categories that describe the general nature of your app’s audio use.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum Category
```

#### Overview

The category provides context that helps the operating system arbitrate between Apple devices that are trying to take ownership of a Bluetooth audio route.

## Topics

### Categories
- [AVAudioRoutingArbiter.Category.playback](avaudioroutingarbiter/category/playback.md)
  The app plays audio.
- [AVAudioRoutingArbiter.Category.playAndRecord](avaudioroutingarbiter/category/playandrecord.md)
  The app plays and records audio.
- [AVAudioRoutingArbiter.Category.playAndRecordVoice](avaudioroutingarbiter/category/playandrecordvoice.md)
  The app uses Voice over IP (VoIP).
### Initializers
- [init?(rawValue: Int)](avaudioroutingarbiter/category/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func begin(category: AVAudioRoutingArbiter.Category, completionHandler: (Bool, (any Error)?) -> Void)](avaudioroutingarbiter/begin(category:completionhandler:).md)
  Begins routing arbitration to take ownership of a nearby Bluetooth audio route.
- [func leave()](avaudioroutingarbiter/leave.md)
  Stops an app’s participation in audio routing arbitration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioroutingarbiter/category)*