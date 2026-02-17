# Clock Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var minimumResolution: Duration](continuousclock/minimumresolution.md)
  The minimum non-zero resolution between any two calls to `now`.
- [var now: ContinuousClock.Instant](continuousclock/now-swift.property.md)
  The current continuous instant.
- [var traits: ClockTraits](continuousclock/traits.md)
- [var traits: ClockTraits](continuousclock/traits-51dx6.md)
### Instance Methods
- [func convert(from: Self.Duration) -> Duration?](continuousclock/convert(from:)-1jlhb.md)
- [func convert(from: Duration) -> Self.Duration?](continuousclock/convert(from:)-3lfde.md)
- [func convert(from: Self.Duration) -> Self.Duration?](continuousclock/convert(from:)-6tuwg.md)
- [func convert<OtherClock>(instant: OtherClock.Instant, from: OtherClock) -> Self.Instant?](continuousclock/convert(instant:from:).md)
- [func enqueue(consuming ExecutorJob, on: some Executor, at: ContinuousClock.Instant, tolerance: Duration?)](continuousclock/enqueue(_:on:at:tolerance:).md)
  Enqueue the given job on the specified executor at some point after the given instant.
- [func enqueue(consuming ExecutorJob, on: some Executor, at: Self.Instant, tolerance: Self.Duration?)](continuousclock/enqueue(_:on:at:tolerance:)-7ff7v.md)
  Enqueue the given job on the specified executor at some point after the given instant.
- [func measure(() throws -> Void) rethrows -> Self.Instant.Duration](continuousclock/measure(_:).md)
  Measure the elapsed time to execute a closure.
- [func measure(isolation: isolated (any Actor)?, () async throws -> Void) async rethrows -> Self.Instant.Duration](continuousclock/measure(isolation:_:).md)
  Measure the elapsed time to execute an asynchronous closure.
- [func run(consuming ExecutorJob, at: ContinuousClock.Instant, tolerance: Duration?)](continuousclock/run(_:at:tolerance:).md)
  Run the given job on an unspecified executor at some point after the given instant.
- [func run(consuming ExecutorJob, at: Self.Instant, tolerance: Self.Duration?)](continuousclock/run(_:at:tolerance:)-4oplv.md)
  Run the given job on an unspecified executor at some point after the given instant.
- [func sleep(for: Self.Instant.Duration, tolerance: Self.Instant.Duration?) async throws](continuousclock/sleep(for:tolerance:).md)
  Suspends for the given duration.
- [func sleep(until: ContinuousClock.Instant, tolerance: Duration?) async throws](continuousclock/sleep(until:tolerance:).md)
  Suspend task execution until a given deadline within a tolerance. If no tolerance is specified then the system may adjust the deadline to coalesce CPU wake-ups to more efficiently process the wake-ups in a more power efficient manner.
### Type Aliases
- [ContinuousClock.Duration](continuousclock/duration.md)
### Type Properties
- [static var continuous: ContinuousClock](continuousclock/continuous.md)
  A clock that measures time that always increments but does not stop incrementing while the system is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/clock-implementations)*