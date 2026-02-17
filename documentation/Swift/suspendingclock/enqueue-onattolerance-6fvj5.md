# enqueue(_:on:at:tolerance:)

**Framework**: Swift  
**Kind**: method

Enqueue the given job on the specified executor at some point after the given instant.

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
func enqueue(_ job: consuming ExecutorJob, on executor: some Executor, at instant: Self.Instant, tolerance: Self.Duration?)
```

#### Discussion

The default implementation uses the `run` method to trigger a job that does `executor.enqueue(job)`.  If a particular `Clock` knows that the executor it has been asked to use is the same one that it will run jobs on, it can short-circuit this behaviour and directly use `run` with the original job.

Parameters:

- job:         The job we wish to run
- on executor: The executor on which we would like it to run.
- at instant:  The time at which we would like it to run.
- tolerance:   The ideal maximum delay we are willing to tolerate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/suspendingclock/enqueue(_:on:at:tolerance:)-6fvj5)*