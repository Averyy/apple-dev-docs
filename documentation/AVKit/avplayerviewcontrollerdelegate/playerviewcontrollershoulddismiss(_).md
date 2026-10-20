# playerViewControllerShouldDismiss(_:)

**Framework**: AVKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate object whether the player view controller dismisses itself upon request.

**Availability**:
- tvOS 11.0+

## Declaration

```swift
optional func playerViewControllerShouldDismiss(_ playerViewController: AVPlayerViewController) -> Bool
```

```objc
- (BOOL) playerViewControllerShouldDismiss:(AVPlayerViewController *) playerViewController;
```

#### Return Value

`true` if the player view controller should dismiss itself; otherwise `false`.

#### Discussion

If allowed, the player view controller dismisses itself with animation. If you’ve embedded the player view controller in another view, the delegate may need to manually dismiss the view controller.

## Parameters

- `playerViewController`: The player view controller.

## See Also

### Dismissing the player view controller
- [func playerViewControllerWillBeginDismissalTransition(AVPlayerViewController)](./playerviewcontrollerwillbegindismissaltransition%28_%29.md)
  Tells the delegate when the player view controller is about to start its dismissal transition.
- [func playerViewControllerDidEndDismissalTransition(AVPlayerViewController)](./playerviewcontrollerdidenddismissaltransition%28_%29.md)
  Tells the delegate when the player view controller ends its dismissal transition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershoulddismiss(_:))*