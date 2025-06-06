# quantityType

**Framework**: HealthKit  
**Kind**: property

The quantity type of the samples used to calculate these statistics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var quantityType: HKQuantityType { get }
```

#### Discussion

The quantity type from the statistics query used to generate these statistics.

## See Also

- [var startDate: Date](hkstatistics/startdate.md)
  The start of the time period included in these statistics.
- [var endDate: Date](hkstatistics/enddate.md)
  The end of the time period included in these statistics.
- [var sources: [HKSource]?](hkstatistics/sources.md)
  An array containing all the sources contributing to these statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/quantitytype)*