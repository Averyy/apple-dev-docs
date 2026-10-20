# workoutSession

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The workout session created by the data source and associated with this builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
weak var workoutSession: HKWorkoutSession? { get }
```

```objc
@property (weak, readonly) HKWorkoutSession * workoutSession;
```

## See Also

### Configuring a live workout builder
- [var dataSource: HKLiveWorkoutDataSource?](./datasource.md)
  A data source that provides live data from a workout session automatically.
- [var delegate: (any HKLiveWorkoutBuilderDelegate)?](./delegate.md)
  The live builder’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilder/workoutsession)*