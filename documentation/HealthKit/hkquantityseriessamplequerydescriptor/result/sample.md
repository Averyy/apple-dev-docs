# sample

**Framework**: HealthKit  
**Kind**: property

The quantity sample that owns the series of data entries.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
let sample: HKQuantitySample?
```

#### Discussion

HealthKit sets this value to `nil` unless you included the [`includeSample`](hkquantityseriessamplequerydescriptor/options-swift.struct/includesample.md) option when you created the series query descriptor.

## See Also

- [let quantity: HKQuantity](hkquantityseriessamplequerydescriptor/result/quantity.md)
  The quantity stored by the data entry.
- [let dateInterval: DateInterval](hkquantityseriessamplequerydescriptor/result/dateinterval.md)
  The date interval for the entry.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/result/sample)*