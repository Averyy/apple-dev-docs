# results(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query that returns an asynchronous sequence of matching series samples.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> HKQuantitySeriesSampleQueryDescriptor.Results
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [HKQuantitySeriesSampleQueryDescriptor.Results](hkquantityseriessamplequerydescriptor/results.md)
  An asynchronous sequence that emits data from the quantity series query.
- [HKQuantitySeriesSampleQueryDescriptor.Result](hkquantityseriessamplequerydescriptor/result.md)
  A set of results from a quantity series sample descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityseriessamplequerydescriptor/results(for:))*