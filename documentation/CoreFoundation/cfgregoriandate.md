# CFGregorianDate

**Framework**: Core Foundation  
**Kind**: struct

Structure used to represent a point in time using the Gregorian calendar.

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
struct CFGregorianDate
```

#### Overview

[`CFGregorianDate`](cfgregoriandate.md) is implemented using the smallest data type appropriate for the range of possible values. For example, there are only 12 months in the Gregorian year, so there is no need to use an integer type larger than 8 bits. To represent a time interval in Gregorian units, use a [`CFGregorianUnits`](cfgregorianunits.md).

The month and day units are 1-based: the index for January is 1, and the index for the first day of the month is 1.

## Topics

### Initializers
- [init()](cfgregoriandate/init.md)
- [init(year: Int32, month: Int8, day: Int8, hour: Int8, minute: Int8, second: Double)](cfgregoriandate/init(year:month:day:hour:minute:second:).md)
### Instance Properties
- [var day: Int8](cfgregoriandate/day.md)
- [var hour: Int8](cfgregoriandate/hour.md)
- [var minute: Int8](cfgregoriandate/minute.md)
- [var month: Int8](cfgregoriandate/month.md)
- [var second: Double](cfgregoriandate/second.md)
- [var year: Int32](cfgregoriandate/year.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias CFAbsoluteTime](cfabsolutetime.md)
  Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.
- [struct CFGregorianUnits](cfgregorianunits.md)
  Structure used to represent a time interval in Gregorian units.
- [typealias CFTimeInterval](cftimeinterval.md)
  Type used to represent elapsed time in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfgregoriandate)*