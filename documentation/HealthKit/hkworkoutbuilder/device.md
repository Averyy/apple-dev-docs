# device

**Framework**: HealthKit  
**Kind**: property

The device associated with the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS ?+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var device: HKDevice? { get }
```

## See Also

- [init(healthStore: HKHealthStore, configuration: HKWorkoutConfiguration, device: HKDevice?)](hkworkoutbuilder/init(healthstore:configuration:device:).md)
  Returns a new workout builder object that is not connected to a workout session or other data source.
- [var workoutConfiguration: HKWorkoutConfiguration](hkworkoutbuilder/workoutconfiguration.md)
  The configuration information for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/device)*