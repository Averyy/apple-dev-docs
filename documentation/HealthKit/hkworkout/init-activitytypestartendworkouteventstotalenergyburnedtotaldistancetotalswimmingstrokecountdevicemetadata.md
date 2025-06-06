# init(activityType:start:end:workoutEvents:totalEnergyBurned:totalDistance:totalSwimmingStrokeCount:device:metadata:)

**Framework**: HealthKit  
**Kind**: init

Instantiates a workout using a variety of data, including the number of strokes while swimming.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(activityType workoutActivityType: HKWorkoutActivityType, start startDate: Date, end endDate: Date, workoutEvents: [HKWorkoutEvent]?, totalEnergyBurned: HKQuantity?, totalDistance: HKQuantity?, totalSwimmingStrokeCount: HKQuantity?, device: HKDevice?, metadata: [String : Any]?)
```

#### Return Value

A workout object with the specified duration, total energy burned, total distance, total stroke count, device, metadata, and workout events.

#### Discussion

This method calculates the workout’s duration based on the amount of time it spends in an active state. A workout starts in an active state. A pause event switches it to an inactive state, and a resume event switches it back to an active state. For more information on workout events, see [`HKWorkoutEvent`](hkworkoutevent.md).

If the total energy burned or total distance are non-zero values, create a set of corresponding samples that add up to the calculated totals. Associate these samples with the workout by calling the health store’s [`add(_:to:completion:)`](hkhealthstore/add(_:to:completion:).md) method.

## Parameters

- `workoutActivityType`: The type of activity performed during the workout. For the complete list of activity types, see  .
- `startDate`: The date and time when the activity started.
- `endDate`: The date and time when the activity ended. This date must be equal to or later than the start date.
- `workoutEvents`: An array of workout event objects. This array specifies when the user has paused and resumed the workout activity. This method calculates the workout’s duration based on the total amount of active time between the provided start and end dates.
- `totalEnergyBurned`: A quantity using energy units, or  . This property sets the workout’s   property. It represents the total active energy burned during the workout.
- `totalDistance`: A quantity using length units, or  . This property sets the workout’s   property.
- `totalSwimmingStrokeCount`: A quantity unit using count units or  . This property sets the workout’s   property.
- `device`: The device that generated the data for this sample.
- `metadata`: Using predefined keys helps facilitate sharing data between apps; however, you are also encouraged to create your own, custom keys as needed to extend the HealthKit quantity sample’s capabilities.

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
- [convenience init(activityType: HKWorkoutActivityType, start: Date, end: Date)](hkworkout/init(activitytype:start:end:).md)
  Instantiates a new workout.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkout/init(activitytype:start:end:workoutevents:totalenergyburned:totaldistance:totalswimmingstrokecount:device:metadata:))*