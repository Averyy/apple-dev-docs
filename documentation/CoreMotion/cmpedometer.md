# CMPedometer

**Framework**: Core Motion  
**Kind**: class

An object for fetching the system-generated live walking data.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
class CMPedometer
```

#### Overview

You use a pedometer object to retrieve step counts and other information about the distance traveled and the number of floors ascended or descended. The pedometer object manages a cache of historic data that you can query or you can ask for live updates as the data is processed.

To use a pedometer object, create an instance of this class and call the appropriate methods. Use the [`queryPedometerData(from:to:withHandler:)`](cmpedometer/querypedometerdata(from:to:withhandler:).md) method to retrieve data that has already been gathered. To get live updates, use the [`startUpdates(from:withHandler:)`](cmpedometer/startupdates(from:withhandler:).md) method to start the delivery of events to the handler you provide.

> ❗ **Important**:  To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

 To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

## Topics

### Determining Pedometer Availability
- [class func isStepCountingAvailable() -> Bool](cmpedometer/isstepcountingavailable.md)
  Returns a Boolean value indicating whether step counting is available on the current device.
- [class func isDistanceAvailable() -> Bool](cmpedometer/isdistanceavailable.md)
  Returns a Boolean value indicating whether distance estimation is available on the current device.
- [class func isFloorCountingAvailable() -> Bool](cmpedometer/isfloorcountingavailable.md)
  Returns a Boolean value indicating whether floor counting is available on the current device.
- [class func isPaceAvailable() -> Bool](cmpedometer/ispaceavailable.md)
  Returns a Boolean value indicating whether pace information is available on the current device.
- [class func isCadenceAvailable() -> Bool](cmpedometer/iscadenceavailable.md)
  Returns a Boolean value indicating whether cadence information is available on the current device.
- [class func isPedometerEventTrackingAvailable() -> Bool](cmpedometer/ispedometereventtrackingavailable.md)
  Returns a Boolean value indicating whether pedometer events are available on the current device.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmpedometer/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to gather pedometer data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
### Gathering Live Pedometer Data
- [func startUpdates(from: Date, withHandler: CMPedometerHandler)](cmpedometer/startupdates(from:withhandler:).md)
  Starts the delivery of recent pedestrian-related data to your app.
- [func stopUpdates()](cmpedometer/stopupdates.md)
  Stops the delivery of recent pedestrian data updates to your app.
- [func startEventUpdates(handler: CMPedometerEventHandler)](cmpedometer/starteventupdates(handler:).md)
  Starts the delivery of pedometer events to your app.
- [func stopEventUpdates()](cmpedometer/stopeventupdates.md)
  Stops the delivery of pedometer events to your app.
- [typealias CMPedometerHandler](cmpedometerhandler.md)
  A block for processing pedometer-related data.
- [typealias CMPedometerEventHandler](cmpedometereventhandler.md)
  A block for processing pedometer events.
### Fetching Historical Pedometer Data
- [func queryPedometerData(from: Date, to: Date, withHandler: CMPedometerHandler)](cmpedometer/querypedometerdata(from:to:withhandler:).md)
  Retrieves the data between the specified start and end dates.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CMPedometerData](cmpedometerdata.md)
  Information about the distance traveled by a user on foot.
- [class CMPedometerEvent](cmpedometerevent.md)
  A change in the user’s pedestrian activity.
- [class CMStepCounter](cmstepcounter.md)
  The number of steps the user has taken with the device.
- [class CMOdometerData](cmodometerdata.md)
  A class that represents odometer data for workouts.
- [class CMHighFrequencyHeartRateData](cmhighfrequencyheartratedata.md)
  A class that represents heart rate data collected at 1 Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometer)*