# Clock Implementations

**Framework**: Swift

## Topics

### Instance Properties
- [var minimumResolution: Duration](continuousclock/minimumresolution.md)
  The minimum non-zero resolution between any two calls to `now`.
- [var now: ContinuousClock.Instant](continuousclock/now-swift.property.md)
  The current continuous instant.
### Instance Methods
- [func measure(() throws -> Void) rethrows -> Self.Instant.Duration](continuousclock/measure(_:).md)
  Measure the elapsed time to execute a closure.
- [func measure(isolation: isolated (any Actor)?, () async throws -> Void) async rethrows -> Self.Instant.Duration](continuousclock/measure(isolation:_:).md)
  Measure the elapsed time to execute an asynchronous closure.
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