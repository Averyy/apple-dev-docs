# playerViewControllerWillBeginDismissalTransition(_:)

**Framework**: AVKit  
**Kind**: method

Tells the delegate when the player view controller is about to start its dismissal transition.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
optional func playerViewControllerWillBeginDismissalTransition(_ playerViewController: AVPlayerViewController)
```

## Parameters

- `playerViewController`: The player view controller.

## See Also

- [func playerViewControllerShouldDismiss(AVPlayerViewController) -> Bool](avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss(_:).md)
  Asks the delegate object whether the player view controller dismisses itself upon request.
- [func playerViewControllerDidEndDismissalTransition(AVPlayerViewController)](avplayerviewcontrollerdelegate/playerviewcontrollerdidenddismissaltransition(_:).md)
  Tells the delegate when the player view controller ends its dismissal transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillbegindismissaltransition(_:))*