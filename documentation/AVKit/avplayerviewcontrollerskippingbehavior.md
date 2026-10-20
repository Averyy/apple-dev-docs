# AVPlayerViewControllerSkippingBehavior

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the player view controller’s skipping behavior.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
enum AVPlayerViewControllerSkippingBehavior
```

```c
enum AVPlayerViewControllerSkippingBehavior : NSInteger;
```

## Topics

### Creating a skipping behavior
- [init?(rawValue: Int)](./avplayerviewcontrollerskippingbehavior/init%28rawvalue%29.md)
### Skipping behaviors
- [AVPlayerViewControllerSkippingBehavior.default](./avplayerviewcontrollerskippingbehavior/default.md)
  The default skipping behavior, which is to skip forward or backward in 10-second intervals.
- [AVPlayerViewControllerSkippingBehavior.skipItem](./avplayerviewcontrollerskippingbehavior/skipitem.md)
  Skipping behavior that specifies skipping to the next or previous item in the player’s playlist.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Configuring skipping behavior
- [var isSkipForwardEnabled: Bool](./avplayerviewcontroller/isskipforwardenabled.md)
  A Boolean value that indicates whether forward-skipping is available.
- [var isSkipBackwardEnabled: Bool](./avplayerviewcontroller/isskipbackwardenabled.md)
  A Boolean value that indicates whether backward-skipping is available.
- [var skippingBehavior: AVPlayerViewControllerSkippingBehavior](./avplayerviewcontroller/skippingbehavior.md)
  The behavior that skipping gestures perform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerskippingbehavior)*