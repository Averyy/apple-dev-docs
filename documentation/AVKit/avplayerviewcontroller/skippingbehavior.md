# skippingBehavior

**Framework**: AVKit  
**Kind**: property  
**Role**: Instance Property

The behavior that skipping gestures perform.

**Availability**:
- tvOS 10.0+

## Declaration

```swift
var skippingBehavior: AVPlayerViewControllerSkippingBehavior { get set }
```

```objc
@property (nonatomic) AVPlayerViewControllerSkippingBehavior skippingBehavior;
```

#### Discussion

This property lets you override the default skipping behavior in tvOS, which is to skip forward or backward 10 seconds when a user presses the right or left sides, respectively, of the Touch surface on the Siri Remote.

## See Also

### Configuring skipping behavior
- [var isSkipForwardEnabled: Bool](./isskipforwardenabled.md)
  A Boolean value that indicates whether forward-skipping is available.
- [var isSkipBackwardEnabled: Bool](./isskipbackwardenabled.md)
  A Boolean value that indicates whether backward-skipping is available.
- [enum AVPlayerViewControllerSkippingBehavior](../avplayerviewcontrollerskippingbehavior.md)
  Constants that represent the player view controller’s skipping behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontroller/skippingbehavior)*