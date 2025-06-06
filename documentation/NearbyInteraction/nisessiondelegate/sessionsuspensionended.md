# sessionSuspensionEnded(_:)

**Framework**: Nearby Interaction  
**Kind**: method

Notifies you of the end of a session’s suspension.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
optional func sessionSuspensionEnded(_ session: NISession)
```

## Mentions

- [Extending advanced direction finding and ranging](extending-advanced-direction-finding-and-ranging.md)

#### Discussion

NI suspends an interaction session when the user backgrounds the app. NI ends the suspension when the user foregrounds the app again. An app may resume a suspended session only after NI invokes this callback. To resume a session after a suspension ends, call [`run(_:)`](nisession/run(_:).md), passing in your session’s configuration.

Session suspension is a local event. The framework suspends only the user’s session when the user or system event such as a phone call backgrounds the app. However, if the app stays backgrounded for too long during a suspension, NI invalidates the session with [`session(_:didInvalidateWith:)`](nisessiondelegate/session(_:didinvalidatewith:).md) and the peer user’s session invokes [`session(_:didRemove:reason:)`](nisessiondelegate/session(_:didremove:reason:).md) with `reason` [`NINearbyObject.RemovalReason.timeout`](ninearbyobject/removalreason/timeout.md).

## Parameters

- `session`: The session that NI suspended.

## See Also

- [func sessionWasSuspended(NISession)](nisessiondelegate/sessionwassuspended(_:).md)
  Notifies you of a suspended session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/sessionsuspensionended(_:))*