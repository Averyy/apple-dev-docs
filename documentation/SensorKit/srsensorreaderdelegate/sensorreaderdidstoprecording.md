# sensorReaderDidStopRecording(_:)

**Framework**: SensorKit  
**Kind**: method

Notifies the delegate when a reader stops recording.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReaderDidStopRecording(_ reader: SRSensorReader)
```

## Parameters

- `reader`: The reader that stopped recording.

## See Also

- [func sensorReaderWillStartRecording(SRSensorReader)](srsensorreaderdelegate/sensorreaderwillstartrecording(_:).md)
  Notifies the delegate when a reader starts recording.
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to stop recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderdidstoprecording(_:))*