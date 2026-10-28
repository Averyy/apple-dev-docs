# startDate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The start of the time period included in these statistics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var startDate: Date { get }
```

```objc
@property (strong, readonly) NSDate * startDate;
```

## Discussion

This property contains the start date for the statistics. If you calculated these statistics using a statistics query, this is the earliest start date from all the samples that match the query. If you calculated these statistics using a statistics collection query, this is the start of the time interval for that particular collection of statistics.

## See Also

### Getting Property Data
- [var endDate: Date](./enddate.md)
  The end of the time period included in these statistics.
- [var quantityType: HKQuantityType](./quantitytype.md)
  The quantity type of the samples used to calculate these statistics.
- [var sources: [HKSource]?](./sources.md)
  An array containing all the sources contributing to these statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/startdate)*