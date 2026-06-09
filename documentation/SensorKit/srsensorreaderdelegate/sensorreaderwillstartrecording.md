# sensorReaderWillStartRecording(_:)

**Framework**: SensorKit  
**Kind**: method

Notifies the delegate when a reader starts recording.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+

## Declaration

```swift
optional func sensorReaderWillStartRecording(_ reader: SRSensorReader)
```

## Parameters

- `reader`: The reader that stopped recording.

## See Also

- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReaderDidStopRecording(SRSensorReader)](srsensorreaderdelegate/sensorreaderdidstoprecording(_:).md)
  Notifies the delegate when a reader stops recording.
- [func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to stop recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreaderwillstartrecording(_:))*