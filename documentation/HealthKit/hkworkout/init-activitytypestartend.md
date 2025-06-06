# init(activityType:start:end:)

**Framework**: HealthKit  
**Kind**: init

Instantiates a new workout.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date)
```

#### Return Value

A workout activity.

#### Discussion

The workout’s duration is calculated from its start and end times. The workout’s total distance, total energy burned, workout events, device, and metadata are all set to `nil`.

## Parameters

- `workoutActivityType`: The type of activity being performed during the workout. For a list of possible activity types, see  .
- `startDate`: The date and time when the activity started.
- `endDate`: The date and time when the activity ended. This date must be equal to or later than the start date.

## See Also

- [var workoutActivityType: HKWorkoutActivityType](hkworkout/workoutactivitytype.md)
  The type of activity performed during the workout.
- [var totalDistance: HKQuantity?](hkworkout/totaldistance.md)
  The total distance traveled during the workout.
- [var duration: TimeInterval](hkworkout/duration.md)
  The workout’s duration.
- [var metadata: [String : Any]?](hkobject/metadata.md)
  The metadata for this HealthKit object.
- [var totalEnergyBurned: HKQuantity?](hkworkout/totalenergyburned.md)
  The total active energy burned during the workout.
- [var workoutEvents: [HKWorkoutEvent]?](hkworkout/workoutevents.md)
  An array of workout event objects.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:metadata:).md)
  Instantiates a new workout that includes the energy burned, distance, and metadata for the workout.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:metadata:).md)
  Instantiates a new workout whose duration is calculated based on the start and end dates and the provided workout events.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, duration: TimeInterval, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:duration:totalenergyburned:totaldistance:device:metadata:).md)
  Instantiates a new workout activity that includes the device that produced the sample data.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:device:metadata:).md)
  Instantiates a workout that includes both workout events and the device that produced the sample data.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalFlightsClimbed: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:totalflightsclimbed:device:metadata:).md)
  Instantiates a workout using a variety of data, including the number of flights of stairs climbed.
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalSwimmingStrokeCount: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)](hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:totalswimmingstrokecount:device:metadata:).md)
  Instantiates a workout using a variety of data, including the number of strokes while swimming.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/init(activitytype:start:end:))*