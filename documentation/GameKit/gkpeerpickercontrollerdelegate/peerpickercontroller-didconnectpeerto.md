# peerPickerController(_:didConnectPeer:to:)

**Framework**: GameKit  
**Kind**: method

Tells the delegate that the controller connected a peer to the session.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
optional func peerPickerController(_ picker: GKPeerPickerController, didConnectPeer peerID: String, to session: GKSession)
```

#### Discussion

Once a peer is connected to the session, your application should take ownership of the session, dismiss the peer picker, and then use the session to communicate with the other peer.

> ❗ **Important**:  Although optional in the protocol, Game Kit expects your application to implement this method.

 Although optional in the protocol, Game Kit expects your application to implement this method.

## Parameters

- `picker`: The controller that connected the peer.
- `peerID`: The identification string for the peer that connected to the session.
- `session`: The session that the peer is connected to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/peerpickercontroller(_:didconnectpeer:to:))*