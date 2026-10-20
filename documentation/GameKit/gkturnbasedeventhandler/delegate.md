# delegate

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The delegate for the event handler.

**Availability**:
- iOS 5.0+ - Deprecated in 7.0
- iPadOS 5.0+ - Deprecated in 7.0
- Mac Catalyst 5.0+ - Deprecated in 7.0
- macOS 10.8+ - Deprecated in 10.10
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
weak var delegate: (any GKTurnBasedEventHandlerDelegate & NSObjectProtocol)? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, weak) NSObject<GKTurnBasedEventHandlerDelegate> * delegate;
```

*macOS*

```objc
@property (atomic, weak) NSObject<GKTurnBasedEventHandlerDelegate> * delegate;
```

#### Discussion

If your game implements turn-based matches, it should set the delegate immediately after the local player is successfully initialized. You want to set the delegate immediately because your game may have been launched specifically to handle a turn-based match event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkturnbasedeventhandler/delegate)*