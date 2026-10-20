# presentationControllerShouldDismiss(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate for permission to dismiss the presentation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func presentationControllerShouldDismiss(_ presentationController: UIPresentationController) -> Bool
```

```objc
- (BOOL) presentationControllerShouldDismiss:(UIPresentationController *) presentationController;
```

#### Return Value

[`true`](../../Swift/true.md) to allow the system to dismiss the presentation, [`false`](../../Swift/false.md) to refuse the dismissal.

#### Discussion

The system may call this method at any time. This method isn’t guaranteed to be followed by a call to [`presentationControllerWillDismiss(_:)`](./presentationcontrollerwilldismiss%28_%29.md) or [`presentationControllerDidDismiss(_:)`](./presentationcontrollerdiddismiss%28_%29.md). Make sure that your implementation of this method returns quickly.

## Parameters

- `presentationController`: The presentation controller that manages the adaptivity change.

## See Also

### Related Documentation
- [Disabling the pull-down gesture for a sheet](../disabling-the-pull-down-gesture-for-a-sheet.md)
  Ensure a positive user experience when presenting a view controller as a sheet.
### Responding to adaptive transitions
- [func presentationController(UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)](./presentationcontroller%28_,willpresentwithadaptivestyle,transitioncoordinator%29.md)
  Notifies the delegate that an adaptivity-related transition is about to occur.
- [func presentationControllerDidAttemptToDismiss(UIPresentationController)](./presentationcontrollerdidattempttodismiss%28_%29.md)
  Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [func presentationControllerDidDismiss(UIPresentationController)](./presentationcontrollerdiddismiss%28_%29.md)
  Notifies the delegate after a presentation is dismissed.
- [func presentationControllerWillDismiss(UIPresentationController)](./presentationcontrollerwilldismiss%28_%29.md)
  Notifies the delegate before a presentation is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:))*