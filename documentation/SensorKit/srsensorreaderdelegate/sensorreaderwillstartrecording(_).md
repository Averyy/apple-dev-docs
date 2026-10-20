# sensorReaderWillStartRecording(_:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when a reader starts recording.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReaderWillStartRecording(_ reader: SRSensorReader)
```

```objc
- (void) sensorReaderWillStartRecording:(SRSensorReader *) reader;
```

## Parameters

- `reader`: The reader that stopped recording.

## See Also

### Recording Data
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](./sensorreader%28_,startrecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReaderDidStopRecording(SRSensorReader)](./sensorreaderdidstoprecording%28_%29.md)
  Notifies the delegate when a reader stops recording.
- [func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)](./sensorreader%28_,stoprecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to stop recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))*