# strictEndDate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

The sample’s end time must fall within the target time period.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var strictEndDate: HKQueryOptions { get }
```

```c
HKQueryOptionStrictEndDate
```

#### Discussion

The sample’s end time must be equal to or later than the target’s start time, and the sample’s end time must also be earlier than the target’s end time.

## See Also

### Constants
- [static var strictStartDate: HKQueryOptions](./strictstartdate.md)
  The sample’s start time must fall within the target time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkqueryoptions/strictenddate)*