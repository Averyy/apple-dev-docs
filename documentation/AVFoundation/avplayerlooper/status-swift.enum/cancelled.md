# AVPlayerLooper.Status.cancelled

**Framework**: AVFoundation  
**Kind**: case  
**Role**: Case

The app canceled looping on the player.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case cancelled
```

```c
AVPlayerLooperStatusCancelled
```

#### Discussion

The system sets this status after you call the [`disableLooping()`](../disablelooping%28%29.md) method.

## See Also

### Status values
- [AVPlayerLooper.Status.unknown](./unknown.md)
  The status isn’t known.
- [AVPlayerLooper.Status.ready](./ready.md)
  The looper is ready to perform looping playback.
- [AVPlayerLooper.Status.failed](./failed.md)
  The looper isn’t able to perform looping playback due to an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.enum/cancelled)*