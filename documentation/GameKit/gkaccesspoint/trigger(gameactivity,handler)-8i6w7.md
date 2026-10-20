# trigger(gameActivity:handler:)

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method

Displays the game activity view for the provided activity instance.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func trigger(gameActivity: GKGameActivity, handler: (@Sendable () -> Void)? = nil)
```

```swift
func trigger(gameActivity: GKGameActivity) async
```

```objc
- (void) triggerAccessPointWithGameActivity:(GKGameActivity *) gameActivity handler:(void (^)()) handler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/trigger(gameactivity:handler:)-8i6w7)*