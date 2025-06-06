# beginNewActivity(configuration:date:metadata:)

**Framework**: HealthKit  
**Kind**: method

Begins a new workout activity in the workout session.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS ?+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func beginNewActivity(configuration workoutConfiguration: HKWorkoutConfiguration, date: Date, metadata: [String : Any]?)
```

## Mentions

- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)

#### Discussion

This method asynchronously creates a new workout activity. HealthKit calls the session delegate’s [`workoutSession(_:didBeginActivityWith:date:)`](hkworkoutsessiondelegate/workoutsession(_:didbeginactivitywith:date:).md) method after the activity begins. If the workout already has a current activity, HealthKit also ends that activity.

HealthKit may also set the data source’s [`typesToCollect`](hkliveworkoutdatasource/typestocollect.md) value based on the new activity. If you’ve never modified the types that the data source collects (for example, by calling [`enableCollection(for:predicate:)`](hkliveworkoutdatasource/enablecollection(for:predicate:).md) or [`disableCollection(for:)`](hkliveworkoutdatasource/disablecollection(for:).md)), HealthKit automatically sets the [`typesToCollect`](hkliveworkoutdatasource/typestocollect.md) property to a set of relevant data types based on the new actiity. However, if you’ve explicitly set the collected data types, HealthKit won’t modify them; therefore, you may need to update them for the new activity.

## Parameters

- `workoutConfiguration`: The configuration information for the activity. For   workouts, the activity’s configuration must use the  ,  , or   activity types. For interval training, the activity’s configuration must use the same activity type as the containing workout.
- `date`: The activity’s start date and time.
- `metadata`: Metadata that provides additional information about the activity.

## See Also

- [var currentActivity: HKWorkoutActivity](hkworkoutsession/currentactivity.md)
  The current workout activity.
- [func endCurrentActivity(on: Date)](hkworkoutsession/endcurrentactivity(on:).md)
  Ends the current workout activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutsession/beginnewactivity(configuration:date:metadata:))*