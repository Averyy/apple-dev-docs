# presentationControllerDidAttemptToDismiss(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
optional func presentationControllerDidAttemptToDismiss(_ presentationController: UIPresentationController)
```

```objc
- (void) presentationControllerDidAttemptToDismiss:(UIPresentationController *) presentationController;
```

## Discussion

UIKit supports refusing to dismiss a presentation when the `presentationController`.[`isModalInPresentation`](../uiviewcontroller/ismodalinpresentation.md) returns `true` or [`presentationControllerShouldDismiss(_:)`](./presentationcontrollershoulddismiss%28_%29.md) returns `false`.

Use this method to inform the user why the presentation can’t be dismissed, for example, by presenting an instance of [`UIAlertController`](../uialertcontroller.md).

## Parameters

- `presentationController`: The presentation controller managing the adaptivity change.

## See Also

### Responding to adaptive transitions
- [func presentationController(UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)](./presentationcontroller%28_,willpresentwithadaptivestyle,transitioncoordinator%29.md)
  Notifies the delegate that an adaptivity-related transition is about to occur.
- [func presentationControllerShouldDismiss(UIPresentationController) -> Bool](./presentationcontrollershoulddismiss%28_%29.md)
  Asks the delegate for permission to dismiss the presentation.
- [func presentationControllerDidDismiss(UIPresentationController)](./presentationcontrollerdiddismiss%28_%29.md)
  Notifies the delegate after a presentation is dismissed.
- [func presentationControllerWillDismiss(UIPresentationController)](./presentationcontrollerwilldismiss%28_%29.md)
  Notifies the delegate before a presentation is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:))*