# hasUndeterminedDuration

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) BOOL hasUndeterminedDuration;
```

#### Discussion

This property is [`true`](../../Swift/true.md) if the sample’s [`endDate`](./enddate.md) property is [`distantFuture`](../../Foundation/nsdate/distantfuture.md).

## See Also

### Accessing the Sample’s Data
- [var startDate: Date](./startdate.md)
  The sample’s start date.
- [var endDate: Date](./enddate.md)
  The sample’s end date.
- [var sampleType: HKSampleType](./sampletype.md)
  The sample type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hksample/hasundeterminedduration)*