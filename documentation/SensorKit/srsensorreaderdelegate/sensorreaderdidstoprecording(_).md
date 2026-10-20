# sensorReaderDidStopRecording(_:)

**Framework**: SensorKit  
**Kind**: method  
**Role**: Instance Method

Notifies the delegate when a reader stops recording.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
optional func sensorReaderDidStopRecording(_ reader: SRSensorReader)
```

```objc
- (void) sensorReaderDidStopRecording:(SRSensorReader *) reader;
```

## Parameters

- `reader`: The reader that stopped recording.

## See Also

### Recording Data
- [func sensorReaderWillStartRecording(SRSensorReader)](./sensorreaderwillstartrecording%28_%29.md)
  Notifies the delegate when a reader starts recording.
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](./sensorreader%28_,startrecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)](./sensorreader%28_,stoprecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to stop recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))*