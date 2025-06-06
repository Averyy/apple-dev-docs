# Duration

**Framework**: Swift  
**Kind**: struct

A representation of high precision time.

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
@frozen
struct Duration
```

#### Overview

`Duration` represents an elapsed time value with high precision in an integral form. It may be used for measurements of varying clock sources. In those cases it represents the elapsed time measured by that clock. Calculations using `Duration` may span from a negative value to a positive value and have a suitable range to at least cover attosecond scale for both small elapsed durations like sub-second precision to durations that span centuries.

Typical construction of `Duration` values should be created via the static methods for specific time values.

```swift
 var d: Duration = .seconds(3)
 d += .milliseconds(33)
 print(d) // 3.033 seconds
```

`Duration` itself does not ferry any additional information other than the temporal measurement component; specifically leap seconds should be represented as an additional accessor since that is specific only to certain clock implementations.

## Topics

### Creating a duration
- [init(secondsComponent: Int64, attosecondsComponent: Int64)](duration/init(secondscomponent:attosecondscomponent:).md)
  Construct a `Duration` by adding attoseconds to a seconds value.
- [static func seconds<T>(T) -> Duration](duration/seconds(_:)-311cx.md)
  Construct a `Duration` given a number of seconds represented as a `BinaryInteger`.
- [static func seconds(Double) -> Duration](duration/seconds(_:)-5ifzr.md)
  Construct a `Duration` given a number of seconds represented as a `Double` by converting the value into the closest attosecond scale value.
- [static func milliseconds<T>(T) -> Duration](duration/milliseconds(_:)-1w328.md)
  Construct a `Duration` given a number of milliseconds represented as a `BinaryInteger`.
- [static func milliseconds(Double) -> Duration](duration/milliseconds(_:)-7ledy.md)
  Construct a `Duration` given a number of seconds milliseconds as a `Double` by converting the value into the closest attosecond scale value.
- [static func microseconds(Double) -> Duration](duration/microseconds(_:)-1zzcc.md)
  Construct a `Duration` given a number of seconds microseconds as a `Double` by converting the value into the closest attosecond scale value.
- [static func microseconds<T>(T) -> Duration](duration/microseconds(_:)-2majo.md)
  Construct a `Duration` given a number of microseconds represented as a `BinaryInteger`.
- [static func nanoseconds<T>(T) -> Duration](duration/nanoseconds(_:).md)
  Construct a `Duration` given a number of nanoseconds represented as a `BinaryInteger`.
### Accessing a duration’s components
- [var components: (seconds: Int64, attoseconds: Int64)](duration/components.md)
  The composite components of the `Duration`.
### Performing calculations on durations
- [static func * (Duration, Double) -> Duration](duration/*(_:_:)-3d469.md)
- [static func *= <T>(inout Duration, T)](duration/*=(_:_:).md)
- [static func / (Duration, Double) -> Duration](duration/_(_:_:)-7fkmh.md)
- [static func /= (inout Duration, Double)](duration/_=(_:_:)-10rgx.md)
- [static func /= <T>(inout Duration, T)](duration/_=(_:_:)-1qfv3.md)
### Formatting a duration
- [func formatted() -> String](duration/formatted.md)
  Formats the string using a localized hour-minute-second time pattern.
- [func formatted<S>(S) -> S.FormatOutput](duration/formatted(_:).md)
  Formats the duration, using the provided format style.
- [Duration.TimeFormatStyle](duration/timeformatstyle.md)
  A format style that shows durations in a compact, localized format with separators.
- [Duration.UnitsFormatStyle](duration/unitsformatstyle.md)
  A format style that shows durations with localized labeled components
### Initializers
- [init(timeval)](duration/init(_:).md)
### Default Implementations
- [AdditiveArithmetic Implementations](duration/additivearithmetic-implementations.md)
- [AtomicRepresentable Implementations](duration/atomicrepresentable-implementations.md)
- [Comparable Implementations](duration/comparable-implementations.md)
- [CustomStringConvertible Implementations](duration/customstringconvertible-implementations.md)
- [Decodable Implementations](duration/decodable-implementations.md)
- [DurationProtocol Implementations](duration/durationprotocol-implementations.md)
- [Encodable Implementations](duration/encodable-implementations.md)
- [Equatable Implementations](duration/equatable-implementations.md)
- [Hashable Implementations](duration/hashable-implementations.md)

## Relationships

### Conforms To
- [AdditiveArithmetic](additivearithmetic.md)
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [DurationProtocol](durationprotocol.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)

## See Also

- [protocol DurationProtocol](durationprotocol.md)
  A type that defines a duration for a given `InstantProtocol` type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration)*