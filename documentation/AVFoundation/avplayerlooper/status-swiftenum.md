# AVPlayerLooper.Status

**Framework**: AVFoundation  
**Kind**: enum

Status constants that indicate whether a looper can successfully perform looping playback.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum Status
```

## Topics

### Status Values
- [AVPlayerLooper.Status.unknown](avplayerlooper/status-swift.enum/unknown.md)
  The status isn’t known.
- [AVPlayerLooper.Status.ready](avplayerlooper/status-swift.enum/ready.md)
  The looper is ready to perform looping playback.
- [AVPlayerLooper.Status.failed](avplayerlooper/status-swift.enum/failed.md)
  The looper isn’t able to perform looping playback due to an error.
- [AVPlayerLooper.Status.cancelled](avplayerlooper/status-swift.enum/cancelled.md)
  The app canceled looping on the player.
### Initializers
- [init?(rawValue: Int)](avplayerlooper/status-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var loopCount: Int](avplayerlooper/loopcount.md)
  The number of times the object played the media.
- [var status: AVPlayerLooper.Status](avplayerlooper/status-swift.property.md)
  A status that indicates the object’s ability to loop playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum)*