# Time

**Framework**: Swift

Measure how long an operation takes and determine schedules in the future.

## Topics

### Clocks
- [protocol Clock](clock.md)
  A mechanism in which to measure time, and delay work until a given point in time.
- [struct ContinuousClock](continuousclock.md)
  A clock that measures time that always increments and does not stop incrementing while the system is asleep.
- [struct SuspendingClock](suspendingclock.md)
  A clock that measures time that always increments but stops incrementing while the system is asleep.
### Durations
- [struct Duration](duration.md)
  A representation of high precision time.
- [protocol DurationProtocol](durationprotocol.md)
  A type that defines a duration for a given `InstantProtocol` type.
### Supporting Types
- [protocol InstantProtocol](instantprotocol.md)

## See Also

- [Numbers and Basic Values](numbers-and-basic-values.md)
  Model data with numbers, Boolean values, and other fundamental types.
- [Strings and Text](strings-and-text.md)
  Work with text using Unicode-safe strings.
- [Collections](collections.md)
  Store and organize data using arrays, dictionaries, sets, and other data structures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/time-and-duration)*