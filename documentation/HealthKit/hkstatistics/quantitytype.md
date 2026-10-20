# quantityType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (strong, readonly) HKQuantityType * quantityType;
```

#### Discussion

The quantity type from the statistics query used to generate these statistics.

## See Also

### Getting Property Data
- [var startDate: Date](./startdate.md)
  The start of the time period included in these statistics.
- [var endDate: Date](./enddate.md)
  The end of the time period included in these statistics.
- [var sources: [HKSource]?](./sources.md)
  An array containing all the sources contributing to these statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/quantitytype)*