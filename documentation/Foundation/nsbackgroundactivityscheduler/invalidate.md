# invalidate()

**Framework**: Foundation  
**Kind**: method

Prevents the background activity from being scheduled again.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func invalidate()
```

#### Discussion

When `invalidate` is used to stop an activity that is currently executing, the activity will still finish executing.

See [`Stop Activity`](nsbackgroundactivityscheduler#Stop-Activity.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/invalidate())*