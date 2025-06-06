# startRecording()

**Framework**: SensorKit  
**Kind**: method

Starts recording sensor data.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
func startRecording()
```

#### Discussion

This function instructs the framework to start recording for this reader’s sensor. The framework records on this device and any paired devices. Call [`fetchDevices()`](srsensorreader/fetchdevices().md) to acquire the full list of devices on which the framework records.

The framework allows a sensor to be recorded simultaneously by multiple readers, either in the same app or across different apps on the same system. On multiple calls to this function, the framework just ensures that recording for the sensor is active.

Upon success, the framework calls the delegate’s [`sensorReaderWillStartRecording(_:)`](srsensorreaderdelegate/sensorreaderwillstartrecording(_:).md) callback. Upon failure, the framework calls the delegate’s [`sensorReader(_:startRecordingFailedWithError:)`](srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:).md).

The reader must be authorized (see [`authorizationStatus`](srsensorreader/authorizationstatus.md)) for this function to succeed.

## See Also

- [func stopRecording()](srsensorreader/stoprecording.md)
  Stops recording sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())*