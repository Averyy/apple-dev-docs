# session(_:connectionWithPeerFailed:withError:)

**Framework**: GameKit  
**Kind**: method

Received by the delegate when an attempt to connect to another peer failed.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func session(_ session: GKSession, connectionWithPeerFailed peerID: String, withError error: any Error)
```

#### Discussion

The `error` parameter can be used to inform the user of why the connection failed.

> ❗ **Important**:  If a [`GKPeerPickerController`](gkpeerpickercontroller.md) object is being used to configure the session, the controller handles this message automatically. Your delegate can ignore it if the peer picker dialog is in use.

 If a [`GKPeerPickerController`](gkpeerpickercontroller.md) object is being used to configure the session, the controller handles this message automatically. Your delegate can ignore it if the peer picker dialog is in use.

## Parameters

- `session`: The session that received the message.
- `peerID`: A string that uniquely identifies the peer.
- `error`: The error that occurred.

## See Also

- [func session(GKSession, didFailWithError: any Error)](gksessiondelegate/session(_:didfailwitherror:).md)
  Sent to the delegate when a serious error has occurred in the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessiondelegate/session(_:connectionwithpeerfailed:witherror:))*