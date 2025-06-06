# init(predicate:options:)

**Framework**: HealthKit  
**Kind**: init

Creates a quantity series query descriptor.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
init(predicate: HKSamplePredicate<HKQuantitySample>, options: HKQuantitySeriesSampleQueryDescriptor.Options = [])
```

## Parameters

- `predicate`: A predicate that defines the set of series samples that the query returns. For a list of convenience methods for building predicates, see  .
- `options`: A set of options for the query. For a list of possible values, see  .

## See Also

- [HKQuantitySeriesSampleQueryDescriptor.Options](hkquantityseriessamplequerydescriptor/options-swift.struct.md)
  Options used when querying series data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/init(predicate:options:))*