# MCAdvertiserAssistant

**Framework**: Multipeer Connectivity  
**Kind**: class

The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MCAdvertiserAssistant
```

#### Overview

Before you can advertise a service, you must create an `MCPeerID` object that identifies your app and the user to nearby devices.

## Topics

### Initializing and Configuring
- [init(serviceType: String, discoveryInfo: [String : String]?, session: MCSession)](mcadvertiserassistant/init(servicetype:discoveryinfo:session:).md)
  Initializes an advertiser assistant object.
- [var session: MCSession](mcadvertiserassistant/session.md)
  The session into which new peers are added after accepting an invitation.
- [var delegate: (any MCAdvertiserAssistantDelegate)?](mcadvertiserassistant/delegate.md)
  The delegate object that handles advertising-assistant-related events.
- [var discoveryInfo: [String : String]?](mcadvertiserassistant/discoveryinfo.md)
  The `info` dictionary that was passed when this object was initialized.
- [var serviceType: String](mcadvertiserassistant/servicetype.md)
  The service type that your app is advertising.
### Starting and Stopping the Assistant
- [func start()](mcadvertiserassistant/start.md)
  Begins advertising the service provided by a local peer and starts the assistant.
- [func stop()](mcadvertiserassistant/stop.md)
  Stops advertising the service provided by a local peer and stops the assistant.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MCBrowserViewController](mcbrowserviewcontroller.md)
  The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/prepare(for:sender:)) and [`performSegue(withIdentifier:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/performSegue(withIdentifier:sender:)) for storyboards or [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)) and [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/presentAsSheet(_:)) and [`dismiss(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/dismiss(_:)-91my5) instead.
- [class MCNearbyServiceAdvertiser](mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCNearbyServiceBrowser](mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCPeerID](mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.
- [class MCSession](mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcadvertiserassistant)*