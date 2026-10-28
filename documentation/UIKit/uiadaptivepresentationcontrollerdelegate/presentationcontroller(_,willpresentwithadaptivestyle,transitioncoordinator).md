# presentationController(_:willPresentWithAdaptiveStyle:transitionCoordinator:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate that an adaptivity-related transition is about to occur.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func presentationController(_ presentationController: UIPresentationController, willPresentWithAdaptiveStyle style: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)
```

```objc
- (void) presentationController:(UIPresentationController *) presentationController willPresentWithAdaptiveStyle:(UIModalPresentationStyle) style transitionCoordinator:(id<UIViewControllerTransitionCoordinator>) transitionCoordinator;
```

## Discussion

When a size class change occurs, UIKit calls this method to let you know how the presentation controller will adapt. Use this method to make any additional changes. For example, you might use the transition coordinator object to create additional animations for the transition.

## Parameters

- `presentationController`: The presentation controller that is managing the adaptivity change.
- `style`: The new presentation style. If the presentation style is not changing, this parameter is set to [`UIModalPresentationStyle.none`](../uimodalpresentationstyle/none.md).
- `transitionCoordinator`: The transition coordinator that is managing the transition.

## See Also

### Responding to adaptive transitions
- [func presentationControllerDidAttemptToDismiss(UIPresentationController)](./presentationcontrollerdidattempttodismiss%28_%29.md)
  Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [func presentationControllerShouldDismiss(UIPresentationController) -> Bool](./presentationcontrollershoulddismiss%28_%29.md)
  Asks the delegate for permission to dismiss the presentation.
- [func presentationControllerDidDismiss(UIPresentationController)](./presentationcontrollerdiddismiss%28_%29.md)
  Notifies the delegate after a presentation is dismissed.
- [func presentationControllerWillDismiss(UIPresentationController)](./presentationcontrollerwilldismiss%28_%29.md)
  Notifies the delegate before a presentation is dismissed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:))*