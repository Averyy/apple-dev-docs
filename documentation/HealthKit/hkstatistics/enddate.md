# endDate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The end of the time period included in these statistics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var endDate: Date { get }
```

```objc
@property (strong, readonly) NSDate * endDate;
```

## Discussion

This property contains the end date for the statistics. If you calculated these statistics using a statistics query, this is the latest end date from all the samples that match the query. If you calculated these statistics using a statistics collection query, this is the end of the time interval for that particular collection of statistics.

## See Also

### Getting Property Data
- [var startDate: Date](./startdate.md)
  The start of the time period included in these statistics.
- [var quantityType: HKQuantityType](./quantitytype.md)
  The quantity type of the samples used to calculate these statistics.
- [var sources: [HKSource]?](./sources.md)
  An array containing all the sources contributing to these statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/enddate)*