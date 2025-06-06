# HKElectrocardiogramQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits data about individual voltage measurements from an electrocardiogram sample.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+
- watchOS 8.5+

## Declaration

```swift
struct Results
```

## Topics

### Creating an Iterator
- [HKElectrocardiogramQueryDescriptor.Results.Iterator](hkelectrocardiogramquerydescriptor/results/iterator.md)
  An iterator for accessing individual voltage measurements from the series.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func results(for: HKHealthStore) -> HKElectrocardiogramQueryDescriptor.Results](hkelectrocardiogramquerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual heartbeats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkelectrocardiogramquerydescriptor/results)*