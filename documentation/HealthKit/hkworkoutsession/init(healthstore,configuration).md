# init(healthStore:configuration:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Returns a newly instantiated workout session with an associated workout builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- watchOS 5.0+

## Declaration

```swift
init(healthStore: HKHealthStore, configuration workoutConfiguration: HKWorkoutConfiguration) throws
```

```objc
- (instancetype) initWithHealthStore:(HKHealthStore *) healthStore configuration:(HKWorkoutConfiguration *) workoutConfiguration error:(NSError **) error;
```

## See Also

### Related Documentation
- [func associatedWorkoutBuilder() -> HKLiveWorkoutBuilder](./associatedworkoutbuilder%28%29.md)
  Returns the live workout builder associated with the workout session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/init(healthstore:configuration:))*