# CMSensorRecorder

**Framework**: Core Motion  
**Kind**: class

An object that gathers and retrieves accelerometer data from a device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
class CMSensorRecorder
```

## Mentions

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)

#### Overview

Use a sensor recorder to initiate the gathering of accelerometer data. Later, use the sensor recorder to fetch the recorded data so you can analyze it. You might use the recorded data to assess specific types of motion and incorporate the results into your app.

To use a sensor recorder, create an instance of this class and call the [`recordAccelerometer(forDuration:)`](cmsensorrecorder/recordaccelerometer(forduration:).md) method to begin recording data. You do not need to stop the recording process explicitly. The system stops recording automatically when the specified time expires and no other apps extend the recording time. The following example shows how to record 20 minutes worth of accelerometer data:

> ❗ **Important**:  To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

 To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

## Topics

### Checking the Availability of Sensor Recording
- [class func isAccelerometerRecordingAvailable() -> Bool](cmsensorrecorder/isaccelerometerrecordingavailable.md)
  Returns a Boolean value indicating whether accelerometer recording is supported on the current device.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmsensorrecorder/authorizationstatus.md)
  Returns a value indicating whether the app is authorized to record sensor data.
- [enum CMAuthorizationStatus](cmauthorizationstatus.md)
  The authorization status for motion-related features.
- [class func isAuthorizedForRecording() -> Bool](cmsensorrecorder/isauthorizedforrecording.md)
  Returns a Boolean value indicating whether the app is authorized to record sensor data.
### Recording Accelerometer Data
- [func recordAccelerometer(forDuration: TimeInterval)](cmsensorrecorder/recordaccelerometer(forduration:).md)
  Begins recording accelerometer data for the specified period of time.
### Retrieving Past Accelerometer Data
- [func accelerometerData(from: Date, to: Date) -> CMSensorDataList?](cmsensorrecorder/accelerometerdata(from:to:).md)
  Retrieves the accelerometer data collected between the specified dates.

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

- [Getting raw accelerometer events](getting-raw-accelerometer-events.md)
  Retrieve data from the onboard accelerometers.
- [class CMAccelerometerData](cmaccelerometerdata.md)
  A data sample from the device’s three accelerometers.
- [class CMRecordedAccelerometerData](cmrecordedaccelerometerdata.md)
  A single piece of accelerometer data that was recorded by the device.
- [class CMSensorDataList](cmsensordatalist.md)
  A list of the accelerometer data recorded by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmsensorrecorder)*