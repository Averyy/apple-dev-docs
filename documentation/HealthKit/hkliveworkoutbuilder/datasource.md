# dataSource

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

A data source that provides live data from a workout session automatically.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
var dataSource: HKLiveWorkoutDataSource? { get set }
```

```objc
@property (strong, nullable) HKLiveWorkoutDataSource * dataSource;
```

## See Also

### Configuring a live workout builder
- [var workoutSession: HKWorkoutSession?](./workoutsession.md)
  The workout session created by the data source and associated with this builder.
- [var delegate: (any HKLiveWorkoutBuilderDelegate)?](./delegate.md)
  The live builder’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilder/datasource)*