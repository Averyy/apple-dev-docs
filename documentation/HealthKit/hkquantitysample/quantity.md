# quantity

**Framework**: HealthKit  
**Kind**: property

The quantity for this sample.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var quantity: HKQuantity { get }
```

#### Discussion

If the sample contains more than one quantity, this property returns the sum or average, depending on the sample’s aggregation style (sum for cumulative, average for discrete). To access the individual quantities, use an [`HKQuantitySeriesSampleQuery`](hkquantityseriessamplequery.md).

To see the type of units compatible with this quantity, look up the sample’s quantity type identifier in [`HKQuantityTypeIdentifier`](hkquantitytypeidentifier.md).

## See Also

- [var count: Int](hkquantitysample/count.md)
  The number of quantities contained in this sample.
- [var quantityType: HKQuantityType](hkquantitysample/quantitytype.md)
  The quantity type for this sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitysample/quantity)*