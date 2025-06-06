# typesToCollect

**Framework**: HealthKit  
**Kind**: property

The quantity type samples that the data source automatically sends to the workout builder.

**Availability**:
- macOS ?+
- watchOS 5.0+

## Declaration

```swift
var typesToCollect: Set<HKQuantityType> { get }
```

#### Discussion

Apple Watch automatically collects the listed data types and sends the data to the workout builder. The available data types vary depending on the user’s settings and the workout configuration, and can include types like [`basalEnergyBurned`](hkquantitytypeidentifier/basalenergyburned.md), [`activeEnergyBurned`](hkquantitytypeidentifier/activeenergyburned.md), [`heartRate`](hkquantitytypeidentifier/heartrate.md), [`distanceWalkingRunning`](hkquantitytypeidentifier/distancewalkingrunning.md), [`distanceCycling`](hkquantitytypeidentifier/distancecycling.md), [`distanceSwimming`](hkquantitytypeidentifier/distanceswimming.md), or [`distanceWheelchair`](hkquantitytypeidentifier/distancewheelchair.md).

To monitor this data, add a delegate to the session’s [`HKLiveWorkoutBuilder`](hkliveworkoutbuilder.md) object, and implement its [`workoutBuilder(_:didCollectDataOf:)`](hkliveworkoutbuilderdelegate/workoutbuilder(_:didcollectdataof:).md) method.

## See Also

- [init(healthStore: HKHealthStore, workoutConfiguration: HKWorkoutConfiguration?)](hkliveworkoutdatasource/init(healthstore:workoutconfiguration:).md)
  Creates a new data source based on the provided workout configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkliveworkoutdatasource/typestocollect)*