# session(_:didInvalidateWith:)

**Framework**: Nearby Interaction  
**Kind**: method

Notifies you of an invalidated session.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
optional func session(_ session: NISession, didInvalidateWith error: any Error)
```

## Mentions

- [Initiating and maintaining a session](initiating-and-maintaining-a-session.md)

#### Discussion

The delegate of an invalidated session receives no further callbacks, and the app can’t restart the session. To resume peer interaction, remove references to the invalidated session and begin a new session.

## Parameters

- `session`: The invalidated session.
- `error`: The error that invalidated the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisessiondelegate/session(_:didinvalidatewith:))*