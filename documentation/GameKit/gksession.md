# GKSession

**Framework**: GameKit  
**Kind**: class

A [`GKSession`](gksession.md) object provides the ability to discover and connect to nearby iOS devices using Bluetooth or Wi-fi.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class GKSession
```

#### Overview

Sessions primarily work with . A peer is any iOS device made visible by creating and configuring a [`GKSession`](gksession.md) object. Each peer is identified by a unique identifier, called a peer id ([`peerID`](gksession/peerid.md)) string. Your application can use a [`peerID`](gksession/peerid.md) string to obtain a user-readable name for a remote peer and to attempt to connect to that peer. Similarly, your session’s peer ID is visible to other nearby peers. After a connection is established, your application uses the remote peer’s ID to address data packets that it wants to send.

Peers discover other peers by using a unique string to identify the service they implement, called a session ID ([`sessionID`](gksession/sessionid.md)). Sessions can be configured to broadcast a session ID (as a ), to search for other peers advertising with that session ID (as a ), or to act as both a server and a client simultaneously (as a .

Your application controls the behavior of a session through a delegate that implements the [`GKSessionDelegate`](gksessiondelegate.md) protocol. The delegate is called when remote peers are discovered, when those peers attempt to connect to the session, and when the state of a remote peer changes. Your application also provides a data handler to the session so that the session can forward data it receives from remote peers. The data handler can be a separate object or the same object as the delegate.

When Bluetooth is turned on, Wi-Fi download speeds drastically decrease while the device is searching for other Bluetooth enabled devices. After the Bluetooth discovery time has completed, Wi-Fi speeds return to normal.

[`GKSession`](gksession.md) methods are thread-safe and may be called from any thread. However, the session always calls its delegate on the main thread.

## Topics

### Creating a Session
- [init!(sessionID: String!, displayName: String!, sessionMode: GKSessionMode)](gksession/init(sessionid:displayname:sessionmode:).md)
  Initializes and returns a newly allocated session.
### Setting and Getting the Delegate
- [var delegate: (any GKSessionDelegate)!](gksession/delegate.md)
  The delegate of the session object.
### Searching for Other Peers
- [var isAvailable: Bool](gksession/isavailable.md)
  A Boolean value that determines whether or not the session wants to connect to new peers.
### Obtaining Information About Other Peers
- [func peers(with: GKPeerConnectionState) -> [Any]!](gksession/peers(with:).md)
  Returns a list of peers in the specified connection state.
- [func displayName(forPeer: String!) -> String!](gksession/displayname(forpeer:).md)
  Returns a user-readable name for a peer.
### Connecting to a Remote Peer
- [func connect(toPeer: String!, withTimeout: TimeInterval)](gksession/connect(topeer:withtimeout:).md)
  Creates a connection to another iOS device.
- [func cancelConnect(toPeer: String!)](gksession/cancelconnect(topeer:).md)
  Cancels a pending request to connect to another iOS device.
### Receiving Connections from a Remote Peer
- [func acceptConnection(fromPeer: String!) throws](gksession/acceptconnection(frompeer:).md)
  Called by the delegate to accept a connection request received from a remote peer.
- [func denyConnection(fromPeer: String!)](gksession/denyconnection(frompeer:).md)
  Called by the delegate to reject a connection request received from a remote peer.
### Working with Connected Peers
- [func setDataReceiveHandler(Any!, withContext: UnsafeMutableRawPointer!)](gksession/setdatareceivehandler(_:withcontext:).md)
  Sets the object that handles data received from other peers connected to the session.
- [func send(Data!, toPeers: [Any]!, with: GKSendDataMode) throws](gksession/send(_:topeers:with:).md)
  Transmits a collection of bytes to a list of connected peers.
- [func sendData(toAllPeers: Data!, with: GKSendDataMode) throws](gksession/senddata(toallpeers:with:).md)
  Transmits a collection of bytes to all connected peers.
- [var disconnectTimeout: TimeInterval](gksession/disconnecttimeout.md)
  A time interval that expresses how long the session waits before it disconnects a nonresponsive peer.
- [func disconnectFromAllPeers()](gksession/disconnectfromallpeers.md)
  Disconnects the session from all connected peers.
- [func disconnectPeer(fromAllPeers: String!)](gksession/disconnectpeer(fromallpeers:).md)
  Disconnects a connected peer from all peers connected to the session.
### Information about the Session
- [var displayName: String!](gksession/displayname.md)
  The name of the user.
- [var peerID: String!](gksession/peerid.md)
  A string that identifies your session to other peers.
- [var sessionID: String!](gksession/sessionid.md)
  A string used to filter the list of peers who are allowed to see your session.
- [var sessionMode: GKSessionMode](gksession/sessionmode.md)
  The mode the session uses to find other peers.
### Constants
- [enum GKSendDataMode](gksenddatamode.md)
  The mechanism used to transmit data to other peers.
- [enum GKSessionMode](gksessionmode.md)
  Modes that determine how a session interacts with other peers.
- [enum GKPeerConnectionState](gkpeerconnectionstate.md)
  The state of a peer known to the session.
- [The Session Error Domain](the-session-error-domain.md)
  The [`GKSession`](gksession.md) error domain.
- [GKSessionError.Code](gksessionerror-swift.struct/code.md)
  Error codes for the session error domain.
- [struct GKSessionError](gksessionerror-swift.struct.md)

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

- [class GKAchievementViewController](gkachievementviewcontroller.md)
  An `GKAchievementViewController` object provides a standard user interface to display achievement progress for the local player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKChallengeEventHandler](gkchallengeeventhandler.md)
  The `GKChallengeEventHandler` class is used to respond to events related to challenges sent or received by the local player.
- [class GKChallengesViewController](gkchallengesviewcontroller.md)
- [class GKCloudPlayer](gkcloudplayer.md)
  The object representing the currently signed-in iCloud user.
- [class GKGameSession](gkgamesession.md)
  A game session you can use to save game data, invite other players, and create turn-based and real-time game apps.
- [class GKGameSessionSharingViewController](gkgamesessionsharingviewcontroller.md)
  A user interface you can use to invite other users into a tvOS game session.
- [class GKFriendRequestComposeViewController](gkfriendrequestcomposeviewcontroller.md)
  Your game uses the `GKFriendRequestComposeViewController` class to present a screen that allows the local player to send friend requests to other players.
- [class GKLeaderboardViewController](gkleaderboardviewcontroller.md)
  The `GKLeaderboardViewController` class provides a standard user interface that displays leaderboard scores to the player. If the [`GKGameCenterViewController`](gkgamecenterviewcontroller.md) class is available, you should use it instead.
- [class GKPeerPickerController](gkpeerpickercontroller.md)
  Provides a standard user interface to allow one iOS device to discover and connect to another.
- [class GKScore](gkscore.md)
  An object containing information for a score that was earned by the player.
- [class GKTurnBasedEventHandler](gkturnbasedeventhandler.md)
  The [`GKTurnBasedEventHandler`](gkturnbasedeventhandler.md) class is used to respond to important messages related to turn-based matches. To use it, call the [`shared()`](gkturnbasedeventhandler/shared().md) class method to get the singleton instance and assign an object that implements the [`GKTurnBasedEventHandlerDelegate`](gkturnbasedeventhandlerdelegate.md) protocol to its [`delegate`](gkturnbasedeventhandler/delegate.md) property. All methods are called on the main thread.
- [class GKVoiceChat](gkvoicechat.md)
  A voice channel that allows players to speak with each other in a multiplayer game.
- [class GKVoiceChatService](gkvoicechatservice.md)
  The [`GKVoiceChatService`](gkvoicechatservice.md) class allows your application to connect two iOS devices into a voice chat.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession)*