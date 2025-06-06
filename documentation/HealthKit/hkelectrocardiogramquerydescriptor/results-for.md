# results(for:)

**Framework**: HealthKit  
**Kind**: method

Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> HKElectrocardiogramQueryDescriptor.Results
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

- [HKElectrocardiogramQueryDescriptor.Results](hkelectrocardiogramquerydescriptor/results.md)
  An asynchronous sequence that emits data about individual voltage measurements from an electrocardiogram sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquerydescriptor/results(for:))*