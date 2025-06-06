# HKQuantitySeriesSampleQueryDescriptor.Options

**Framework**: HealthKit  
**Kind**: struct

Options used when querying series data.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Options
```

## Topics

### Setting Options
- [static let includeSample: HKQuantitySeriesSampleQueryDescriptor.Options](hkquantityseriessamplequerydescriptor/options-swift.struct/includesample.md)
  An option indicating that the results should include a reference to the quantity sample that contains the series data.
- [static let orderByQuantitySampleStartDate: HKQuantitySeriesSampleQueryDescriptor.Options](hkquantityseriessamplequerydescriptor/options-swift.struct/orderbyquantitysamplestartdate.md)
  An option indicating that the results are grouped by the containing quantity sample’s start date.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKQuantitySeriesSampleQueryDescriptor.Options)](hkquantityseriessamplequerydescriptor/init(predicate:options:).md)
  Creates a quantity series query descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/options-swift.struct)*