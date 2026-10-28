# beginNewActivity(configuration:date:metadata:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

Begins a new workout activity in the workout session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func beginNewActivity(configuration workoutConfiguration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)
```

```objc
- (void) beginNewActivityWithConfiguration:(HKWorkoutConfiguration *) workoutConfiguration date:(NSDate *) date metadata:(NSDictionary<NSString *,id> *) metadata;
```

## Mentions

- [Dividing a HealthKit workout into activities](../dividing-a-healthkit-workout-into-activities.md)

## Discussion

This method asynchronously creates a new workout activity. HealthKit calls the session delegate’s [`workoutSession(_:didBeginActivityWith:date:)`](../hkworkoutsessiondelegate/workoutsession%28_,didbeginactivitywith,date%29.md) method after the activity begins. If the workout already has a current activity, HealthKit also ends that activity.

HealthKit may also set the data source’s [`typesToCollect`](../hkliveworkoutdatasource/typestocollect.md) value based on the new activity. If you’ve never modified the types that the data source collects (for example, by calling [`enableCollection(for:predicate:)`](../hkliveworkoutdatasource/enablecollection%28for,predicate%29.md) or [`disableCollection(for:)`](../hkliveworkoutdatasource/disablecollection%28for%29.md)), HealthKit automatically sets the [`typesToCollect`](../hkliveworkoutdatasource/typestocollect.md) property to a set of relevant data types based on the new actiity. However, if you’ve explicitly set the collected data types, HealthKit won’t modify them; therefore, you may need to update them for the new activity.

## Parameters

- `workoutConfiguration`: The configuration information for the activity. For [`HKWorkoutActivityType.swimBikeRun`](../hkworkoutactivitytype/swimbikerun.md) workouts, the activity’s configuration must use the [`HKWorkoutActivityType.swimming`](../hkworkoutactivitytype/swimming.md), [`HKWorkoutActivityType.cycling`](../hkworkoutactivitytype/cycling.md), or [`HKWorkoutActivityType.running`](../hkworkoutactivitytype/running.md) activity types. For interval training, the activity’s configuration must use the same activity type as the containing workout.
- `date`: The activity’s start date and time.
- `metadata`: Metadata that provides additional information about the activity.

## See Also

### Managing workout activities
- [var currentActivity: HKWorkoutActivity](./currentactivity.md)
  The current workout activity.
- [func endCurrentActivity(on: Date)](./endcurrentactivity%28on%29.md)
  Ends the current workout activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/beginnewactivity(configuration:date:metadata:))*