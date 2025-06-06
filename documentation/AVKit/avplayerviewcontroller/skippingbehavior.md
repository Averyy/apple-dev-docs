# skippingBehavior

**Framework**: AVKit  
**Kind**: property

The behavior that skipping gestures perform.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
var skippingBehavior: AVPlayerViewControllerSkippingBehavior { get set }
```

#### Discussion

This property lets you override the default skipping behavior in tvOS, which is to skip forward or backward 10 seconds when a user presses the right or left sides, respectively, of the Touch surface on the Siri Remote.

## See Also

- [var isSkipForwardEnabled: Bool](avplayerviewcontroller/isskipforwardenabled.md)
  A Boolean value that indicates whether forward-skipping is available.
- [var isSkipBackwardEnabled: Bool](avplayerviewcontroller/isskipbackwardenabled.md)
  A Boolean value that indicates whether backward-skipping is available.
- [enum AVPlayerViewControllerSkippingBehavior](avplayerviewcontrollerskippingbehavior.md)
  Constants that represent the player view controller’s skipping behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/skippingbehavior)*