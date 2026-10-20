# SFSafariViewControllerDelegate

**Framework**: Safari Services  
**Kind**: protocol  
**Role**: Protocol

A protocol used to implement custom event handling for a Safari view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol SFSafariViewControllerDelegate : NSObjectProtocol
```

```objc
@protocol SFSafariViewControllerDelegate <NSObject>
```

#### Overview

For more information about the `SFSafariViewController` class, see [`SFSafariViewController`](./sfsafariviewcontroller.md).

## Topics

### Working with the View Controller
- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](./sfsafariviewcontrollerdelegate/safariviewcontroller%28_,didcompleteinitialload%29.md)
  Tells the delegate that the initial URL load completed.
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](./sfsafariviewcontrollerdelegate/safariviewcontroller%28_,activityitemsfor,title%29.md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewControllerDidFinish(SFSafariViewController)](./sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish%28_%29.md)
  Tells the delegate that the user dismissed the view.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](./sfsafariviewcontrollerdelegate/safariviewcontroller%28_,excludedactivitytypesfor,title%29.md)
### Instance Methods
- [func safariViewController(SFSafariViewController, initialLoadDidRedirectTo: URL)](./sfsafariviewcontrollerdelegate/safariviewcontroller%28_,initialloaddidredirectto%29.md)
- [func safariViewControllerWillOpenInBrowser(SFSafariViewController)](./sfsafariviewcontrollerdelegate/safariviewcontrollerwillopeninbrowser%28_%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to View Controller Interaction
- [var delegate: (any SFSafariViewControllerDelegate)?](./sfsafariviewcontroller/delegate.md)
  An object that provides behavior for the Safari view controller’s Done and Action buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate)*