# stopRecording()

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Stops recording sensor data.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
func stopRecording()
```

```objc
- (void) stopRecording;
```

#### Discussion

This function requests that the framework stop recording for this reader’s sensor. The framework records on this device and any paired devices. Call [`fetchDevices()`](./fetchdevices%28%29.md) to get acquire the full list of devices on which the framework records.

The framework allows a sensor to be recorded simultaneously by multiple readers, either in the same app, or across different apps on the same system. As a result, this function signifies that the caller relinquishes interest in recording the reader’s sensor.

Upon success, the framework calls the delegate’s [`sensorReaderDidStopRecording(_:)`](../srsensorreaderdelegate/sensorreaderdidstoprecording%28_%29.md) callback. Upon failure, the framework calls the delegate’s [`sensorReader(_:stopRecordingFailedWithError:)`](../srsensorreaderdelegate/sensorreader%28_,stoprecordingfailedwitherror%29.md).

The reader must be authorized (see [`authorizationStatus`](./authorizationstatus.md)) for this function to succeed.

## See Also

### Recording sensor data
- [func startRecording()](./startrecording%28%29.md)
  Starts recording sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/stoprecording())*