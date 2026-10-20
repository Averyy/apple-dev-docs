# MCNearbyServiceBrowser

**Framework**: Multipeer Connectivity  
**Kind**: class  
**Role**: Class

Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).

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
class MCNearbyServiceBrowser
```

```objc
@interface MCNearbyServiceBrowser : NSObject
```

## Topics

### Initializing the Browser
- [init(peer: MCPeerID, serviceType: String)](./mcnearbyservicebrowser/init%28peer,servicetype%29.md)
  Initializes the nearby service browser object.
- [var delegate: (any MCNearbyServiceBrowserDelegate)?](./mcnearbyservicebrowser/delegate.md)
  The delegate object that handles browser-related events.
- [var myPeerID: MCPeerID](./mcnearbyservicebrowser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](./mcnearbyservicebrowser/servicetype.md)
  The service type to browse for.
### Browsing for Peers
- [func startBrowsingForPeers()](./mcnearbyservicebrowser/startbrowsingforpeers%28%29.md)
  Starts browsing for peers.
- [func stopBrowsingForPeers()](./mcnearbyservicebrowser/stopbrowsingforpeers%28%29.md)
  Stops browsing for peers.
### Inviting Peers
- [func invitePeer(MCPeerID, to: MCSession, withContext: Data?, timeout: TimeInterval)](./mcnearbyservicebrowser/invitepeer%28_,to,withcontext,timeout%29.md)
  Invites a discovered peer to join a Multipeer Connectivity session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Classes
- [class MCAdvertiserAssistant](./mcadvertiserassistant.md)
  The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.
- [class MCBrowserViewController](./mcbrowserviewcontroller.md)
  The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](../UIKit/uiviewcontroller/prepare%28for,sender%29.md) and [`performSegue(withIdentifier:sender:)`](../UIKit/uiviewcontroller/performsegue%28withidentifier,sender%29.md) for storyboards or [`present(_:animated:completion:)`](../UIKit/uiviewcontroller/present%28_,animated,completion%29.md) and [`dismiss(animated:completion:)`](../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](../AppKit/nsviewcontroller/presentassheet%28_%29.md) and [`dismiss(_:)`](../AppKit/nsviewcontroller/dismiss%28_%29-91my5.md) instead.
- [class MCNearbyServiceAdvertiser](./mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCPeerID](./mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.
- [class MCSession](./mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser)*