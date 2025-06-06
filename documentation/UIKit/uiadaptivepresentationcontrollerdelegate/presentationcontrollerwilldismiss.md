# presentationControllerWillDismiss(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate before a presentation is dismissed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func presentationControllerWillDismiss(_ presentationController: UIPresentationController)
```

#### Discussion

You can use this method to set up animations or interaction notifications with the presentationController’s transitionCoordinator.

This method is not called if the presentation is dismissed programmatically.

## Parameters

- `presentationController`: The presentation controller managing the trait changes from your app.

## See Also

- [func presentationController(UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:).md)
  Notifies the delegate that an adaptivity-related transition is about to occur.
- [func presentationControllerDidAttemptToDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:).md)
  Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [func presentationControllerShouldDismiss(UIPresentationController) -> Bool](uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:).md)
  Asks the delegate for permission to dismiss the presentation.
- [func presentationControllerDidDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:).md)
  Notifies the delegate after a presentation is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:))*