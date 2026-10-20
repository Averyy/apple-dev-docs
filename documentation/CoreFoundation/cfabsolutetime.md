# CFAbsoluteTime

**Framework**: Core Foundation  
**Kind**: typealias  
**Role**: Type Alias

Type used to represent a specific point in time relative to the absolute reference date of 1 Jan 2001 00:00:00 GMT.

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
typealias CFAbsoluteTime = CFTimeInterval
```

```c
typedef CFTimeInterval CFAbsoluteTime;
```

#### Discussion

Absolute time is measured by the number of seconds between the reference date and the specified date. Negative values indicate dates/times before the reference date. Positive values indicate dates/times after the reference date.

## See Also

### Data Types
- [struct CFGregorianDate](./cfgregoriandate.md)
  Structure used to represent a point in time using the Gregorian calendar.
- [struct CFGregorianUnits](./cfgregorianunits.md)
  Structure used to represent a time interval in Gregorian units.
- [typealias CFTimeInterval](./cftimeinterval.md)
  Type used to represent elapsed time in seconds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfabsolutetime)*