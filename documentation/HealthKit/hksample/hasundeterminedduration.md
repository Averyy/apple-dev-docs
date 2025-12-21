# hasUndeterminedDuration

**Framework**: HealthKit  
**Kind**: property

Indicates whether the sample has an unknown duration.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.2+

## Declaration

```swift
var hasUndeterminedDuration: Bool { get }
```

#### Discussion

This property is [`true`](https://developer.apple.com/documentation/Swift/true) if the sample’s [`endDate`](hksample/enddate.md) property is [`distantFuture`](https://developer.apple.com/documentation/Foundation/NSDate/distantFuture).

## See Also

- [var startDate: Date](hksample/startdate.md)
  The sample’s start date.
- [var endDate: Date](hksample/enddate.md)
  The sample’s end date.
- [var sampleType: HKSampleType](hksample/sampletype.md)
  The sample type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksample/hasundeterminedduration)*