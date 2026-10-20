# Clock Implementations

**Framework**: Swift  
**Role**: API Collection

## Topics

### Instance Properties
- [var minimumResolution: Duration](./minimumresolution.md)
  The minimum non-zero resolution between any two calls to `now`.
- [var now: ContinuousClock.Instant](./now-swift.property.md)
  The current continuous instant.
### Instance Methods
- [func measure(() throws -> Void) rethrows -> Self.Instant.Duration](./measure%28_%29-73b0n.md)
  Measure the elapsed time to execute a closure.
- [func measure(nonisolated(nonsending) () async throws -> Void) async rethrows -> Self.Instant.Duration](./measure%28_%29-9npzl.md)
  Measure the elapsed time to execute an asynchronous closure.
- [func measure(isolation: isolated (any Actor)?, () async throws -> Void) async rethrows -> Self.Instant.Duration](./measure%28isolation,_%29.md)
- [func sleep(for: Self.Instant.Duration, tolerance: Self.Instant.Duration?) async throws](./sleep%28for,tolerance%29.md)
  Suspends for the given duration.
- [func sleep(until: ContinuousClock.Instant, tolerance: Duration?) async throws](./sleep%28until,tolerance%29.md)
  Suspend task execution until a given deadline within a tolerance. If no tolerance is specified then the system may adjust the deadline to coalesce CPU wake-ups to more efficiently process the wake-ups in a more power efficient manner.
### Type Aliases
- [ContinuousClock.Duration](./duration.md)
### Type Properties
- [static var continuous: ContinuousClock](./continuous.md)
  A clock that measures time that always increments but does not stop incrementing while the system is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/continuousclock/clock-implementations)*