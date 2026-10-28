# delegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the session object.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 2.0

> **Deprecated**: No longer supported.

## Declaration

```swift
weak var delegate: (any GKSessionDelegate)! { get set }
```

```objc
@property (weak) id<GKSessionDelegate> delegate;
```

## Discussion

A session’s delegate is responsible for observing changes to other peers running with the same session ID. Your application must set a delegate before making your session known to other peers.

## See Also

### Related Documentation
- [protocol GKSessionDelegate](../gksessiondelegate.md)
  An object implements the [`GKSessionDelegate`](../gksessiondelegate.md) protocol to control the behavior of a [`GKSession`](../gksession.md) object. The delegate is called when other visible peers change their state relative to the session. It is also called to determine whether another peer is allowed to connect to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/delegate)*