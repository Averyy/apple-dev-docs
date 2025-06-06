# schedule(_:)

**Framework**: Foundation  
**Kind**: method

Begins scheduling the background activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func schedule(_ block: @escaping (@escaping NSBackgroundActivityScheduler.CompletionHandler) -> Void)
```

#### Discussion

When your block is called, it’s passed a completion handler as an argument. Configure the block to invoke this handler, passing it a result of type [`NSBackgroundActivityScheduler.Result`](nsbackgroundactivityscheduler/result.md) to indicate whether the activity finished ([`NSBackgroundActivityScheduler.Result.finished`](nsbackgroundactivityscheduler/result/finished.md)) or should be deferred ([`NSBackgroundActivityScheduler.Result.deferred`](nsbackgroundactivityscheduler/result/deferred.md)) and rescheduled for a later time. Failure to invoke the completion handler results in the activity not being rescheduled. For work that will be deferred and rescheduled, the block may optionally adjust scheduler properties, such as [`interval`](nsbackgroundactivityscheduler/interval.md) or [`tolerance`](nsbackgroundactivityscheduler/tolerance.md), before calling the completion handler. See [`Schedule Activity with scheduleWithBlock:`](nsbackgroundactivityscheduler#Schedule-Activity-with-scheduleWithBlock.md).

## Parameters

- `block`: A block of code to execute when the scheduler runs. This block will be called on a serial background queue appropriate for the level of quality of service specified. See  .

## See Also

- [NSBackgroundActivityScheduler.Result](nsbackgroundactivityscheduler/result.md)
  These constants indicate whether background activity has been completed successfully or whether additional processing should be deferred until a more optimal time.
- [NSBackgroundActivityScheduler.CompletionHandler](nsbackgroundactivityscheduler/completionhandler.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsbackgroundactivityscheduler/schedule(_:))*