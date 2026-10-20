# maximumQuantity

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The maximum quantity contained by the sample.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var maximumQuantity: HKQuantity { get }
```

```objc
@property (copy, readonly) HKQuantity * maximumQuantity;
```

## See Also

### Accessing Calculated Values
- [var averageQuantity: HKQuantity](./averagequantity.md)
  The average of all quantities contained by the sample.
- [var minimumQuantity: HKQuantity](./minimumquantity.md)
  The minimum value contained by the sample.
- [var mostRecentQuantity: HKQuantity](./mostrecentquantity.md)
  The most recent quantity contained by the sample.
- [var mostRecentQuantityDateInterval: DateInterval](./mostrecentquantitydateinterval.md)
  The date interval for the most recent quantity contained by the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdiscretequantitysample/maximumquantity)*