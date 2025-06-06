# isSkipBackwardEnabled

**Framework**: AVKit  
**Kind**: property

A Boolean value that indicates whether backward-skipping is available.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
@MainActor
var isSkipBackwardEnabled: Bool { get set }
```

#### Discussion

This property affects the appearance of the backward-skipping indicator. The value you set for the player view controller’s [`skippingBehavior`](avplayerviewcontroller/skippingbehavior.md) property determines its backward-skipping behavior.

## See Also

- [var isSkipForwardEnabled: Bool](avplayerviewcontroller/isskipforwardenabled.md)
  A Boolean value that indicates whether forward-skipping is available.
- [var skippingBehavior: AVPlayerViewControllerSkippingBehavior](avplayerviewcontroller/skippingbehavior.md)
  The behavior that skipping gestures perform.
- [enum AVPlayerViewControllerSkippingBehavior](avplayerviewcontrollerskippingbehavior.md)
  Constants that represent the player view controller’s skipping behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/isskipbackwardenabled)*