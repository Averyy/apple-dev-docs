# Accessing condensed workout samples

**Framework**: HealthKit

Read series data from condensed workouts.

#### Overview

To reduce the size of workout data, HealthKit can condense samples associated with workouts created on Apple Watch. HealthKit enumerates the data associated with a workout and adds that data to one or more quantity series samples. After saving all the data to series objects, HealthKit deletes the originals. In addition, it converts older [`HKQuantitySample`](hkquantitysample.md) objects to [`HKCumulativeQuantitySample`](hkcumulativequantitysample.md) or [`HKDiscreteQuantitySample`](hkdiscretequantitysample.md) objects.

HealthKit only condenses high-frequency data recorded by the Workout app on Apple Watch. This includes the following data types:

- [`distanceWalkingRunning`](hkquantitytypeidentifier/distancewalkingrunning.md)
- [`distanceCycling`](hkquantitytypeidentifier/distancecycling.md)
- [`basalEnergyBurned`](hkquantitytypeidentifier/basalenergyburned.md)
- [`activeEnergyBurned`](hkquantitytypeidentifier/activeenergyburned.md)
- [`heartRate`](hkquantitytypeidentifier/heartrate.md)

For these data types, HealthKit condenses samples that are more than 90 days old and associated with a workout that’s at least 5 minutes long.

HealthKit may condense samples for a given workout more than once. For example, if the system syncs new samples associated with the workout to the device, or if the condenser algorithm changes, HealthKit may condense the workout again.

HealthKit also batches the data into multiple quantity series to optimize how the system lays out the data in memory. For many data types, HealthKit creates a separate quantity series for each 5-minute interval in the workout. The condensation process preserves all the data from the original workout — but it greatly reduces the overhead needed to save that data to disk. However, your app may need to perform additional steps to read the condensed data.

##### Query High Frequency Data From a Condensed Workout

Because HealthKit condenses older workout data, any samples associated with a workout may actually represent a series of higher-frequency data. In many cases, you can just use these samples, without having to access the underlying data. For example, [`HKStatisticsQuery`](hkstatisticsquery.md) and [`HKStatisticsCollectionQuery`](hkstatisticscollectionquery.md) transparently operate on the underlying data.

However, if your app needs to access the underlying data directly, start by querying for all the samples associated with a workout:

```swift
// Create the workout predicate.
let forWorkout = HKQuery.predicateForObjects(from: workout)

// Create the heart-rate descriptor.
let heartRateDescriptor = HKQueryDescriptor(sampleType: myHeartRateType,
                                            predicate: forWorkout)

// Create the query.
let heartRateQuery = HKSampleQuery(queryDescriptors: [heartRateDescriptor],
                                   limit: HKObjectQueryNoLimit)
{ query, samples, error in
    // Process the samples.
}

// Run  the query.
myStore.execute(heartRateQuery)
```

Then, in the query’s results handler, if a sample has a [`count`](hkquantitysample/count.md) greater than 1, it contains series data.

```swift
// Create the query.
let heartRateQuery = HKSampleQuery(queryDescriptors: [heartRateDescriptor],
                                   limit: HKObjectQueryNoLimit)
{ query, samples, error in

    // Start by checking for errors.
    guard let samples = samples else {
        // Handle the error.
        fatalError("*** An error occurred: \(error!.localizedDescription) ***")
    }
    
    // Iterate over all the samples.
    for sample in samples {
        
        guard let sample = sample as? HKDiscreteQuantitySample else {
            fatalError("*** Unexpected Sample Type ***")
        }
        
        // Check to see if the sample is a series.
        if sample.count == 1 {
            // This is a single sample.
            // Use the sample.
            myOutput.append("\(sample)\n")
        }
        else {
            // This is a series.
            // Get the detailed items for the series.
            myGetDetailedItems(for: sample)
        }
    }
}

```

Use an [`HKQuantitySeriesSampleQuery`](hkquantityseriessamplequery.md) to access the detailed data from the series.

```swift
// Create the predicate.
let inSeriesSample = HKQuery.predicateForObject(with: series.uuid)

// Create the query.
let detailQuery = HKQuantitySeriesSampleQuery(quantityType: myHeartRateType,
                                              predicate: inSeriesSample)
{ query, quantity, dateInterval, HKSample, done, error in
    
    guard let quantity = quantity, let dateInterval = dateInterval else {
        fatalError("*** An error occurred: \(error!.localizedDescription) ***")
    }
    
    // Use the data.
    myOutput.append("\(quantity.doubleValue(for: HKUnit(from: "count/min"))): \(dateInterval)")
}

// Run the query.
myStore.execute(detailQuery)
```

## See Also

- [Adding samples to a workout](adding-samples-to-a-workout.md)
  Create associated samples that add details to a workout.
- [Dividing a HealthKit workout into activities](dividing-a-healthkit-workout-into-activities.md)
  Partition multisport and interval workouts into activities that represent the different parts of the workout.
- [class HKWorkout](hkworkout.md)
  A workout sample that stores information about a single physical activity.
- [class HKWorkoutActivity](hkworkoutactivity.md)
  An object that describes an activity within a longer workout.
- [class HKWorkoutBuilder](hkworkoutbuilder.md)
  A builder object that incrementally constructs a workout.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [let HKWorkoutTypeIdentifier: String](hkworkouttypeidentifier.md)
  The workout type identifier.
- [enum HKWorkoutActivityType](hkworkoutactivitytype.md)
  The type of activity performed during a workout.
- [enum HKWorkoutSessionType](hkworkoutsessiontype.md)
  The type of session.
- [class HKWorkoutEvent](hkworkoutevent.md)
  An object representing an important event during a workout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/accessing-condensed-workout-samples)*