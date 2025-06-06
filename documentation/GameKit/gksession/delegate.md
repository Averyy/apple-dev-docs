# delegate

**Framework**: GameKit  
**Kind**: property

The delegate of the session object.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var delegate: (any GKSessionDelegate)! { get set }
```

#### Discussion

A session’s delegate is responsible for observing changes to other peers running with the same session ID. Your application must set a delegate before making your session known to other peers.

## See Also

- [protocol GKSessionDelegate](gksessiondelegate.md)
  An object implements the [`GKSessionDelegate`](gksessiondelegate.md) protocol to control the behavior of a [`GKSession`](gksession.md) object. The delegate is called when other visible peers change their state relative to the session. It is also called to determine whether another peer is allowed to connect to the session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gksession/delegate)*