# NSPageControllerDelegate

**Framework**: AppKit  
**Kind**: protocol

The `NSPageControllerDelegate` protocol allows you to customize the behavior of instances of the NSPageController class.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSPageControllerDelegate : NSObjectProtocol
```

#### Overview

See [`NSPageController`](nspagecontroller.md) for more information.

> **Note**:  If your page controller is going to completely manage the page snapshots, then you should not implement the [`pageController(_:viewControllerForIdentifier:)`](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md) or [`pageController(_:prepare:with:)`](nspagecontrollerdelegate/pagecontroller(_:prepare:with:).md) methods. However, if you manually set the `NSPageController` instance’s [`arrangedObjects`](nspagecontroller/arrangedobjects.md) property, you are required to implement the following those methods so that navigation can properly occur.

## Topics

### Transition Notification
- [func pageControllerWillStartLiveTransition(NSPageController)](nspagecontrollerdelegate/pagecontrollerwillstartlivetransition(_:).md)
  This message is sent when the user begins a transition.
- [func pageControllerDidEndLiveTransition(NSPageController)](nspagecontrollerdelegate/pagecontrollerdidendlivetransition(_:).md)
  This message is sent when a transition animation completes.
- [func pageController(NSPageController, didTransitionTo: Any)](nspagecontrollerdelegate/pagecontroller(_:didtransitionto:).md)
  This message is sent when any page transition is completed.
### Managing View Controllers
- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](nspagecontrollerdelegate/pagecontroller(_:identifierfor:).md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](nspagecontrollerdelegate/pagecontroller(_:viewcontrollerforidentifier:).md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](nspagecontrollerdelegate/pagecontroller(_:prepare:with:).md)
  Prepare the view controller and it’s view for drawing.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](nspagecontrollerdelegate/pagecontroller(_:framefor:).md)
  Returns the frame appropriate for displaying the specified object.
- [NSPageController.ObjectIdentifier](nspagecontroller/objectidentifier.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSPageControllerDelegate)?](nspagecontroller/delegate.md)
  The page controller’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate)*