# AVPlayerLooper.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Status constants that indicate whether a looper can successfully perform looping playback.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum Status
```

```c
enum AVPlayerLooperStatus : NSInteger;
```

## Topics

### Status values
- [AVPlayerLooper.Status.unknown](./status-swift.enum/unknown.md)
  The status isn’t known.
- [AVPlayerLooper.Status.ready](./status-swift.enum/ready.md)
  The looper is ready to perform looping playback.
- [AVPlayerLooper.Status.failed](./status-swift.enum/failed.md)
  The looper isn’t able to perform looping playback due to an error.
- [AVPlayerLooper.Status.cancelled](./status-swift.enum/cancelled.md)
  The app canceled looping on the player.
### Initializers
- [init?(rawValue: Int)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Observing looping state
- [var loopCount: Int](./loopcount.md)
  The number of times the object played the media.
- [var status: AVPlayerLooper.Status](./status-swift.property.md)
  A status that indicates the object’s ability to loop playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum)*