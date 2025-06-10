# MCSession

**Framework**: Multipeer Connectivity  
**Kind**: class

An `MCSession` object enables and manages communication among all peers in a Multipeer Connectivity session.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MCSession
```

##### Initiating a Session

To set up a session:

1. Use the [`init(displayName:)`](mcpeerid/init(displayname:).md) method of the [`MCPeerID`](mcpeerid.md) to create a peer ID that represents the local peer, or retrieve a peer ID that you previously archived (to maintain a stable peer ID over time).
2. Use the peer ID with the method [`init(peer:)`](mcsession/init(peer:).md) to initialize the session object.
3. Invite peers to join the session using an [`MCNearbyServiceBrowser`](mcnearbyservicebrowser.md) object, an [`MCBrowserViewController`](mcbrowserviewcontroller.md) object, or your own peer discovery code. (Sessions currently support up to 8 peers, including the local peer.)
4. Set up an [`MCNearbyServiceAdvertiser`](mcnearbyserviceadvertiser.md) object or [`MCAdvertiserAssistant`](mcadvertiserassistant.md) object to allow other devices to ask your app to join a session that they create.

If you use one of the framework’s browser objects for peer discovery, when a peer accepts an invitation, the session calls its delegate object’s [`session(_:peer:didChange:)`](mcsessiondelegate/session(_:peer:didchange:).md) method with [`MCSessionState.connected`](mcsessionstate/connected.md) as the new state, along with an object that tells you which peer became connected. See Creating a Session for related methods.

If instead you write your own peer discovery code, you are responsible for managing the connection manually. See the [`Managing Peers Manually`](mcsession#Managing-Peers-Manually.md) section for more information.

##### Communicating with Peers

Once you have set up the session, your app can send data to other peers by calling one of the following methods, found in Sending Data and Resources:

- [`send(_:toPeers:with:)`](mcsession/send(_:topeers:with:).md) sends an `NSData` object to the specified peers. On each recipient device, the delegate object’s [`session(_:didReceive:fromPeer:)`](mcsessiondelegate/session(_:didreceive:frompeer:).md) method is called with the data object when the data has been fully received.
- [`sendResource(at:withName:toPeer:withCompletionHandler:)`](mcsession/sendresource(at:withname:topeer:withcompletionhandler:).md) sends the contents from an `NSURL` object to the specified peer. The URL can be either a local file URL or a web URL. The `completionHandler` block is called when the resource is fully received by the recipient peer or when an error occurs during transmission. This method returns an `NSProgress` object that you can use to cancel the transfer or check the current status of the transfer. On the recipient device, the session calls its delegate object’s [`session(_:didStartReceivingResourceWithName:fromPeer:with:)`](mcsessiondelegate/session(_:didstartreceivingresourcewithname:frompeer:with:).md) method when the device begins receiving the resource, and calls its [`session(_:didFinishReceivingResourceWithName:fromPeer:at:withError:)`](mcsessiondelegate/session(_:didfinishreceivingresourcewithname:frompeer:at:witherror:).md) method when the resource has been fully received or when an error occurs.
- [`startStream(withName:toPeer:)`](mcsession/startstream(withname:topeer:).md) creates a connected byte stream (`NSOutputStream`) that you can use to send data to the specified peer. On the recipient device, the session calls its delegate object’s [`session(_:didReceive:withName:fromPeer:)`](mcsessiondelegate/session(_:didreceive:withname:frompeer:).md) method with an `NSInputStream` object that represents the other endpoint of communication. On both sides, your code must set the stream’s delegate, schedule the stream on a run loop, and open the stream. Your code must also implement stream delegate methods to manage sending and receiving stream data.

> ❗ **Important**:  Delegate calls occur on a private operation queue. If your app needs to perform an action on a particular run loop or operation queue, its delegate method should explicitly dispatch or schedule that work.

##### Managing Peers Manually

If instead of using the framework’s browser and advertiser objects to perform peer discovery, you decide to write your own peer discovery code (with `NSNetService` or the Bonjour C API, for example), you can manually connect nearby peers into a session. To do this:

1. Establish a connection from your app to nearby peers, and exchange peer IDs with those peers.

Each peer should serialize its own local `MCPeerID` object with `NSKeyedArchiver`, and the receiving peer should unserialize it with `NSKeyedUnarchiver`.

> ❗ **Important**:  Do not attempt to construct a peer ID object for a nonlocal peer using [`init(displayName:)`](mcpeerid/init(displayname:).md). A peer ID object must be constructed .

1. Exchange connection data. After you have obtained the nearby peer’s ID object, call [`nearbyConnectionData(forPeer:withCompletionHandler:)`](mcsession/nearbyconnectiondata(forpeer:withcompletionhandler:).md) to obtain a connection data object specific to that nearby peer.

When the completion handler block is called, send the resulting connection data object to that peer.

> **Note**:  Each device in the session must perform this step for each nonlocal peer in the session. So if there are four devices in the session, each device must generate a connection data object for each of the other three devices.

1. When your app receives connection data from another peer, it must call [`connectPeer(_:withNearbyConnectionData:)`](mcsession/connectpeer(_:withnearbyconnectiondata:).md) to add that peer to the session.

> **Note**:  Each of the nonlocal peers must also call [`connectPeer(_:withNearbyConnectionData:)`](mcsession/connectpeer(_:withnearbyconnectiondata:).md) with the connection data that it received from your app and other nonlocal peers.

You can also cancel an outstanding connection attempt by calling [`cancelConnectPeer(_:)`](mcsession/cancelconnectpeer(_:).md). These methods are described in the Managing Peers Manually group.

##### Disconnecting

To leave a session, your app must call [`disconnect()`](mcsession/disconnect().md). For more details, see Leaving a Session.

## Topics

### Creating a Session
- [convenience init(peer: MCPeerID)](mcsession/init(peer:).md)
  Creates a Multipeer Connectivity session.
- [init(peer: MCPeerID, securityIdentity: [Any]?, encryptionPreference: MCEncryptionPreference)](mcsession/init(peer:securityidentity:encryptionpreference:).md)
  Creates a Multipeer Connectivity session, providing security information.
- [var delegate: (any MCSessionDelegate)?](mcsession/delegate.md)
  The delegate object that handles session-related events.
- [var encryptionPreference: MCEncryptionPreference](mcsession/encryptionpreference.md)
  A value indicating whether the connection prefers encrypted connections, unencrypted connections, or has no preference.
- [var myPeerID: MCPeerID](mcsession/mypeerid.md)
  A local identifier that represents the device on which your app is currently running.
- [var securityIdentity: [Any]?](mcsession/securityidentity.md)
  The security identity of the local peer.
### Managing Peers Manually
- [func connectPeer(MCPeerID, withNearbyConnectionData: Data)](mcsession/connectpeer(_:withnearbyconnectiondata:).md)
  Call this method to connect a peer to the session when using your own service discovery code instead of an  `MCNearbyServiceBrowser` or `MCBrowserViewController` object.
- [func cancelConnectPeer(MCPeerID)](mcsession/cancelconnectpeer(_:).md)
  Cancels an attempt to connect to a peer.
- [var connectedPeers: [MCPeerID]](mcsession/connectedpeers.md)
  An array of all peers that are currently connected to this session.
- [func nearbyConnectionData(forPeer: MCPeerID, withCompletionHandler: (Data?, (any Error)?) -> Void)](mcsession/nearbyconnectiondata(forpeer:withcompletionhandler:).md)
  Obtains connection data for the specified peer.
### Sending Data and Resources
- [func send(Data, toPeers: [MCPeerID], with: MCSessionSendDataMode) throws](mcsession/send(_:topeers:with:).md)
  Sends a message to nearby peers.
- [func sendResource(at: URL, withName: String, toPeer: MCPeerID, withCompletionHandler: (((any Error)?) -> Void)?) -> Progress?](mcsession/sendresource(at:withname:topeer:withcompletionhandler:).md)
  Sends the contents of a URL to a peer.
- [func startStream(withName: String, toPeer: MCPeerID) throws -> OutputStream](mcsession/startstream(withname:topeer:).md)
  Opens a byte stream to a nearby peer.
### Leaving a Session
- [func disconnect()](mcsession/disconnect.md)
  Disconnects the local peer from the session.
### Constants
- [enum MCSessionSendDataMode](mcsessionsenddatamode.md)
  Indicates whether delivery of data should be guaranteed.
- [enum MCSessionState](mcsessionstate.md)
  Indicates the current state of a given peer within a session.
- [enum MCEncryptionPreference](mcencryptionpreference.md)
  Indicates whether a session should use encryption when communicating with nearby peers.
- [MCError.Code](mcerror/code.md)
  Error codes found in [`MCErrorDomain`](mcerrordomain.md) error domain `NSError` objects returned by methods in the Multipeer Connectivity framework.
- [Multipeer Connectivity Error Domain](multipeer_connectivity_error_domain.md)
  The error domain for errors specific to Multipeer Connectivity.
- [Minimum and Maximum Supported Peers](minimum_and_maximum_supported_peers.md)
  Constants that define the minimum and maximum number of peers supported in a session.

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
- [class MCNearbyServiceAdvertiser](mcnearbyserviceadvertiser.md)
  The `MCNearbyServiceAdvertiser` class publishes an advertisement for a specific service that your app provides through the Multipeer Connectivity framework and notifies its delegate about invitations from nearby peers.
- [class MCNearbyServiceBrowser](mcnearbyservicebrowser.md)
  Searches (by service type) for services offered by nearby devices using infrastructure Wi-Fi, peer-to-peer Wi-Fi, and Bluetooth (in iOS) or Ethernet (in macOS and tvOS), and provides the ability to easily invite those devices to a Multipeer Connectivity session (`MCSession`).
- [class MCPeerID](mcpeerid.md)
  An  `MCPeerID` object represents a peer in a multipeer session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcsession)*