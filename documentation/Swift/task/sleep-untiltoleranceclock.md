# sleep(until:tolerance:clock:)

**Framework**: Swift  
**Kind**: method

Suspends the current task until the given deadline within a tolerance.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static func sleep<C>(until deadline: C.Instant, tolerance: C.Instant.Duration? = nil, clock: C = ContinuousClock()) async throws where C : Clock
```

#### Discussion

If the task is canceled before the time ends, this function throws `CancellationError`.

This function doesn’t block the underlying thread.

```swift
  try await Task.sleep(until: .now + .seconds(3))
```

## See Also

- [static func yield() async](task/yield.md)
  Suspends the current task and allows other tasks to execute.
- [static func sleep(nanoseconds: UInt64) async throws](task/sleep(nanoseconds:).md)
  Suspends the current task for at least the given duration in nanoseconds.
- [static func sleep<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(for:tolerance:clock:).md)
  Suspends the current task for the given duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/sleep(until:tolerance:clock:))*