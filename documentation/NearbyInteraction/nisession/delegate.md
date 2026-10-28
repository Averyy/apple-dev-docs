# delegate

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, weak, nullable) id<NISessionDelegate> delegate;
```

## Discussion

An app must set a delegate to receive the peer’s distance and direction information through [`session(_:didUpdate:)`](../nisessiondelegate/session%28_,didupdate%29.md). The [`session(_:didInvalidateWith:)`](../nisessiondelegate/session%28_,didinvalidatewith%29.md) and [`session(_:didRemove:reason:)`](../nisessiondelegate/session%28_,didremove,reason%29.md) callbacks notify you when the session invalidated or removed a peer. The system may suspend an interaction session for various reasons (see [`sessionWasSuspended(_:)`](../nisessiondelegate/sessionwassuspended%28_%29.md)), such as when the peer backgrounds the app.

## See Also

### Managing life cycle
- [func pause()](./pause%28%29.md)
  Stops sending distance and direction updates to the peer.
- [func invalidate()](./invalidate%28%29.md)
  Stops a running session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nisession/delegate)*