# session(_:didReceiveConnectionRequestFromPeer:)

**Framework**: GameKit  
**Kind**: method

Received by the delegate when a remote peer wants to create a connection to the session.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func session(_ session: GKSession, didReceiveConnectionRequestFromPeer peerID: String)
```

#### Discussion

The delegate should call the session’s [`acceptConnection(fromPeer:)`](gksession/acceptconnection(frompeer:).md) method if it wants to accept the connection or the [`denyConnection(fromPeer:)`](gksession/denyconnection(frompeer:).md) method if it wants to refuse the connection.

> ❗ **Important**:  If a [`GKPeerPickerController`](gkpeerpickercontroller.md) object is being used to configure the session, the controller handles this message automatically. Your delegate can ignore it if the peer picker dialog is in use. If your application is not using a [`GKPeerPickerController`](gkpeerpickercontroller.md) object to configure the session, your delegate must implement this method as described above.

## Parameters

- `session`: The session that received the request.
- `peerID`: A string that uniquely identifies the peer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessiondelegate/session(_:didreceiveconnectionrequestfrompeer:))*