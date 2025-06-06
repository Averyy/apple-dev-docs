# MCBrowserViewControllerDelegate

**Framework**: Multipeer Connectivity  
**Kind**: protocol

The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol MCBrowserViewControllerDelegate : NSObjectProtocol
```

#### Overview

No assumption should be made about which queue the delegate methods are called on. It is the receiver’s responsibility to ensure that any UIKit-related updates are called on the main thread.

## Topics

### Peer Notifications
- [func browserViewController(MCBrowserViewController, shouldPresentNearbyPeer: MCPeerID, withDiscoveryInfo: [String : String]?) -> Bool](mcbrowserviewcontrollerdelegate/browserviewcontroller(_:shouldpresentnearbypeer:withdiscoveryinfo:).md)
  Called when a new peer is discovered to decide whether to show it in the user interface.
### User Action Notifications
- [func browserViewControllerDidFinish(MCBrowserViewController)](mcbrowserviewcontrollerdelegate/browserviewcontrollerdidfinish(_:).md)
  Called when the browser view controller is dismissed with peers connected in a session.
- [func browserViewControllerWasCancelled(MCBrowserViewController)](mcbrowserviewcontrollerdelegate/browserviewcontrollerwascancelled(_:).md)
  Called when the user cancels the browser view controller.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MCAdvertiserAssistantDelegate](mcadvertiserassistantdelegate.md)
  The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.
- [protocol MCNearbyServiceAdvertiserDelegate](mcnearbyserviceadvertiserdelegate.md)
  The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.
- [protocol MCNearbyServiceBrowserDelegate](mcnearbyservicebrowserdelegate.md)
  The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.
- [protocol MCSessionDelegate](mcsessiondelegate.md)
  The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](mcsession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcbrowserviewcontrollerdelegate)*