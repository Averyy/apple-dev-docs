# actionWasDiscarded(_:)

**Framework**: TabletopKit  
**Kind**: method  
**Required**: Yes

Called once for every local action that is discarded because there is insufficient space to enqueue and become pending. Every local action will, in order, generate either an `actionIsPending` or `actionWasDiscarded` callback in the next update after it was added.

**Availability**:
- visionOS 26.0+ (Beta)

## Declaration

```swift
func actionWasDiscarded(_ action: some TabletopAction)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopgame/observer/actionwasdiscarded(_:))*