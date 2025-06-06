# MCNearbyServiceAdvertiser

**Framework**: Multipeer Connectivity  
**Kind**: class

The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MCNearbyServiceAdvertiser
```

#### Overview

Before you can advertise a service, you must create an `MCPeerID` object that identifies your app and the user to nearby devices.

The `serviceType` parameter is a short text string used to describe the app’s networking protocol.  It should be in the same format as a Bonjour service type: 1–15 characters long and valid characters include ASCII lowercase letters, numbers, and the hyphen, containing at least one letter and no adjacent hyphens.  A short name that distinguishes itself from unrelated services is recommended; for example, a text chat app made by ABC company could use the service type `"abc-txtchat"`. For more information about service types, read [`Domain Naming Conventions`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/domainnames.html#//apple_ref/doc/uid/TP40002460).

The `discoveryInfo` parameter is a dictionary of string key/value pairs that will be advertised for browsers to see.  The content of `discoveryInfo` will be advertised within Bonjour TXT records, so you should keep the dictionary small for better discovery performance.

For more information about TXT records, read [`Bonjour Operations`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/NetServices/Articles/NetServicesArchitecture.html#//apple_ref/doc/uid/20001074).

## Topics

### Configuring and Initialization
- [init(peer: MCPeerID, discoveryInfo: [String : String]?, serviceType: String)](mcnearbyserviceadvertiser/init(peer:discoveryinfo:servicetype:).md)
  Initializes an advertiser object.
- [var delegate: (any MCNearbyServiceAdvertiserDelegate)?](mcnearbyserviceadvertiser/delegate.md)
  The delegate object that handles advertising-related events.
- [var discoveryInfo: [String : String]?](mcnearbyserviceadvertiser/discoveryinfo.md)
  The `info` dictionary passed when this object was initialized.
- [var myPeerID: MCPeerID](mcnearbyserviceadvertiser/mypeerid.md)
  The local peer ID for this instance.
- [var serviceType: String](mcnearbyserviceadvertiser/servicetype.md)
  The service type that your app is advertising
### Starting and Stopping Advertisement
- [func startAdvertisingPeer()](mcnearbyserviceadvertiser/startadvertisingpeer.md)
  Begins advertising the service provided by a local peer.
- [func stopAdvertisingPeer()](mcnearbyserviceadvertiser/stopadvertisingpeer.md)
  Stops advertising the service provided by a local peer.

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

- [class MCAdvertiserAssistant](mcadvertiserassistant.md)
  The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.
- [class MCBrowserViewController](mcbrowserviewcontroller.md)
  The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/prepare(for:sender:)) and [`performSegue(withIdentifier:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/performSegue(withIdentifier:sender:)) for storyboards or [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)) and [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/presentAsSheet(_:)) and [`dismiss(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/dismiss(_:)-91my5) instead.
- [class MCNearbyServiceBrowser](mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCPeerID](mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.
- [class MCSession](mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyserviceadvertiser)*