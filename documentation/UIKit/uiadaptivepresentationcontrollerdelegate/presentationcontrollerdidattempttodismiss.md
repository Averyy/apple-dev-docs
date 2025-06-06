# presentationControllerDidAttemptToDismiss(_:)

**Framework**: UIKit  
**Kind**: method

Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func presentationControllerDidAttemptToDismiss(_ presentationController: UIPresentationController)
```

#### Discussion

UIKit supports refusing to dismiss a presentation when the `presentationController`.[`isModalInPresentation`](uiviewcontroller/ismodalinpresentation.md) returns `true` or [`presentationControllerShouldDismiss(_:)`](uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:).md) returns `false`.

Use this method to inform the user why the presentation can’t be dismissed, for example, by presenting an instance of [`UIAlertController`](uialertcontroller.md).

## Parameters

- `presentationController`: The presentation controller managing the adaptivity change.

## See Also

- [func presentationController(UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:).md)
  Notifies the delegate that an adaptivity-related transition is about to occur.
- [func presentationControllerShouldDismiss(UIPresentationController) -> Bool](uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:).md)
  Asks the delegate for permission to dismiss the presentation.
- [func presentationControllerDidDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:).md)
  Notifies the delegate after a presentation is dismissed.
- [func presentationControllerWillDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:).md)
  Notifies the delegate before a presentation is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:))*