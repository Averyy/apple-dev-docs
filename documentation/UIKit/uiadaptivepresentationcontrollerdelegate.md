# UIAdaptivePresentationControllerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
@MainActor
protocol UIAdaptivePresentationControllerDelegate : NSObjectProtocol
```

#### Overview

After implementing an object that conforms to this protocol, assign that object to the [`delegate`](uipresentationcontroller/delegate.md) property of an appropriate [`UIPresentationController`](uipresentationcontroller.md) object. Your delegate can suggest a new presentation style or an entirely new view controller for displaying content. For more information about using the delegate to respond to size class changes, see [`UIPresentationController`](uipresentationcontroller.md).

## Topics

### Adapting the presentation style
- [func adaptivePresentationStyle(for: UIPresentationController, traitCollection: UITraitCollection) -> UIModalPresentationStyle](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:traitcollection:).md)
  Asks the delegate for the presentation style to use when the specified set of traits are active.
- [func adaptivePresentationStyle(for: UIPresentationController) -> UIModalPresentationStyle](uiadaptivepresentationcontrollerdelegate/adaptivepresentationstyle(for:).md)
  Asks the delegate for the new presentation style to use.
### Adapting the view controller
- [func presentationController(UIPresentationController, viewControllerForAdaptivePresentationStyle: UIModalPresentationStyle) -> UIViewController?](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:viewcontrollerforadaptivepresentationstyle:).md)
  Asks the delegate for the view controller to display when adapting to the specified presentation style.
### Responding to adaptive transitions
- [func presentationController(UIPresentationController, willPresentWithAdaptiveStyle: UIModalPresentationStyle, transitionCoordinator: (any UIViewControllerTransitionCoordinator)?)](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:willpresentwithadaptivestyle:transitioncoordinator:).md)
  Notifies the delegate that an adaptivity-related transition is about to occur.
- [func presentationControllerDidAttemptToDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdidattempttodismiss(_:).md)
  Notifies the delegate that a user-initiated attempt to dismiss a view was prevented.
- [func presentationControllerShouldDismiss(UIPresentationController) -> Bool](uiadaptivepresentationcontrollerdelegate/presentationcontrollershoulddismiss(_:).md)
  Asks the delegate for permission to dismiss the presentation.
- [func presentationControllerDidDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerdiddismiss(_:).md)
  Notifies the delegate after a presentation is dismissed.
- [func presentationControllerWillDismiss(UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontrollerwilldismiss(_:).md)
  Notifies the delegate before a presentation is dismissed.
### Preparing the adaptive presentation controller
- [func presentationController(UIPresentationController, prepare: UIPresentationController)](uiadaptivepresentationcontrollerdelegate/presentationcontroller(_:prepare:).md)
  Provides an opportunity to configure the adaptive presentation controller after an adaptivity change.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [UIPopoverPresentationControllerDelegate](uipopoverpresentationcontrollerdelegate.md)
- [UISheetPresentationControllerDelegate](uisheetpresentationcontrollerdelegate.md)

## See Also

- [class UITraitCollection](uitraitcollection.md)
  A collection of data that represents the environment for an individual element in your app’s user interface.
- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiadaptivepresentationcontrollerdelegate)*