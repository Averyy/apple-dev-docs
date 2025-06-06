# delegate

**Framework**: Nearby Interaction  
**Kind**: property

An object that the framework notifies of session events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- watchOS 7.3+

## Declaration

```swift
weak var delegate: (any NISessionDelegate)? { get set }
```

#### Discussion

An app must set a delegate to receive the peer’s distance and direction information through [`session(_:didUpdate:)`](nisessiondelegate/session(_:didupdate:).md). The [`session(_:didInvalidateWith:)`](nisessiondelegate/session(_:didinvalidatewith:).md) and [`session(_:didRemove:reason:)`](nisessiondelegate/session(_:didremove:reason:).md) callbacks notify you when the session invalidated or removed a peer. The system may suspend an interaction session for various reasons (see [`sessionWasSuspended(_:)`](nisessiondelegate/sessionwassuspended(_:).md)), such as when the peer backgrounds the app.

## See Also

- [func pause()](nisession/pause.md)
  Stops sending distance and direction updates to the peer.
- [func invalidate()](nisession/invalidate.md)
  Stops a running session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/delegate)*