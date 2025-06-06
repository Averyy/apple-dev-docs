# CFGregorianUnits

**Framework**: Core Foundation  
**Kind**: struct

Structure used to represent a time interval in Gregorian units.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
struct CFGregorianUnits
```

#### Overview

A CFGregorianUnits is used to represent arbitrary time  (to represent a point in time using Gregorian units, use a [`CFGregorianDate`](cfgregoriandate.md)). Each field can take values up to the maximum possible for its data type. Negative values are also valid.

## Topics

### Initializers
- [init()](cfgregorianunits/init.md)
- [init(years: Int32, months: Int32, days: Int32, hours: Int32, minutes: Int32, seconds: Double)](cfgregorianunits/init(years:months:days:hours:minutes:seconds:).md)
### Instance Properties
- [var days: Int32](cfgregorianunits/days.md)
- [var hours: Int32](cfgregorianunits/hours.md)
- [var minutes: Int32](cfgregorianunits/minutes.md)
- [var months: Int32](cfgregorianunits/months.md)
- [var seconds: Double](cfgregorianunits/seconds.md)
- [var years: Int32](cfgregorianunits/years.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CFAbsoluteTime](cfabsolutetime.md)
  Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.
- [struct CFGregorianDate](cfgregoriandate.md)
  Structure used to represent a point in time using the Gregorian calendar.
- [typealias CFTimeInterval](cftimeinterval.md)
  Type used to represent elapsed time in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgregorianunits)*