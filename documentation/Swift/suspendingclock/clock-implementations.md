# Clock Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var minimumResolution: Duration](suspendingclock/minimumresolution.md)
  The minimum non-zero resolution between any two calls to `now`.
- [var now: SuspendingClock.Instant](suspendingclock/now-swift.property.md)
  The current instant accounting for machine suspension.
- [var traits: ClockTraits](suspendingclock/traits.md)
  The suspending clock is monotonic
- [var traits: ClockTraits](suspendingclock/traits-2kk1s.md)
  The traits associated with this clock instance.
### Instance Methods
- [func convert(from: Self.Duration) -> Duration?](suspendingclock/convert(from:)-3gyqg.md)
  Convert a Clock-specific Duration to a Swift Duration
- [func convert(from: Self.Duration) -> Self.Duration?](suspendingclock/convert(from:)-7914d.md)
- [func convert(from: Duration) -> Self.Duration?](suspendingclock/convert(from:)-mpdo.md)
  Convert a Swift Duration to a Clock-specific Duration
- [func convert<OtherClock>(instant: OtherClock.Instant, from: OtherClock) -> Self.Instant?](suspendingclock/convert(instant:from:).md)
  Convert an `Instant` from some other clock’s `Instant`
- [func measure(() throws -> Void) rethrows -> Self.Instant.Duration](suspendingclock/measure(_:).md)
  Measure the elapsed time to execute a closure.
- [func measure(isolation: isolated (any Actor)?, () async throws -> Void) async rethrows -> Self.Instant.Duration](suspendingclock/measure(isolation:_:).md)
  Measure the elapsed time to execute an asynchronous closure.
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