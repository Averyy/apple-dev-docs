# SRSensorReader

**Framework**: SensorKit  
**Kind**: class

An object that establishes user authorization and records data for a particular sensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class SRSensorReader
```

#### Overview

To acquire data from a particular sensor using a reader, an app creates an instance of this class using [`init(sensor:)`](srsensorreader/init(sensor:).md) and passes in one sensor from the available options in `Sensors`.

A reader is a data stream for a particular sensor that the user must authorize before use. When an app calls [`requestAuthorization(sensors:completion:)`](srsensorreader/requestauthorization(sensors:completion:).md), the OS prompts the user for approval to use the particular sensor and determines the app’s authorization according to the user’s answer. The framework notifies the delegate with the  [`sensorReader(_:didChange:)`](srsensorreaderdelegate/sensorreader(_:didchange:).md) callback if the authorization status changes as a result of the [`requestAuthorization(sensors:completion:)`](srsensorreader/requestauthorization(sensors:completion:).md) call. When a reader’s [`authorizationStatus`](srsensorreader/authorizationstatus.md) is [`SRAuthorizationStatus.authorized`](srauthorizationstatus/authorized.md), an app starts collecting sensor data by beginning recording.

When an app calls [`startRecording()`](srsensorreader/startrecording().md), the framework starts the reader’s sensor if it isn’t already running because of a request from another app or a system process. An app has access to 7 days of prior recorded data for an active sensor. When an app calls [`stopRecording()`](srsensorreader/stoprecording().md), the app relinquishes stakeholdership in the sensor. When a sensor has no app or system stakeholders, the framework deactivates the sensor and, thereby, stops recording data.

To fetch a sensor’s data, pass a request object to the [`fetch(_:)`](srsensorreader/fetch(_:).md) function. [`SRFetchRequest`](srfetchrequest.md) specifies a time range that defines the age of the data, and a device, such as a phone or a watch, from which to collect the data. Use [`fetchDevices()`](srsensorreader/fetchdevices().md) to list the available devices, and use the time convenience-functions in Defining the Time Range to specify the time range.

If the fetch query succeeds, the framework notifies the delegate with [`sensorReader(_:didCompleteFetch:)`](srsensorreaderdelegate/sensorreader(_:didcompletefetch:).md). The delegate receives sensor data in the form of  from [`sensorReader(_:fetching:didFetchResult:)`](srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:).md). A fetch result’s [`sample`](srfetchresult/sample.md) type is different depending on the particular sensor for the reader. For a mapping of sensors to their samples, see [`Sample types`](srfetchresult/sample#Sample-types.md).

## Topics

### Checking user authorization
- [var authorizationStatus: SRAuthorizationStatus](srsensorreader/authorizationstatus.md)
  The status of the user’s agreement to let the app access this reader’s sensor.
- [class func requestAuthorization(sensors: Set<SRSensor>, completion: ((any Error)?) -> Void)](srsensorreader/requestauthorization(sensors:completion:).md)
  Requests user permission to read one or more sensors.
- [enum SRAuthorizationStatus](srauthorizationstatus.md)
  The states that model whether the user approves the app to read a particular sensor.
### Creating a sensor reader
- [init(sensor: SRSensor)](srsensorreader/init(sensor:).md)
  Initializes a new sensor reader object.
- [struct SRSensor](srsensor.md)
  The sensors an app can read.
- [var sensor: SRSensor](srsensorreader/sensor.md)
  The particular sensor that this object reads.
### Recording sensor data
- [func startRecording()](srsensorreader/startrecording.md)
  Starts recording sensor data.
- [func stopRecording()](srsensorreader/stoprecording.md)
  Stops recording sensor data.
### Reading recorded data
- [func fetch(SRFetchRequest)](srsensorreader/fetch(_:).md)
  Fetches the samples that a fetch request specifies.
- [func fetchDevices()](srsensorreader/fetchdevices.md)
  Acquires device information for all devices that store data for this reader’s sensor.
- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.
### Responding to sensor events
- [var delegate: (any SRSensorReaderDelegate)?](srsensorreader/delegate.md)
  An object that responds to sensor-related events.
- [protocol SRSensorReaderDelegate](srsensorreaderdelegate.md)
  A set of callbacks the framework invokes to notify the app of sensor-related events.

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

- [Configuring your project for sensor reading](configuring-your-project-for-sensor-reading.md)
  Add metadata to your app to attain system and user permission to access sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader)*