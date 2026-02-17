# Clock Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var minimumResolution: Duration](suspendingclock/minimumresolution.md)
  The minimum non-zero resolution between any two calls to `now`.
- [var now: SuspendingClock.Instant](suspendingclock/now-swift.property.md)
  The current instant accounting for machine suspension.
- [var traits: ClockTraits](suspendingclock/traits.md)
- [var traits: ClockTraits](suspendingclock/traits-2kk1s.md)
### Instance Methods
- [func convert(from: Self.Duration) -> Duration?](suspendingclock/convert(from:)-3gyqg.md)
- [func convert(from: Self.Duration) -> Self.Duration?](suspendingclock/convert(from:)-7914d.md)
- [func convert(from: Duration) -> Self.Duration?](suspendingclock/convert(from:)-mpdo.md)
- [func convert<OtherClock>(instant: OtherClock.Instant, from: OtherClock) -> Self.Instant?](suspendingclock/convert(instant:from:).md)
- [func enqueue(consuming ExecutorJob, on: some Executor, at: SuspendingClock.Instant, tolerance: Duration?)](suspendingclock/enqueue(_:on:at:tolerance:).md)
  Enqueue the given job on the specified executor at some point after the given instant.
- [func enqueue(consuming ExecutorJob, on: some Executor, at: Self.Instant, tolerance: Self.Duration?)](suspendingclock/enqueue(_:on:at:tolerance:)-6fvj5.md)
  Enqueue the given job on the specified executor at some point after the given instant.
- [func measure(() throws -> Void) rethrows -> Self.Instant.Duration](suspendingclock/measure(_:).md)
  Measure the elapsed time to execute a closure.
- [func measure(isolation: isolated (any Actor)?, () async throws -> Void) async rethrows -> Self.Instant.Duration](suspendingclock/measure(isolation:_:).md)
  Measure the elapsed time to execute an asynchronous closure.
- [func run(consuming ExecutorJob, at: SuspendingClock.Instant, tolerance: Duration?)](suspendingclock/run(_:at:tolerance:).md)
  Run the given job on an unspecified executor at some point after the given instant.
- [func run(consuming ExecutorJob, at: Self.Instant, tolerance: Self.Duration?)](suspendingclock/run(_:at:tolerance:)-45gka.md)
  Run the given job on an unspecified executor at some point after the given instant.
- [func sleep(for: Self.Instant.Duration, tolerance: Self.Instant.Duration?) async throws](suspendingclock/sleep(for:tolerance:).md)
  Suspends for the given duration.
- [func sleep(until: SuspendingClock.Instant, tolerance: Duration?) async throws](suspendingclock/sleep(until:tolerance:).md)
  Suspend task execution until a given deadline within a tolerance. If no tolerance is specified then the system may adjust the deadline to coalesce CPU wake-ups to more efficiently process the wake-ups in a more power efficient manner.
### Type Aliases
- [SuspendingClock.Duration](suspendingclock/duration.md)
### Type Properties
- [static var suspending: SuspendingClock](suspendingclock/suspending.md)
  A clock that measures time that always increments but stops incrementing while the system is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/suspendingclock/clock-implementations)*