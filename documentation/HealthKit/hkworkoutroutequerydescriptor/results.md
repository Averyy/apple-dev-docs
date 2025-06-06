# HKWorkoutRouteQueryDescriptor.Results

**Framework**: HealthKit  
**Kind**: struct

An asynchronous sequence that emits data about individual locations from a workout route sample.

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
- [HKWorkoutRouteQueryDescriptor.Results.Iterator](hkworkoutroutequerydescriptor/results/iterator.md)
  An iterator for accessing individual locations from the workout route.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/AsyncSequence.md)

## See Also

- [func results(for: HKHealthStore) -> HKWorkoutRouteQueryDescriptor.Results](hkworkoutroutequerydescriptor/results(for:).md)
  Runs a one-shot query that returns an asynchronous sequence of data representing individual locations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequerydescriptor/results)*