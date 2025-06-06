# init(healthStore:workoutConfiguration:)

**Framework**: HealthKit  
**Kind**: init

Creates a new data source based on the provided workout configuration.

**Availability**:
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
init(healthStore: HKHealthStore, workoutConfiguration configuration: HKWorkoutConfiguration?)
```

## See Also

- [var typesToCollect: Set<HKQuantityType>](hkliveworkoutdatasource/typestocollect.md)
  The quantity type samples that the data source automatically sends to the workout builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/init(healthstore:workoutconfiguration:))*