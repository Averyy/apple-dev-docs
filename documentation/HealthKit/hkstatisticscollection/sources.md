# sources()

**Framework**: HealthKit  
**Kind**: method

Returns a set containing all the sources that had samples matched by the statistics collection query.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func sources() -> Set<HKSource>
```

#### Return Value

A set of sources if the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option was specified; otherwise, it returns `nil`.

#### Discussion

If the [`separateBySource`](hkstatisticsoptions/separatebysource.md) option was set, each of the statistics objects returned by the statistics collection also has a [`sources`](hkstatistics/sources.md) array. The statistic object’s array should contain a subset of the sources returned by this method. Specifically, it contains only those sources that contributed samples to that particular statistics object. You can use the source objects in these arrays to request source-specific statistical data.

## See Also

- [var sources: [HKSource]?](hkstatistics/sources.md)
  An array containing all the sources contributing to these statistics.
- [func averageQuantity(for: HKSource) -> HKQuantity?](hkstatistics/averagequantity(for:).md)
  Returns the average value from all the samples that match the query and that were created by the specified source.
- [func sumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/sumquantity(for:).md)
  Returns the sum of all the samples that match the query and that were created by the specified source.
- [func minimumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/minimumquantity(for:).md)
  Returns the minimum value from all the samples that match the query and that were created by the specified source.
- [func maximumQuantity(for: HKSource) -> HKQuantity?](hkstatistics/maximumquantity(for:).md)
  Returns the maximum value from all the samples that match the query and that were created by the specified source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstatisticscollection/sources())*