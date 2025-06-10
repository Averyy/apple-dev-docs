# SuspendingClock

**Framework**: Swift  
**Kind**: struct

A clock that measures time that always increments but stops incrementing while the system is asleep.

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
struct SuspendingClock
```

#### Overview

`SuspendingClock` can be considered as a system awake time clock. The frame of reference of the `Instant` may be bound machine boot or some other locally defined reference point. This means that the instants are only comparable on the same machine in the same booted session.

This clock is suitable for high resolution measurements of execution.

## Topics

### Structures
- [SuspendingClock.Instant](suspendingclock/instant.md)
### Initializers
- [init()](suspendingclock/init.md)
### Type Properties
- [static var now: SuspendingClock.Instant](suspendingclock/now-swift.type.property.md)
  The current instant accounting for machine suspension.
### Default Implementations
- [Clock Implementations](suspendingclock/clock-implementations.md)

## Relationships

### Conforms To
- [Clock](clock.md)
- [Copyable](copyable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol Clock](clock.md)
  A mechanism in which to measure time, and delay work until a given point in time.
- [struct ClockTraits](clocktraits.md)
  Represents traits of a particular Clock implementation.
- [struct ContinuousClock](continuousclock.md)
  A clock that measures time that always increments and does not stop incrementing while the system is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/suspendingclock)*