# AVPlayerLooper.Status.failed

**Framework**: AVFoundation  
**Kind**: case

The looper isn’t able to perform looping playback due to an error.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case failed
```

#### Discussion

Examine the looper’s [`error`](avplayerlooper/error.md) property to determine the cause of the failure.

## See Also

- [AVPlayerLooper.Status.unknown](avplayerlooper/status-swift.enum/unknown.md)
  The status isn’t known.
- [AVPlayerLooper.Status.ready](avplayerlooper/status-swift.enum/ready.md)
  The looper is ready to perform looping playback.
- [AVPlayerLooper.Status.cancelled](avplayerlooper/status-swift.enum/cancelled.md)
  The app canceled looping on the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum/failed)*