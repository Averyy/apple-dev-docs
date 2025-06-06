# SFSafariViewControllerDelegate

**Framework**: Safari Services  
**Kind**: protocol

A protocol used to implement custom event handling for a Safari view controller.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+

## Declaration

```swift
protocol SFSafariViewControllerDelegate : NSObjectProtocol
```

#### Overview

For more information about the `SFSafariViewController` class, see [`SFSafariViewController`](sfsafariviewcontroller.md).

## Topics

### Working with the View Controller
- [func safariViewController(SFSafariViewController, didCompleteInitialLoad: Bool)](sfsafariviewcontrollerdelegate/safariviewcontroller(_:didcompleteinitialload:).md)
  Tells the delegate that the initial URL load completed.
- [func safariViewController(SFSafariViewController, activityItemsFor: URL, title: String?) -> [UIActivity]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:activityitemsfor:title:).md)
  Tells the delegate that the user tapped an Action button.
- [func safariViewControllerDidFinish(SFSafariViewController)](sfsafariviewcontrollerdelegate/safariviewcontrollerdidfinish(_:).md)
  Tells the delegate that the user dismissed the view.
- [func safariViewController(SFSafariViewController, excludedActivityTypesFor: URL, title: String?) -> [UIActivity.ActivityType]](sfsafariviewcontrollerdelegate/safariviewcontroller(_:excludedactivitytypesfor:title:).md)
### Instance Methods
- [func safariViewController(SFSafariViewController, initialLoadDidRedirectTo: URL)](sfsafariviewcontrollerdelegate/safariviewcontroller(_:initialloaddidredirectto:).md)
- [func safariViewControllerWillOpenInBrowser(SFSafariViewController)](sfsafariviewcontrollerdelegate/safariviewcontrollerwillopeninbrowser(_:).md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SFSafariViewControllerDelegate)?](sfsafariviewcontroller/delegate.md)
  An object that provides behavior for the Safari view controller’s Done and Action buttons.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariviewcontrollerdelegate)*