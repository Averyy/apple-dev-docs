# ActivityState.active

**Framework**: ActivityKit  
**Kind**: case  
**Role**: Case

The Live Activity is active, visible, and can receive content updates.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+

## Declaration

```swift
case active
```

## See Also

### Live Activity states
- [ActivityState.dismissed](./dismissed.md)
  The Live Activity ended and is no longer visible because a person or the system removed it.
- [ActivityState.pending](./pending.md)
  The Live Activity is scheduled to start at a specified date but hasn’t started yet.
- [ActivityState.stale](./stale.md)
  The Live Activity content is out of date and needs an update.
- [ActivityState.ended](./ended.md)
  The Live Activity is visible, but a person, the app, or the system ended it, and it won’t update its content anymore.


---

*[View on Apple Developer](https://developer.apple.com/documentation/activitykit/activitystate/active)*