# AVPlayerViewControllerSkippingBehavior

**Framework**: AVKit  
**Kind**: enum

Constants that represent the player view controller’s skipping behavior.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
enum AVPlayerViewControllerSkippingBehavior
```

## Topics

### Skipping Behaviors
- [AVPlayerViewControllerSkippingBehavior.default](avplayerviewcontrollerskippingbehavior/default.md)
  The default skipping behavior, which is to skip forward or backward in 10-second intervals.
- [AVPlayerViewControllerSkippingBehavior.skipItem](avplayerviewcontrollerskippingbehavior/skipitem.md)
  Skipping behavior that specifies skipping to the next or previous item in the player’s playlist.
### Initializers
- [init?(rawValue: Int)](avplayerviewcontrollerskippingbehavior/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isSkipForwardEnabled: Bool](avplayerviewcontroller/isskipforwardenabled.md)
  A Boolean value that indicates whether forward-skipping is available.
- [var isSkipBackwardEnabled: Bool](avplayerviewcontroller/isskipbackwardenabled.md)
  A Boolean value that indicates whether backward-skipping is available.
- [var skippingBehavior: AVPlayerViewControllerSkippingBehavior](avplayerviewcontroller/skippingbehavior.md)
  The behavior that skipping gestures perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerskippingbehavior)*