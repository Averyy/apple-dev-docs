# MCNearbyServiceBrowserDelegate

**Framework**: Multipeer Connectivity  
**Kind**: protocol  
**Role**: Protocol

The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
protocol MCNearbyServiceBrowserDelegate : NSObjectProtocol
```

```objc
@protocol MCNearbyServiceBrowserDelegate <NSObject>
```

## Overview

No assumption should be made about which queue the delegate methods are called on. It is the receiver’s responsibility to ensure that any `UIKit` updates are called on the main thread.

## Topics

### Error Handling Delegate Methods
- [func browser(MCNearbyServiceBrowser, didNotStartBrowsingForPeers: any Error)](./mcnearbyservicebrowserdelegate/browser%28_,didnotstartbrowsingforpeers%29.md)
  Called when a browser failed to start browsing for peers.
### Peer Discovery Delegate Methods
- [func browser(MCNearbyServiceBrowser, foundPeer: MCPeerID, withDiscoveryInfo: [String : String]?)](./mcnearbyservicebrowserdelegate/browser%28_,foundpeer,withdiscoveryinfo%29.md)
  Called when a nearby peer is found.
- [func browser(MCNearbyServiceBrowser, lostPeer: MCPeerID)](./mcnearbyservicebrowserdelegate/browser%28_,lostpeer%29.md)
  Called when a nearby peer is lost.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [MCBrowserViewController](./mcbrowserviewcontroller.md)

## See Also

### Protocols
- [protocol MCAdvertiserAssistantDelegate](./mcadvertiserassistantdelegate.md)
  The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.
- [protocol MCBrowserViewControllerDelegate](./mcbrowserviewcontrollerdelegate.md)
  The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.
- [protocol MCNearbyServiceAdvertiserDelegate](./mcnearbyserviceadvertiserdelegate.md)
  The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.
- [protocol MCSessionDelegate](./mcsessiondelegate.md)
  The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](./mcsession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate)*