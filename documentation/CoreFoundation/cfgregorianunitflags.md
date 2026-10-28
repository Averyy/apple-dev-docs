# CFGregorianUnitFlags

**Framework**: Core Foundation  
**Kind**: struct  
**Role**: Structure

These option flags are used as a mask to indicate a specific set of fields in the CFGregorianDate or CFGregorianUnits structures.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct CFGregorianUnitFlags
```

```c
enum CFGregorianUnitFlags : CFOptionFlags;
```

## Overview

These flags are used with functions such as [`CFGregorianDateIsValid(_:_:)`](./cfgregoriandateisvalid%28_,_%29.md) and [`CFAbsoluteTimeGetDifferenceAsGregorianUnits(_:_:_:_:)`](./cfabsolutetimegetdifferenceasgregorianunits%28_,_,_,_%29.md) which operate on a CFGregorianDate or CFGregorianUnits structure. For more details, see the discussion of those functions.

## Topics

### Constants
- [static var unitsYears: CFGregorianUnitFlags](./cfgregorianunitflags/unitsyears.md)
  Specifies the year field.
- [static var unitsMonths: CFGregorianUnitFlags](./cfgregorianunitflags/unitsmonths.md)
  Specifies the month field.
- [static var unitsDays: CFGregorianUnitFlags](./cfgregorianunitflags/unitsdays.md)
  Specifies the day field.
- [static var unitsHours: CFGregorianUnitFlags](./cfgregorianunitflags/unitshours.md)
  Specifies the hours field.
- [static var unitsMinutes: CFGregorianUnitFlags](./cfgregorianunitflags/unitsminutes.md)
  Specifies the minutes field.
- [static var unitsSeconds: CFGregorianUnitFlags](./cfgregorianunitflags/unitsseconds.md)
  Specifies the seconds field.
- [static var allUnits: CFGregorianUnitFlags](./cfgregorianunitflags/allunits.md)
  Specifies all fields.
### Initializers
- [init(rawValue: CFOptionFlags)](./cfgregorianunitflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [Predefined Time Interval Values](./predefined-time-interval-values.md)
  Time intervals between the absolute reference date and certain other dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgregorianunitflags)*