# Clock

**Framework**: Swift  
**Kind**: protocol

A mechanism in which to measure time, and delay work until a given point in time.

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
protocol Clock<Duration> : Sendable
```

#### Overview

Types that conform to the `Clock` protocol define a concept of “now” which is the specific instant in time that property is accessed. Any pair of calls to the `now` property may have a minimum duration between them - this minimum resolution is exposed by the `minimumResolution` property to inform any user of the type the expected granularity of accuracy.

One of the primary uses for clocks is to schedule task sleeping. This method resumes the calling task after a given deadline has been met or passed with a given tolerance value. The tolerance is expected as a leeway around the deadline. The clock may reschedule tasks within the tolerance to ensure efficient execution of resumptions by reducing potential operating system wake-ups. If no tolerance is specified (i.e. nil is passed in) the sleep function is expected to schedule with a default tolerance strategy.

For more information about specific clocks see `ContinuousClock` and `SuspendingClock`.

## Topics

### Associated Types
- [associatedtype Duration](clock/duration.md)
- [associatedtype Instant : InstantProtocol](clock/instant.md)
### Instance Properties
- [var minimumResolution: Self.Duration](clock/minimumresolution.md)
- [var now: Self.Instant](clock/now.md)
- [var traits: ClockTraits](clock/traits.md)
  The traits associated with this clock instance.
### Instance Methods
- [func convert(from: Duration) -> Self.Duration?](clock/convert(from:)-37htx.md)
  Convert a Swift Duration to a Clock-specific Duration
- [func convert(from: Self.Duration) -> Duration?](clock/convert(from:)-8sz7z.md)
  Convert a Clock-specific Duration to a Swift Duration
- [func convert<OtherClock>(instant: OtherClock.Instant, from: OtherClock) -> Self.Instant?](clock/convert(instant:from:).md)
  Convert an `Instant` from some other clock’s `Instant`
- [func measure(() throws -> Void) rethrows -> Self.Instant.Duration](clock/measure(_:).md)
  Measure the elapsed time to execute a closure.
- [func measure(isolation: isolated (any Actor)?, () async throws -> Void) async rethrows -> Self.Instant.Duration](clock/measure(isolation:_:).md)
  Measure the elapsed time to execute an asynchronous closure.
- [func sleep(for: Self.Instant.Duration, tolerance: Self.Instant.Duration?) async throws](clock/sleep(for:tolerance:).md)
  Suspends for the given duration.
- [func sleep(until: Self.Instant, tolerance: Self.Instant.Duration?) async throws](clock/sleep(until:tolerance:).md)
### Type Properties
- [static var continuous: ContinuousClock](clock/continuous.md)
  A clock that measures time that always increments but does not stop incrementing while the system is asleep.
- [static var suspending: SuspendingClock](clock/suspending.md)
  A clock that measures time that always increments but stops incrementing while the system is asleep.

## Relationships

### Inherits From
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
### Conforming Types
- [ContinuousClock](continuousclock.md)
- [SuspendingClock](suspendingclock.md)

## See Also

- [struct ClockTraits](clocktraits.md)
  Represents traits of a particular Clock implementation.
- [struct ContinuousClock](continuousclock.md)
  A clock that measures time that always increments and does not stop incrementing while the system is asleep.
- [struct SuspendingClock](suspendingclock.md)
  A clock that measures time that always increments but stops incrementing while the system is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clock)*