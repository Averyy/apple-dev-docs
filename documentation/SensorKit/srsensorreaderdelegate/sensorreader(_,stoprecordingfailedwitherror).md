# sensorReader(_:stopRecordingFailedWithError:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Provides the delegate with a reason when the reader fails to stop recording.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, stopRecordingFailedWithError error: any Error)
```

```objc
- (void) sensorReader:(SRSensorReader *) reader stopRecordingFailedWithError:(NSError *) error;
```

## Parameters

- `reader`: The sensor reader that failed to stop recording.
- `error`: An object that describes the cause of failure.

## See Also

### Recording Data
- [func sensorReaderWillStartRecording(SRSensorReader)](./sensorreaderwillstartrecording%28_%29.md)
  Notifies the delegate when a reader starts recording.
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](./sensorreader%28_,startrecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReaderDidStopRecording(SRSensorReader)](./sensorreaderdidstoprecording%28_%29.md)
  Notifies the delegate when a reader stops recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))*