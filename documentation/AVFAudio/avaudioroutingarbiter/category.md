# AVAudioRoutingArbiter.Category

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Categories that describe the general nature of your app’s audio use.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum Category
```

```c
enum AVAudioRoutingArbitrationCategory : NSInteger;
```

## Overview

The category provides context that helps the operating system arbitrate between Apple devices that are trying to take ownership of a Bluetooth audio route.

## Topics

### Creating a category
- [init?(rawValue: Int)](./category/init%28rawvalue%29.md)
### Choosing an arbitration category
- [AVAudioRoutingArbiter.Category.playback](./category/playback.md)
  The app plays audio.
- [AVAudioRoutingArbiter.Category.playAndRecord](./category/playandrecord.md)
  The app plays and records audio.
- [AVAudioRoutingArbiter.Category.playAndRecordVoice](./category/playandrecordvoice.md)
  The app uses Voice over IP (VoIP).

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Joining AirPods automatic switching
- [func begin(category: AVAudioRoutingArbiter.Category, completionHandler: (Bool, (any Error)?) -> Void)](./begin%28category,completionhandler%29.md)
  Begins routing arbitration to take ownership of a nearby Bluetooth audio route.
- [func leave()](./leave%28%29.md)
  Stops an app’s participation in audio routing arbitration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudioroutingarbiter/category)*