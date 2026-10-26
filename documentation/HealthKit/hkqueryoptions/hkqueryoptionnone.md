# HKQueryOptionNone

**Framework**: HealthKit  
**Kind**: case  
**Role**: Enumeration Case

The sample’s time period must overlap part of the target time period.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
HKQueryOptionNone
```

#### Discussion

The sample’s end time must be equal to or later than the target’s start time, and the sample’s start time must be earlier than the target’s end time.

## See Also

### Constants
- [static var strictStartDate: HKQueryOptions](./strictstartdate.md)
  The sample’s start time must fall within the target time period.
- [static var strictEndDate: HKQueryOptions](./strictenddate.md)
  The sample’s end time must fall within the target time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryoptions/hkqueryoptionnone)*