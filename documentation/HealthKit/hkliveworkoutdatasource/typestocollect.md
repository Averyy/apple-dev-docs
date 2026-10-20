# typesToCollect

**Framework**: HealthKit  
**Kind**: property  
**Role**: Instance Property

The quantity type samples that the data source automatically sends to the workout builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS
- watchOS 5.0+

## Declaration

```swift
var typesToCollect: Set<HKQuantityType> { get }
```

```objc
@property (copy, readonly) NSSet<HKQuantityType *> * typesToCollect;
```

#### Discussion

The workout builder automatically collects the listed data types. The available data types vary depending on platform, the person’s settings and the workout configuration, and can include types like [`basalEnergyBurned`](../hkquantitytypeidentifier/basalenergyburned.md), [`activeEnergyBurned`](../hkquantitytypeidentifier/activeenergyburned.md), [`heartRate`](../hkquantitytypeidentifier/heartrate.md), [`distanceWalkingRunning`](../hkquantitytypeidentifier/distancewalkingrunning.md), [`distanceCycling`](../hkquantitytypeidentifier/distancecycling.md), [`distanceSwimming`](../hkquantitytypeidentifier/distanceswimming.md), or [`distanceWheelchair`](../hkquantitytypeidentifier/distancewheelchair.md).

Some datatypes require you to support an external sensor like [`heartRate`](../hkquantitytypeidentifier/heartrate.md) on iPhone and iPad and cycling power and cycling cadence on Apple Watch. Once a person pairs a device, HealthKit handles getting the data from the device and saving it as samples to the Health Store, making it available to your app.

To monitor this data, add a delegate to the session’s [`HKLiveWorkoutBuilder`](../hkliveworkoutbuilder.md) object, and implement its [`workoutBuilder(_:didCollectDataOf:)`](../hkliveworkoutbuilderdelegate/workoutbuilder%28_,didcollectdataof%29.md) method.

## See Also

### Creating a live data source
- [init(healthStore: HKHealthStore, workoutConfiguration: HKWorkoutConfiguration?)](./init%28healthstore,workoutconfiguration%29.md)
  Creates a new data source based on the provided workout configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/typestocollect)*