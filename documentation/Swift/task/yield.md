# yield()

**Framework**: Swift  
**Kind**: method

Suspends the current task and allows other tasks to execute.

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
static func yield() async
```

#### Discussion

A task can voluntarily suspend itself in the middle of a long-running operation that doesn’t contain any suspension points, to let other tasks run for a while before execution returns to this task.

If this task is the highest-priority task in the system, the executor immediately resumes execution of the same task. As such, this method isn’t necessarily a way to avoid resource starvation.

## See Also

- [static func sleep(nanoseconds: UInt64) async throws](task/sleep(nanoseconds:).md)
  Suspends the current task for at least the given duration in nanoseconds.
- [static func sleep<C>(for: C.Instant.Duration, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(for:tolerance:clock:).md)
  Suspends the current task for the given duration.
- [static func sleep<C>(until: C.Instant, tolerance: C.Instant.Duration?, clock: C) async throws](task/sleep(until:tolerance:clock:).md)
  Suspends the current task until the given deadline within a tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/task/yield())*