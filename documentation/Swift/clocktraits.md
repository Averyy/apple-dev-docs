# ClockTraits

**Framework**: Swift  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct ClockTraits
```

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
- [static let monotonic: ClockTraits](clocktraits/monotonic.md)
- [static let wallTime: ClockTraits](clocktraits/walltime.md)
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