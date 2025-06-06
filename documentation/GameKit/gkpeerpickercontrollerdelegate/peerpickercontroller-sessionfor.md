# peerPickerController(_:sessionFor:)

**Framework**: GameKit  
**Kind**: method

Asks the delegate to return a session for the specified connection type.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
optional func peerPickerController(_ picker: GKPeerPickerController, sessionFor type: GKPeerPickerConnectionType) -> GKSession
```

#### Discussion

Your delegate is responsible for providing a [`GKSession`](gksession.md) to use to find and connect to other devices. When the peer picker needs a session, it calls this method. Your application can either create a new session or return a previously created session to the peer picker. The session that your application returns to the peer picker must advertise itself as a peer ([`GKSessionMode.peer`](gksessionmode/peer.md)).

If your delegate does not implement this method and the user selected a network of type [`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md), the peer controller allocates a new session that advertises itself as a peer ([`GKSessionMode.peer`](gksessionmode/peer.md)) with the default [`sessionID`](gksession/sessionid.md) and [`displayName`](gksession/displayname.md) parameters.

##### Special Considerations

In iOS 3.0, your delegate receives requests only for networks of type [`GKPeerPickerConnectionType.nearby`](gkpeerpickerconnectiontype/nearby.md).

## Parameters

- `picker`: The controller requesting the session.
- `type`: The type of connection the controller wants to configure.

## See Also

- [func peerPickerController(GKPeerPickerController, didSelect: GKPeerPickerConnectionType)](gkpeerpickercontrollerdelegate/peerpickercontroller(_:didselect:).md)
  Tells the delegate that the user selected a connection type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkpeerpickercontrollerdelegate/peerpickercontroller(_:sessionfor:))*