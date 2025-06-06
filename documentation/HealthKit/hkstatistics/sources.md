# sources

**Framework**: HealthKit  
**Kind**: property

An array containing all the sources contributing to these statistics.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var sources: [HKSource]? { get }
```

#### Discussion

If the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option was specified, this property holds an array of all the sources included in the calculations. If the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option was not specified, the property contains `nil`.

## See Also

- [var startDate: Date](hkstatistics/startdate.md)
  The start of the time period included in these statistics.
- [var endDate: Date](hkstatistics/enddate.md)
  The end of the time period included in these statistics.
- [var quantityType: HKQuantityType](hkstatistics/quantitytype.md)
  The quantity type of the samples used to calculate these statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatistics/sources)*