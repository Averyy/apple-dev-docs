# enqueue(_:after:tolerance:clock:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Enqueue a job to run after a specified delay.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- tvOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)
- watchOS 26.4+ (Beta)

## Declaration

```swift
func enqueue<C>(_ job: consuming ExecutorJob, after delay: C.Duration, tolerance: C.Duration?, clock: C) where C : Clock
```

#### Discussion

You need only implement one of the two enqueue functions here; the default implementation for the other will then call the one you have implemented.

Parameters:

- job:       The job to schedule.
- after:     A `Duration` specifying the time after which the job is to run.  The job will not be executed before this time has elapsed.
- tolerance: The maximum additional delay permissible before the job is executed.  `nil` means no limit.
- clock:     The clock used for the delay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/schedulingexecutor/enqueue(_:after:tolerance:clock:))*