# error

**Framework**: AVFoundation  
**Kind**: property

An error that caused a failure.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
var error: (any Error)? { get }
```

#### Discussion

By default, this value is `nil`. If a player reaches a [`AVPlayer.Status.failed`](avplayer/status-swift.enum/failed.md), the system populates this value with an error that describes the failure.

## See Also

- [var status: AVPlayer.Status](avplayer/status-swift.property.md)
  A value that indicates the readiness of a player object for playback.
- [AVPlayer.Status](avplayer/status-swift.enum.md)
  Status values that indicate whether a player can successfully play media.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayer/error)*