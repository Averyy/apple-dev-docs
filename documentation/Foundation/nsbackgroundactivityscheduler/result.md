# NSBackgroundActivityScheduler.Result

**Framework**: Foundation  
**Kind**: enum

These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum Result
```

## Topics

### Constants
- [NSBackgroundActivityScheduler.Result.finished](nsbackgroundactivityscheduler/result/finished.md)
  The activity has finished executing. If the activity repeats, the next invocation is scheduled by the system.
- [NSBackgroundActivityScheduler.Result.deferred](nsbackgroundactivityscheduler/result/deferred.md)
  System conditions have changed since the time the activity began executing, and deferral of additional work is recommended.
- [NSBackgroundActivityScheduler.Result.finished](nsbackgroundactivityscheduler/result/finished.md)
  The activity has finished executing. If the activity repeats, the next invocation is scheduled by the system.
- [NSBackgroundActivityScheduler.Result.deferred](nsbackgroundactivityscheduler/result/deferred.md)
  System conditions have changed since the time the activity began executing, and deferral of additional work is recommended.
### Initializers
- [init?(rawValue: Int)](nsbackgroundactivityscheduler/result/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum QualityOfService](qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result)*