# mostRecentQuantity

**Framework**: HealthKit  
**Kind**: property

The most recent quantity contained by the sample.

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
var mostRecentQuantity: HKQuantity { get }
```

#### Discussion

The sample sorts its contained quantities based on the [`startDate`](https://developer.apple.com/documentation/foundation/nsdateinterval/1641656-startdate) property for the quantity’s date interval.

## See Also

- [var averageQuantity: HKQuantity](hkdiscretequantitysample/averagequantity.md)
  The average of all quantities contained by the sample.
- [var maximumQuantity: HKQuantity](hkdiscretequantitysample/maximumquantity.md)
  The maximum quantity contained by the sample.
- [var minimumQuantity: HKQuantity](hkdiscretequantitysample/minimumquantity.md)
  The minimum value contained by the sample.
- [var mostRecentQuantityDateInterval: DateInterval](hkdiscretequantitysample/mostrecentquantitydateinterval.md)
  The date interval for the most recent quantity contained by the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdiscretequantitysample/mostrecentquantity)*