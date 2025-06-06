# delegate

**Framework**: GameKit  
**Kind**: property

The delegate for the event handler.

**Availability**:
- macOS 10.8+
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any GKChallengeEventHandlerDelegate)! { get set }
```

#### Discussion

Only access this property from your game’s main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/delegate)*