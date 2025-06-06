# AVPlayerLooper.Status.cancelled

**Framework**: AVFoundation  
**Kind**: case

The app canceled looping on the player.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case cancelled
```

#### Discussion

The system sets this status after you call the [`disableLooping()`](avplayerlooper/disablelooping().md) method.

## See Also

- [AVPlayerLooper.Status.unknown](avplayerlooper/status-swift.enum/unknown.md)
  The status isn’t known.
- [AVPlayerLooper.Status.ready](avplayerlooper/status-swift.enum/ready.md)
  The looper is ready to perform looping playback.
- [AVPlayerLooper.Status.failed](avplayerlooper/status-swift.enum/failed.md)
  The looper isn’t able to perform looping playback due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum/cancelled)*