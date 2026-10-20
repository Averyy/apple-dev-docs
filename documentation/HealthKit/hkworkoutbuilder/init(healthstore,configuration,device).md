# init(healthStore:configuration:device:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Returns a new workout builder object that is not connected to a workout session or other data source.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
init(healthStore: HKHealthStore, configuration: HKWorkoutConfiguration, device: HKDevice?)
```

```objc
- (instancetype) initWithHealthStore:(HKHealthStore *) healthStore configuration:(HKWorkoutConfiguration *) configuration device:(HKDevice *) device;
```

## See Also

### Creating the builder
- [var device: HKDevice?](./device.md)
  The device associated with the workout.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration information for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/init(healthstore:configuration:device:))*