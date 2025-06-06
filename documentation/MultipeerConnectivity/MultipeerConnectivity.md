# Multipeer Connectivity

**Framework**: Multipeer Connectivity  
**Kind**: module

Support peer-to-peer connectivity and the discovery of nearby devices.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

#### Overview

The Multipeer Connectivity framework supports the discovery of services provided by nearby devices and supports communicating with those services through message-based data, streaming data, and resources (such as files). In iOS, the framework uses infrastructure Wi-Fi networks, peer-to-peer Wi-Fi, and Bluetooth personal area networks for the underlying transport. In macOS and tvOS, it uses infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Ethernet.

> ❗ **Important**:  Apps that use the local network must provide a usage string in their `Info.plist` with the key [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription). Apps that use Bonjour must also declare the services they browse, using the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) key.

 Apps that use the local network must provide a usage string in their `Info.plist` with the key [`NSLocalNetworkUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSLocalNetworkUsageDescription). Apps that use Bonjour must also declare the services they browse, using the [`NSBonjourServices`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSBonjourServices) key.

##### Architecture

When working with the Multipeer Connectivity framework, your app must interact with several types of objects:

- Session objects ([`MCSession`](mcsession.md)) support communication between connected peer devices. Your app creates a session and adds peers to it when peers accept an invitation to connect, and it creates a session when invited to connect by another peer. Session objects maintain a set of peer ID objects that represent the peers connected to the session.
- Advertiser objects ([`MCNearbyServiceAdvertiser`](mcnearbyserviceadvertiser.md)) tell nearby peers that your app is willing to join sessions of a specified type. An advertiser object uses a single local peer object to provide information that identifies the device and its user to other nearby devices.
- Advertiser assistant objects ([`MCAdvertiserAssistant`](mcadvertiserassistant.md)) provide the same functionality as advertiser objects, but also provide a standard user interface that allows the user to accept invitations. If you wish to provide your own user interface, or if you wish to exercise additional programmatic control over which invitations are displayed, use an advertiser object directly.
- Browser objects ([`MCNearbyServiceBrowser`](mcnearbyservicebrowser.md)) let your app search programmatically for nearby devices with apps that support sessions of a particular type.
- Browser view controller objects ([`MCBrowserViewController`](mcbrowserviewcontroller.md)) provide a standard user interface that allows the user to choose nearby peers to add to a session.
- Peer IDs ([`MCPeerID`](mcpeerid.md)) uniquely identify an app running on a device to nearby peers.

##### Discovery Phase and Session Phase

This framework is used in two phases: the discovery phase and the session phase.

In the discovery phase, your app uses an [`MCNearbyServiceBrowser`](mcnearbyservicebrowser.md) object to browse for nearby peers, optionally using the [`MCBrowserViewController`](mcbrowserviewcontroller.md) object to display a user interface.

The app also uses an [`MCNearbyServiceAdvertiser`](mcnearbyserviceadvertiser.md) object or an [`MCAdvertiserAssistant`](mcadvertiserassistant.md) object to tell nearby peers that it is available, so that apps on other nearby devices can invite it to a session.

During the discovery phase, your app has limited communication with and knowledge of other peers; it has access to the `discoveryInfo` data that other nearby clients provide, and any context data that other peers provide when inviting it to join a session.

After the user chooses which peers to add to a session, the app invites those peers to join the session. Apps running on the nearby devices can choose whether to accept or reject the invitation, and can ask their users for permission.

If the peer accepts the invitation, the browser establishes a connection with the advertiser and the session phase begins. In this phase, your app can perform direct communication to one or more peers within the session. The framework notifies your app through delegate callbacks when peers join the session and when they leave the session.

If the app moves into the background, the framework stops advertising and browsing and disconnects any open sessions. Upon returning to the foreground, the framework automatically resumes advertising and browsing, but the developer must reestablish any closed sessions.

## Topics

### Classes
- [class MCAdvertiserAssistant](mcadvertiserassistant.md)
  The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.
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
### Protocols
- [protocol MCAdvertiserAssistantDelegate](mcadvertiserassistantdelegate.md)
  The `MCAdvertiserAssistantDelegate` protocol describes the methods that the delegate object for an `MCAdvertiserAssistant` instance can implement to handle advertising-related events.
- [protocol MCBrowserViewControllerDelegate](mcbrowserviewcontrollerdelegate.md)
  The `MCBrowserViewControllerDelegate` protocol defines the methods that your delegate object can implement to handle events related to the `MCBrowserViewController` class.
- [protocol MCNearbyServiceAdvertiserDelegate](mcnearbyserviceadvertiserdelegate.md)
  The `MCNearbyServiceAdvertiserDelegate` protocol describes the methods that the delegate object for an `MCNearbyServiceAdvertiser` instance can implement for handling events from the `MCNearbyServiceAdvertiser` class.
- [protocol MCNearbyServiceBrowserDelegate](mcnearbyservicebrowserdelegate.md)
  The `MCNearbyServiceBrowserDelegate` protocol defines methods that a `MCNearbyServiceBrowser` object’s delegate can implement to handle browser-related events.
- [protocol MCSessionDelegate](mcsessiondelegate.md)
  The `MCSessionDelegate` protocol defines methods that a delegate of the `MCSession` class can implement to handle session-related events. For more information, see [`MCSession`](mcsession.md).
### Structures
- [struct MCError](mcerror.md)
### Reference
- [MultipeerConnectivity Enumerations](multipeerconnectivity_enumerations.md)
- [MultipeerConnectivity Constants](multipeerconnectivity_constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/MultipeerConnectivity)*