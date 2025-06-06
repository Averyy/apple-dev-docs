# sessionWasSuspended(_:)

**Framework**: Nearby Interaction  
**Kind**: method

Notifies you of a suspended session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
optional func sessionWasSuspended(_ session: NISession)
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

When NI invokes this callback, the session suspends and doesn’t receive [`session(_:didUpdate:)`](nisessiondelegate/session(_:didupdate:).md) callbacks. NI suspends a session when the user backgrounds the app. If the user reactivates the app before NI times out the session, NI calls [`sessionSuspensionEnded(_:)`](nisessiondelegate/sessionsuspensionended(_:).md). A suspended session won’t resume on its own. To resume the session, call [`run(_:)`](nisession/run(_:).md) again, passing in your session’s configuration.

If the app stays backgrounded for too long during a suspension, NI invalidates the session (see [`session(_:didInvalidateWith:)`](nisessiondelegate/session(_:didinvalidatewith:).md)) and the peer user’s session invokes [`session(_:didRemove:reason:)`](nisessiondelegate/session(_:didremove:reason:).md) with `reason` [`NINearbyObject.RemovalReason.timeout`](ninearbyobject/removalreason/timeout.md).

Additionally, the system may suspend a session for internal reasons.

## Parameters

- `session`: The session that NI suspended.

## See Also

- [func sessionSuspensionEnded(NISession)](nisessiondelegate/sessionsuspensionended(_:).md)
  Notifies you of the end of a session’s suspension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/sessionwassuspended(_:))*