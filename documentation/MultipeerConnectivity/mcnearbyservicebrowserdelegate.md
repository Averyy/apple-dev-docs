# MCNearbyServiceBrowserDelegate

**Framework**: Multipeer Connectivity  
**Kind**: protocol

The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
protocol MCNearbyServiceBrowserDelegate : NSObjectProtocol
```

#### Overview

No assumption should be made about which queue the delegate methods are called on. It is the receiver’s responsibility to ensure that any `UIKit` updates are called on the main thread.

## Topics

### Error Handling Delegate Methods
- [func browser(MCNearbyServiceBrowser, didNotStartBrowsingForPeers: any Error)](mcnearbyservicebrowserdelegate/browser(_:didnotstartbrowsingforpeers:).md)
  Called when a browser failed to start browsing for peers.
### Peer Discovery Delegate Methods
- [func browser(MCNearbyServiceBrowser, foundPeer: MCPeerID, withDiscoveryInfo: [String : String]?)](mcnearbyservicebrowserdelegate/browser(_:foundpeer:withdiscoveryinfo:).md)
  Called when a nearby peer is found.
- [func browser(MCNearbyServiceBrowser, lostPeer: MCPeerID)](mcnearbyservicebrowserdelegate/browser(_:lostpeer:).md)
  Called when a nearby peer is lost.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [MCBrowserViewController](mcbrowserviewcontroller.md)

## See Also

- [protocol MCAdvertiserAssistantDelegate](mcadvertiserassistantdelegate.md)
  The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.
- [protocol MCBrowserViewControllerDelegate](mcbrowserviewcontrollerdelegate.md)
  The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.
- [protocol MCNearbyServiceAdvertiserDelegate](mcnearbyserviceadvertiserdelegate.md)
  The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.
- [protocol MCSessionDelegate](mcsessiondelegate.md)
  The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](mcsession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate)*