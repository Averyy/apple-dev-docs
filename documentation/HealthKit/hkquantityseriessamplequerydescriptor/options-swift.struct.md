# HKQuantitySeriesSampleQueryDescriptor.Options

**Framework**: HealthKit  
**Kind**: struct  
**Role**: Structure

Options used when querying series data.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
struct Options
```

## Topics

### Setting Options
- [static let includeSample: HKQuantitySeriesSampleQueryDescriptor.Options](./options-swift.struct/includesample.md)
  An option indicating that the results should include a reference to the quantity sample that contains the series data.
- [static let orderByQuantitySampleStartDate: HKQuantitySeriesSampleQueryDescriptor.Options](./options-swift.struct/orderbyquantitysamplestartdate.md)
  An option indicating that the results are grouped by the containing quantity sample’s start date.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating Series Query Descriptors
- [init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKQuantitySeriesSampleQueryDescriptor.Options)](./init%28predicate,options%29.md)
  Creates a quantity series query descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/options-swift.struct)*