# typesToCollect

**Framework**: HealthKit  
**Kind**: property

The quantity type samples that the data source automatically sends to the workout builder.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
var typesToCollect: Set<HKQuantityType> { get }
```

#### Discussion

The workout builder automatically collects the listed data types. The available data types vary depending on platform, the person’s settings and the workout configuration, and can include types like [`basalEnergyBurned`](hkquantitytypeidentifier/basalenergyburned.md), [`activeEnergyBurned`](hkquantitytypeidentifier/activeenergyburned.md), [`heartRate`](hkquantitytypeidentifier/heartrate.md), [`distanceWalkingRunning`](hkquantitytypeidentifier/distancewalkingrunning.md), [`distanceCycling`](hkquantitytypeidentifier/distancecycling.md), [`distanceSwimming`](hkquantitytypeidentifier/distanceswimming.md), or [`distanceWheelchair`](hkquantitytypeidentifier/distancewheelchair.md).

Some datatypes require you to support an external sensor like [`heartRate`](hkquantitytypeidentifier/heartrate.md) on iPhone and iPad and cycling power and cycling cadence on Apple Watch. Once a person pairs a device, HealthKit handles getting the data from the device and saving it as samples to the Health Store, making it available to your app.

To monitor this data, add a delegate to the session’s [`HKLiveWorkoutBuilder`](hkliveworkoutbuilder.md) object, and implement its [`workoutBuilder(_:didCollectDataOf:)`](hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:).md) method.

## See Also

- [init(healthStore: HKHealthStore, workoutConfiguration: HKWorkoutConfiguration?)](hkliveworkoutdatasource/init(healthstore:workoutconfiguration:).md)
  Creates a new data source based on the provided workout configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/typestocollect)*