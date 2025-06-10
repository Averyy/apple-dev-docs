# ClockTraits

**Framework**: Swift  
**Kind**: struct

Represents traits of a particular Clock implementation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct ClockTraits
```

#### Overview

Clocks may be of a number of different varieties; executors will likely have specific clocks that they can use to schedule jobs, and will therefore need to be able to convert timestamps to an appropriate clock when asked to enqueue a job with a delay or deadline.

Choosing a clock in general requires the ability to tell which of their clocks best matches the clock that the user is trying to specify a time or delay in.  Executors are expected to do this on a best effort basis.

## Topics

### Initializers
- [init(rawValue: UInt32)](clocktraits/init(rawvalue:).md)
  Creates a new option set from the given raw value.
### Instance Properties
- [let rawValue: UInt32](clocktraits/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Type Aliases
- [ClockTraits.ArrayLiteralElement](clocktraits/arrayliteralelement.md)
  The type of the elements of an array literal.
- [ClockTraits.Element](clocktraits/element.md)
  The element type of the option set.
- [ClockTraits.RawValue](clocktraits/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
### Type Properties
- [static let continuous: ClockTraits](clocktraits/continuous.md)
  Clocks with this trait continue running while the machine is asleep.
- [static let monotonic: ClockTraits](clocktraits/monotonic.md)
  Indicates that a clock’s time will only ever increase.
- [static let wallTime: ClockTraits](clocktraits/walltime.md)
  Clocks with this trait are tied to “wall time”.
### Default Implementations
- [Equatable Implementations](clocktraits/equatable-implementations.md)
- [OptionSet Implementations](clocktraits/optionset-implementations.md)
- [SetAlgebra Implementations](clocktraits/setalgebra-implementations.md)

## Relationships

### Conforms To
- [Equatable](equatable.md)
- [ExpressibleByArrayLiteral](expressiblebyarrayliteral.md)
- [OptionSet](optionset.md)
- [RawRepresentable](rawrepresentable.md)
- [SetAlgebra](setalgebra.md)

## See Also

- [protocol Clock](clock.md)
  A mechanism in which to measure time, and delay work until a given point in time.
- [struct ContinuousClock](continuousclock.md)
  A clock that measures time that always increments and does not stop incrementing while the system is asleep.
- [struct SuspendingClock](suspendingclock.md)
  A clock that measures time that always increments but stops incrementing while the system is asleep.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/clocktraits)*