# status

**Framework**: AVFoundation  
**Kind**: property

A status that indicates the object’s ability to loop playback.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var status: AVPlayerLooper.Status { get }
```

#### Discussion

When the value of this property is [`AVPlayerLooper.Status.failed`](avplayerlooper/status-swift.enum/failed.md) or [`AVPlayerLooper.Status.cancelled`](avplayerlooper/status-swift.enum/cancelled.md), you can no longer use the looper for playback. You need to create a new instance to begin looping again.

This property is key-value observable.

## See Also

- [var loopCount: Int](avplayerlooper/loopcount.md)
  The number of times the object played the media.
- [AVPlayerLooper.Status](avplayerlooper/status-swift.enum.md)
  Status constants that indicate whether a looper can successfully perform looping playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.property)*