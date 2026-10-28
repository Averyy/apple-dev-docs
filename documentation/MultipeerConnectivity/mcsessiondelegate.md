# MCSessionDelegate

**Framework**: Multipeer Connectivity  
**Kind**: protocol  
**Role**: Protocol

The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](./mcsession.md).

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
protocol MCSessionDelegate : NSObjectProtocol
```

```objc
@protocol MCSessionDelegate <NSObject>
```

## Overview

Delegate calls occur on a private serial queue. If your app needs to perform an action on a particular run loop or operation queue, its delegate method should explicitly dispatch or schedule that work.

## Topics

### MCSession Delegate Methods
- [func session(MCSession, didReceive: Data, fromPeer: MCPeerID)](./mcsessiondelegate/session%28_,didreceive,frompeer%29.md)
  Indicates that an `NSData` object has been received from a nearby peer.
- [func session(MCSession, didStartReceivingResourceWithName: String, fromPeer: MCPeerID, with: Progress)](./mcsessiondelegate/session%28_,didstartreceivingresourcewithname,frompeer,with%29.md)
  Indicates that the local peer began receiving a resource from a nearby peer.
- [func session(MCSession, didFinishReceivingResourceWithName: String, fromPeer: MCPeerID, at: URL?, withError: (any Error)?)](./mcsessiondelegate/session%28_,didfinishreceivingresourcewithname,frompeer,at,witherror%29.md)
  Indicates that the local peer finished receiving a resource from a nearby peer.
- [func session(MCSession, didReceive: InputStream, withName: String, fromPeer: MCPeerID)](./mcsessiondelegate/session%28_,didreceive,withname,frompeer%29.md)
  Called when a nearby peer opens a byte stream connection to the local peer.
- [func session(MCSession, peer: MCPeerID, didChange: MCSessionState)](./mcsessiondelegate/session%28_,peer,didchange%29.md)
  Called when the state of a nearby peer changes.
- [func session(MCSession, didReceiveCertificate: [Any]?, fromPeer: MCPeerID, certificateHandler: (Bool) -> Void)](./mcsessiondelegate/session%28_,didreceivecertificate,frompeer,certificatehandler%29.md)
  Called to validate the client certificate provided by a peer when the connection is first established.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Protocols
- [protocol MCAdvertiserAssistantDelegate](./mcadvertiserassistantdelegate.md)
  The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.
- [protocol MCBrowserViewControllerDelegate](./mcbrowserviewcontrollerdelegate.md)
  The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.
- [protocol MCNearbyServiceAdvertiserDelegate](./mcnearbyserviceadvertiserdelegate.md)
  The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.
- [protocol MCNearbyServiceBrowserDelegate](./mcnearbyservicebrowserdelegate.md)
  The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsessiondelegate)*