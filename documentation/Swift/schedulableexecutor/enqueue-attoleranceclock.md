# enqueue(_:at:tolerance:clock:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Enqueue a job to run at a specified time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func enqueue<C>(_ job: consuming ExecutorJob, at instant: C.Instant, tolerance: C.Duration?, clock: C) where C : Clock
```

#### Discussion

You need only implement one of the two enqueue functions here; the default implementation for the other will then call the one you have implemented.

Parameters:

- job:       The job to schedule.
- at:        The `Instant` at which the job should run.  The job will not be executed before this time.
- tolerance: The maximum additional delay permissible before the job is executed.  `nil` means no limit.
- clock:     The clock used for the delay..


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/schedulableexecutor/enqueue(_:at:tolerance:clock:))*