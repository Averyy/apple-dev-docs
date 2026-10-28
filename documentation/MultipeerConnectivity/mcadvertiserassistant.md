# MCAdvertiserAssistant

**Framework**: Multipeer Connectivity  
**Kind**: class  
**Role**: Class

The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.

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
class MCAdvertiserAssistant
```

```objc
@interface MCAdvertiserAssistant : NSObject
```

## Overview

Before you can advertise a service, you must create an `MCPeerID` object that identifies your app and the user to nearby devices.

## Topics

### Initializing and Configuring
- [init(serviceType: String, discoveryInfo: [String : String]?, session: MCSession)](./mcadvertiserassistant/init%28servicetype,discoveryinfo,session%29.md)
  Initializes an advertiser assistant object.
- [var session: MCSession](./mcadvertiserassistant/session.md)
  The session into which new peers are added after accepting an invitation.
- [var delegate: (any MCAdvertiserAssistantDelegate)?](./mcadvertiserassistant/delegate.md)
  The delegate object that handles advertising-assistant-related events.
- [var discoveryInfo: [String : String]?](./mcadvertiserassistant/discoveryinfo.md)
  The `info` dictionary that was passed when this object was initialized.
- [var serviceType: String](./mcadvertiserassistant/servicetype.md)
  The service type that your app is advertising.
### Starting and Stopping the Assistant
- [func start()](./mcadvertiserassistant/start%28%29.md)
  Begins advertising the service provided by a local peer and starts the assistant.
- [func stop()](./mcadvertiserassistant/stop%28%29.md)
  Stops advertising the service provided by a local peer and stops the assistant.

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
- [class MCBrowserViewController](./mcbrowserviewcontroller.md)
  The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](../UIKit/uiviewcontroller/prepare%28for,sender%29.md) and [`performSegue(withIdentifier:sender:)`](../UIKit/uiviewcontroller/performsegue%28withidentifier,sender%29.md) for storyboards or [`present(_:animated:completion:)`](../UIKit/uiviewcontroller/present%28_,animated,completion%29.md) and [`dismiss(animated:completion:)`](../UIKit/uiviewcontroller/dismiss%28animated,completion%29.md) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](../AppKit/nsviewcontroller/presentassheet%28_%29.md) and [`dismiss(_:)`](../AppKit/nsviewcontroller/dismiss%28_%29-91my5.md) instead.
- [class MCNearbyServiceAdvertiser](./mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCNearbyServiceBrowser](./mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCPeerID](./mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.
- [class MCSession](./mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)*