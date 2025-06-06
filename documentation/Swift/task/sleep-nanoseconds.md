# sleep(nanoseconds:)

**Framework**: Swift  
**Kind**: method

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

#### Discussion

If the task is canceled before the time ends, this function throws `CancellationError`.

This function doesn’t block the underlying thread.

## See Also

- [static func yield() async](task/yield.md)
  Suspends the current task and allows other tasks to execute.
- [static func sleep<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(for:tolerance:clock:).md)
  Suspends the current task for the given duration.
- [static func sleep<C>(until: C.Instant, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(until:tolerance:clock:).md)
  Suspends the current task until the given deadline within a tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/sleep(nanoseconds:))*