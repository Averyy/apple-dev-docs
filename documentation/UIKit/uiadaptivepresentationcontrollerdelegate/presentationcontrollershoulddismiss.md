# presentationControllerShouldDismiss(_:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate for permission to dismiss the presentation.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func presentationControllerShouldDismiss(_ presentationController: UIPresentationController) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow the system to dismiss the presentation, [`false`](https://developer.apple.com/documentation/Swift/false) to refuse the dismissal.

#### Discussion

The system may call this method at any time. This method isn’t guaranteed to be followed by a call to [`presentationControllerWillDismiss(_:)`](uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:).md) or [`presentationControllerDidDismiss(_:)`](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:).md). Make sure that your implementation of this method returns quickly.

## Parameters

- `presentationController`: The presentation controller that manages the adaptivity change.

## See Also

- [Disabling the pull-down gesture for a sheet](disabling-the-pull-down-gesture-for-a-sheet.md)
  Ensure a positive user experience when presenting a view controller as a sheet.
- [func presentationController(UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:).md)
  Notifies the delegate that an adaptivity-related transition is about to occur.
- [func presentationControllerDidAttemptToDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:).md)
  Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [func presentationControllerDidDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:).md)
  Notifies the delegate after a presentation is dismissed.
- [func presentationControllerWillDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:).md)
  Notifies the delegate before a presentation is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:))*