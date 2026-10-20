# startRecording()

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Starts recording sensor data.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
func startRecording()
```

```objc
- (void) startRecording;
```

#### Discussion

This function instructs the framework to start recording for this reader’s sensor. The framework records on this device and any paired devices. Call [`fetchDevices()`](./fetchdevices%28%29.md) to acquire the full list of devices on which the framework records.

The framework allows a sensor to be recorded simultaneously by multiple readers, either in the same app or across different apps on the same system. On multiple calls to this function, the framework just ensures that recording for the sensor is active.

Upon success, the framework calls the delegate’s [`sensorReaderWillStartRecording(_:)`](../srsensorreaderdelegate/sensorreaderwillstartrecording%28_%29.md) callback. Upon failure, the framework calls the delegate’s [`sensorReader(_:startRecordingFailedWithError:)`](../srsensorreaderdelegate/sensorreader%28_,startrecordingfailedwitherror%29.md).

The reader must be authorized (see [`authorizationStatus`](./authorizationstatus.md)) for this function to succeed.

## See Also

### Recording sensor data
- [func stopRecording()](./stoprecording%28%29.md)
  Stops recording sensor data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreader/startrecording())*