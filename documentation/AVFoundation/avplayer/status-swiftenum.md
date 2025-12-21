# AVPlayer.Status

**Framework**: AVFoundation  
**Kind**: enum

Status values that indicate whether a player can successfully play media.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum Status
```

## Topics

### Status values
- [AVPlayer.Status.unknown](avplayer/status-swift.enum/unknown.md)
  A value that indicates a player hasn’t attempted to load media for playback.
- [AVPlayer.Status.readyToPlay](avplayer/status-swift.enum/readytoplay.md)
  A value that indicates the player is ready to media.
- [AVPlayer.Status.failed](avplayer/status-swift.enum/failed.md)
  A value that indicates the player can no longer play media due to an error.
### Initializers
- [init?(rawValue: Int)](avplayer/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var status: AVPlayer.Status](avplayer/status-swift.property.md)
  A value that indicates the readiness of a player object for playback.
- [var error: (any Error)?](avplayer/error.md)
  An error that caused a failure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/status-swift.enum)*