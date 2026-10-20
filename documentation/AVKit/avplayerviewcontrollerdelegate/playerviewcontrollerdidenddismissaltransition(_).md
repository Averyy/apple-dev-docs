# playerViewControllerDidEndDismissalTransition(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Tells the delegate when the player view controller ends its dismissal transition.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
optional func playerViewControllerDidEndDismissalTransition(_ playerViewController: AVPlayerViewController)
```

```objc
- (void) playerViewControllerDidEndDismissalTransition:(AVPlayerViewController *) playerViewController;
```

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Dismissing the player view controller
- [func playerViewControllerShouldDismiss(AVPlayerViewController) -> Bool](./playerviewcontrollershoulddismiss%28_%29.md)
  Asks the delegate object whether the player view controller dismisses itself upon request.
- [func playerViewControllerWillBeginDismissalTransition(AVPlayerViewController)](./playerviewcontrollerwillbegindismissaltransition%28_%29.md)
  Tells the delegate when the player view controller is about to start its dismissal transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition(_:))*