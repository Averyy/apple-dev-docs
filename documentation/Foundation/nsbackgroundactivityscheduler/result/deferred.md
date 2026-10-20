# NSBackgroundActivityScheduler.Result.deferred

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

System conditions have changed since the time the activity began executing, and deferral of additional work is recommended.

**Availability**:
- macOS 10.10+

## Declaration

```swift
case deferred
```

```c
NSBackgroundActivityResultDeferred
```

## See Also

### Constants
- [NSBackgroundActivityScheduler.Result.finished](./finished.md)
  The activity has finished executing. If the activity repeats, the next invocation is scheduled by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result/deferred)*