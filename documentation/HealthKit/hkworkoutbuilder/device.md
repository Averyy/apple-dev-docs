# device

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The device associated with the workout.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@NSCopying
var device: HKDevice? { get }
```

```objc
@property (copy, readonly, nullable) HKDevice * device;
```

## See Also

### Creating the builder
- [init(healthStore: HKHealthStore, configuration: HKWorkoutConfiguration, device: HKDevice?)](./init%28healthstore,configuration,device%29.md)
  Returns a new workout builder object that is not connected to a workout session or other data source.
- [var workoutConfiguration: HKWorkoutConfiguration](./workoutconfiguration.md)
  The configuration information for the workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutbuilder/device)*