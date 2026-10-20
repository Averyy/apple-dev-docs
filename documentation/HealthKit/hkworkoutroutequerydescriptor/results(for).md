# results(for:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Runs a one-shot query that returns an asynchronous sequence of data representing individual locations.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS
- watchOS 8.5+

## Declaration

```swift
func results(for healthStore: HKHealthStore) -> HKWorkoutRouteQueryDescriptor.Results
```

## Parameters

- `healthStore`: The access point for HealthKit data.

## See Also

### Running queries
- [HKWorkoutRouteQueryDescriptor.Results](./results.md)
  An asynchronous sequence that emits data about individual locations from a workout route sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutroutequerydescriptor/results(for:))*