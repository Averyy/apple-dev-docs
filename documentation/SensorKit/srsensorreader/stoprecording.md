# stopRecording()

**Framework**: SensorKit  
**Kind**: method

Stops recording sensor data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func stopRecording()
```

#### Discussion

This function requests that the framework stop recording for this reader’s sensor. The framework records on this device and any paired devices. Call [`fetchDevices()`](srsensorreader/fetchdevices().md) to get acquire the full list of devices on which the framework records.

The framework allows a sensor to be recorded simultaneously by multiple readers, either in the same app, or across different apps on the same system. As a result, this function signifies that the caller relinquishes interest in recording the reader’s sensor.

Upon success, the framework calls the delegate’s [`sensorReaderDidStopRecording(_:)`](srsensorreaderdelegate/sensorreaderdidstoprecording(_:).md) callback. Upon failure, the framework calls the delegate’s [`sensorReader(_:stopRecordingFailedWithError:)`](srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:).md).

The reader must be authorized (see [`authorizationStatus`](srsensorreader/authorizationstatus.md)) for this function to succeed.

## See Also

- [func startRecording()](srsensorreader/startrecording.md)
  Starts recording sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording())*