# error

**Framework**: AVFoundation  
**Kind**: property

The error that caused the player item to fail.

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

The value of this property is an error that describes what caused the player item to no longer be able to be played.

If the receiver’s status is not [`AVPlayerItem.Status.failed`](avplayeritem/status-swift.enum/failed.md), the value of this property is `nil`.

## See Also

- [var status: AVPlayerItem.Status](avplayeritem/status-swift.property.md)
  The status of the player item.
- [AVPlayerItem.Status](avplayeritem/status-swift.enum.md)
  The statuses for a player item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/error)*