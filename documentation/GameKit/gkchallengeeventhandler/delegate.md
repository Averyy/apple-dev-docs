# delegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the event handler.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 6.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: No longer supported.

## Declaration

```swift
weak var delegate: (any GKChallengeEventHandlerDelegate)! { get set }
```

```objc
@property (nonatomic, weak) id<GKChallengeEventHandlerDelegate> delegate;
```

#### Discussion

Only access this property from your game’s main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkchallengeeventhandler/delegate)*