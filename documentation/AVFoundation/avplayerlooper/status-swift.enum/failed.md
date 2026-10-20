# AVPlayerLooper.Status.failed

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The looper isn’t able to perform looping playback due to an error.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case failed
```

```c
AVPlayerLooperStatusFailed
```

#### Discussion

Examine the looper’s [`error`](../error.md) property to determine the cause of the failure.

## See Also

### Status values
- [AVPlayerLooper.Status.unknown](./unknown.md)
  The status isn’t known.
- [AVPlayerLooper.Status.ready](./ready.md)
  The looper is ready to perform looping playback.
- [AVPlayerLooper.Status.cancelled](./cancelled.md)
  The app canceled looping on the player.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum/failed)*