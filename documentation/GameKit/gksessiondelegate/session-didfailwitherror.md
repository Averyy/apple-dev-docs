# session(_:didFailWithError:)

**Framework**: GameKit  
**Kind**: method

Sent to the delegate when a serious error has occurred in the session.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
optional func session(_ session: GKSession, didFailWithError error: any Error)
```

#### Discussion

This method is called when a serious internal error occurred in the session. Your application should disconnect the session from other peers and release the session.

## Parameters

- `session`: The session that failed.
- `error`: The error that occurred.

## See Also

- [func session(GKSession, connectionWithPeerFailed: String, withError: any Error)](gksessiondelegate/session(_:connectionwithpeerfailed:witherror:).md)
  Received by the delegate when an attempt to connect to another peer failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksessiondelegate/session(_:didfailwitherror:))*