# HKPredicateKeyPathMostRecentStartDate

**Framework**: HealthKit  
**Kind**: var

The key path for the start date of the sample’s most recent quantity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
let HKPredicateKeyPathMostRecentStartDate: String
```

#### Discussion

Use this constant whenever you want to include a sample’s quantity in a predicate format string. Add a `%K` placeholder to the format string, and then pass this constant as an argument.

## See Also

- [let HKPredicateKeyPathMin: String](hkpredicatekeypathmin.md)
  The key path for the sample’s minimum quantity.
- [let HKPredicateKeyPathAverage: String](hkpredicatekeypathaverage.md)
  The key path for the sample’s average quantity.
- [let HKPredicateKeyPathMax: String](hkpredicatekeypathmax.md)
  The key path for the sample’s maximum quantity.
- [let HKPredicateKeyPathMostRecent: String](hkpredicatekeypathmostrecent.md)
  The key path for the sample’s most recent quantity.
- [let HKPredicateKeyPathMostRecentEndDate: String](hkpredicatekeypathmostrecentenddate.md)
  The key path for the end date of the sample’s most recent quantity.
- [let HKPredicateKeyPathMostRecentDuration: String](hkpredicatekeypathmostrecentduration.md)
  A key path for the duration of the sample’s most recent quantity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkpredicatekeypathmostrecentstartdate)*