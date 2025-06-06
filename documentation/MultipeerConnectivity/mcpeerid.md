# MCPeerID

**Framework**: Multipeer Connectivity  
**Kind**: class

An  `MCPeerID` object represents a peer in a multipeer session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MCPeerID
```

#### Overview

You create a single peer ID object that represents the instance of your app running on the local device. The Multipeer Connectivity framework is responsible for creating peer ID objects that represent other devices.

To create a new peer ID for the local app and associate a display name with that ID, call [`init(displayName:)`](mcpeerid/init(displayname:).md). The peer’s name must be no longer than 63 bytes in UTF-8 encoding.

Each peer ID your app creates with [`init(displayName:)`](mcpeerid/init(displayname:).md) is unique, even when supplying the same display name. If you want a device’s peer ID to be stable over time, don’t create a new peer ID every time your app begins advertising or browsing. Instead, archive the ID when you create it, and then unarchive it the next time you need it. If you need the peer ID to be tied to the display name, you can archive the name as well, and only create a new peer ID when the name changes, as illustrated in the following code fragment:

```objc
NSString *displayName = <#Get a name#>;
 
NSUserDefaults *defaults = [NSUserDefaults standardUserDefaults];
NSString *oldDisplayName = [defaults stringForKey:kDisplayNameKey];
MCPeerID *peerID;
 
if ([oldDisplayName isEqualToString:displayName]) {
    NSData *peerIDData = [defaults dataForKey:kPeerIDKey];
    peerID = [NSKeyedUnarchiver unarchiveObjectWithData:peerIDData];
} else {
    peerID = [[MCPeerID alloc] initWithDisplayName:displayName];
    NSData *peerIDData = [NSKeyedArchiver archivedDataWithRootObject:peerID];
    [defaults setObject:peerIDData forKey:kPeerIDKey];
    [defaults setObject:displayName forKey:kDisplayNameKey];
    [defaults synchronize];
}
```

## Topics

### Peer Methods
- [init(displayName: String)](mcpeerid/init(displayname:).md)
  Initializes a peer.
- [var displayName: String](mcpeerid/displayname.md)
  The display name for this peer.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [SynchronizationPeerID](../RealityKit/SynchronizationPeerID.md)

## See Also

- [class MCAdvertiserAssistant](mcadvertiserassistant.md)
  The `MCAdvertiserAssistant` is a convenience class that handles advertising, presents incoming invitations to the user, and handles users’ responses. Use this class to provide a user interface for handling invitations when your app does not require programmatic control over the invitation process.
- [class MCBrowserViewController](mcbrowserviewcontroller.md)
  The `MCBrowserViewController` class presents nearby devices to the user and enables the user to invite nearby devices to a session. To use this class in iOS or tvOS, call methods from the underlying `UIViewController` class ([`prepare(for:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/prepare(for:sender:)) and [`performSegue(withIdentifier:sender:)`](https://developer.apple.com/documentation/UIKit/UIViewController/performSegue(withIdentifier:sender:)) for storyboards or [`present(_:animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/present(_:animated:completion:)) and [`dismiss(animated:completion:)`](https://developer.apple.com/documentation/UIKit/UIViewController/dismiss(animated:completion:)) for nib-based views) to present and dismiss the view controller. In macOS, use the comparable `NSViewController` methods [`presentAsSheet(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/presentAsSheet(_:)) and [`dismiss(_:)`](https://developer.apple.com/documentation/AppKit/NSViewController/dismiss(_:)-91my5) instead.
- [class MCNearbyServiceAdvertiser](mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCNearbyServiceBrowser](mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCSession](mcsession.md)
  An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcpeerid)*