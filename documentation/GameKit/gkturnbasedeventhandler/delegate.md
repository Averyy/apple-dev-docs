# delegate

**Framework**: GameKit  
**Kind**: property

The delegate for the event handler.

**Availability**:
- macOS 10.8+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var delegate: (any GKTurnBasedEventHandlerDelegate & NSObjectProtocol)? { get set }
```

#### Discussion

If your game implements turn-based matches, it should set the delegate immediately after the local player is successfully authenticated. You want to set the delegate immediately because your game may have been launched specifically to handle a turn-based match event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/delegate)*