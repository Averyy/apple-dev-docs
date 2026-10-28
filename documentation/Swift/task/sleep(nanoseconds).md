# sleep(nanoseconds:)

**Framework**: Swift  
**Kind**: method  
**Role**: Type Method

Suspends the current task for at least the given duration in nanoseconds.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static func sleep(nanoseconds duration: UInt64) async throws
```

Available when `Success` is `Never` and `Failure` is `Never`.

## Discussion

If the task is canceled before the time ends, this function throws `CancellationError`.

This function doesn’t block the underlying thread.

## See Also

### Suspending Execution
- [static func yield() async](./yield%28%29.md)
  Suspends the current task and allows other tasks to execute.
- [static func sleep<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) async throws](./sleep%28for,tolerance,clock%29.md)
  Suspends the current task for the given duration.
- [static func sleep<C>(until: C.Instant, tolerance: C.Instant.Duration?, clock: C) async throws](./sleep%28until,tolerance,clock%29.md)
  Suspends the current task until the given deadline within a tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/sleep(nanoseconds:))*