# NSPageControllerDelegate

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

The `NSPageControllerDelegate` protocol allows you to customize the behavior of instances of the NSPageController class.

**Availability**:
- macOS

## Declaration

```swift
protocol NSPageControllerDelegate : NSObjectProtocol
```

```objc
@protocol NSPageControllerDelegate <NSObject>
```

#### Overview

See [`NSPageController`](./nspagecontroller.md) for more information.

> **Note**:  If your page controller is going to completely manage the page snapshots, then you should not implement the [`pageController(_:viewControllerForIdentifier:)`](./nspagecontrollerdelegate/pagecontroller%28_,viewcontrollerforidentifier%29.md) or [`pageController(_:prepare:with:)`](./nspagecontrollerdelegate/pagecontroller%28_,prepare,with%29.md) methods.
>
> However, if you manually set the `NSPageController` instance’s [`arrangedObjects`](./nspagecontroller/arrangedobjects.md) property, you are required to implement the following those methods so that navigation can properly occur.

## Topics

### Transition Notification
- [func pageControllerWillStartLiveTransition(NSPageController)](./nspagecontrollerdelegate/pagecontrollerwillstartlivetransition%28_%29.md)
  This message is sent when the user begins a transition.
- [func pageControllerDidEndLiveTransition(NSPageController)](./nspagecontrollerdelegate/pagecontrollerdidendlivetransition%28_%29.md)
  This message is sent when a transition animation completes.
- [func pageController(NSPageController, didTransitionTo: Any)](./nspagecontrollerdelegate/pagecontroller%28_,didtransitionto%29.md)
  This message is sent when any page transition is completed.
### Managing View Controllers
- [func pageController(NSPageController, identifierFor: Any) -> NSPageController.ObjectIdentifier](./nspagecontrollerdelegate/pagecontroller%28_,identifierfor%29.md)
  Return the identifier of the view controller that owns a view to display the object.
- [func pageController(NSPageController, viewControllerForIdentifier: NSPageController.ObjectIdentifier) -> NSViewController](./nspagecontrollerdelegate/pagecontroller%28_,viewcontrollerforidentifier%29.md)
  Returns a view controller the page controller uses for managing the specified identifier.
- [func pageController(NSPageController, prepare: NSViewController, with: Any?)](./nspagecontrollerdelegate/pagecontroller%28_,prepare,with%29.md)
  Prepare the view controller and it’s view for drawing.
- [func pageController(NSPageController, frameFor: Any?) -> NSRect](./nspagecontrollerdelegate/pagecontroller%28_,framefor%29.md)
  Returns the frame appropriate for displaying the specified object.
- [NSPageController.ObjectIdentifier](./nspagecontroller/objectidentifier.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Customizing the Paged Interface Behavior
- [var delegate: (any NSPageControllerDelegate)?](./nspagecontroller/delegate.md)
  The page controller’s delegate object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspagecontrollerdelegate)*