# AVPlayer.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Status values that indicate whether a player can successfully play media.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum Status
```

```c
enum AVPlayerStatus : NSInteger;
```

## Topics

### Status values
- [AVPlayer.Status.unknown](./status-swift.enum/unknown.md)
  A value that indicates a player hasn’t attempted to load media for playback.
- [AVPlayer.Status.readyToPlay](./status-swift.enum/readytoplay.md)
  A value that indicates the player is ready to media.
- [AVPlayer.Status.failed](./status-swift.enum/failed.md)
  A value that indicates the player can no longer play media due to an error.
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

### Determining player readiness
- [var status: AVPlayer.Status](./status-swift.property.md)
  A value that indicates the readiness of a player object for playback.
- [var error: (any Error)?](./error.md)
  An error that caused a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/status-swift.enum)*