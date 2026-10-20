# delegate

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The live builder’s delegate.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
weak var delegate: (any HKLiveWorkoutBuilderDelegate)? { get set }
```

```objc
@property (weak) id<HKLiveWorkoutBuilderDelegate> delegate;
```

## See Also

### Configuring a live workout builder
- [var dataSource: HKLiveWorkoutDataSource?](./datasource.md)
  A data source that provides live data from a workout session automatically.
- [var workoutSession: HKWorkoutSession?](./workoutsession.md)
  The workout session created by the data source and associated with this builder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutbuilder/delegate)*