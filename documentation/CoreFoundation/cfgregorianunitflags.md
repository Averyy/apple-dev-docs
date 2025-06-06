# CFGregorianUnitFlags

**Framework**: Core Foundation  
**Kind**: struct

These option flags are used as a mask to indicate a specific set of fields in the CFGregorianDate or CFGregorianUnits structures.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CFGregorianUnitFlags
```

#### Overview

These flags are used with functions such as [`CFGregorianDateIsValid(_:_:)`](cfgregoriandateisvalid(_:_:).md) and [`CFAbsoluteTimeGetDifferenceAsGregorianUnits(_:_:_:_:)`](cfabsolutetimegetdifferenceasgregorianunits(_:_:_:_:).md) which operate on a CFGregorianDate or CFGregorianUnits structure. For more details, see the discussion of those functions.

## Topics

### Constants
- [static var unitsYears: CFGregorianUnitFlags](cfgregorianunitflags/unitsyears.md)
  Specifies the year field.
- [static var unitsMonths: CFGregorianUnitFlags](cfgregorianunitflags/unitsmonths.md)
  Specifies the month field.
- [static var unitsDays: CFGregorianUnitFlags](cfgregorianunitflags/unitsdays.md)
  Specifies the day field.
- [static var unitsHours: CFGregorianUnitFlags](cfgregorianunitflags/unitshours.md)
  Specifies the hours field.
- [static var unitsMinutes: CFGregorianUnitFlags](cfgregorianunitflags/unitsminutes.md)
  Specifies the minutes field.
- [static var unitsSeconds: CFGregorianUnitFlags](cfgregorianunitflags/unitsseconds.md)
  Specifies the seconds field.
- [static var allUnits: CFGregorianUnitFlags](cfgregorianunitflags/allunits.md)
  Specifies all fields.
### Initializers
- [init(rawValue: CFOptionFlags)](cfgregorianunitflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Predefined Time Interval Values](predefined-time-interval-values.md)
  Time intervals between the absolute reference date and certain other dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags)*