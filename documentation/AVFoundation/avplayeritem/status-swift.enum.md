# AVPlayerItem.Status

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

The statuses for a player item.

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
enum AVPlayerItemStatus : NSInteger;
```

## Topics

### Player item statuses
- [AVPlayerItem.Status.unknown](./status-swift.enum/unknown.md)
  The item’s status is unknown.
- [AVPlayerItem.Status.readyToPlay](./status-swift.enum/readytoplay.md)
  The item is ready to play.
- [AVPlayerItem.Status.failed](./status-swift.enum/failed.md)
  The item no longer plays due to an error.
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

### Determining readiness
- [var status: AVPlayerItem.Status](./status-swift.property.md)
  The status of the player item.
- [var error: (any Error)?](./error.md)
  The error that caused the player item to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/status-swift.enum)*