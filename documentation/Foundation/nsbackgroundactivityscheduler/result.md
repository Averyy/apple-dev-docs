# NSBackgroundActivityScheduler.Result

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum Result
```

```c
enum NSBackgroundActivityResult : NSInteger;
```

## Topics

### Constants
- [NSBackgroundActivityScheduler.Result.finished](./result/finished.md)
  The activity has finished executing. If the activity repeats, the next invocation is scheduled by the system.
- [NSBackgroundActivityScheduler.Result.deferred](./result/deferred.md)
  System conditions have changed since the time the activity began executing, and deferral of additional work is recommended.
### Initializers
- [init?(rawValue: Int)](./result/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum QualityOfService](../qualityofservice.md)
  Constants that indicate the nature and importance of work to the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/result)*