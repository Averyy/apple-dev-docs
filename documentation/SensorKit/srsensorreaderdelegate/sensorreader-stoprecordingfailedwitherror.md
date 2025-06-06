# sensorReader(_:stopRecordingFailedWithError:)

**Framework**: SensorKit  
**Kind**: method

Provides the delegate with a reason when the reader fails to stop recording.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
optional func sensorReader(_ reader: SRSensorReader, stopRecordingFailedWithError error: any Error)
```

## Parameters

- `reader`: The sensor reader that failed to stop recording.
- `error`: An object that describes the cause of failure.

## See Also

- [func sensorReaderWillStartRecording(SRSensorReader)](srsensorreaderdelegate/sensorreaderwillstartrecording(_:).md)
  Notifies the delegate when a reader starts recording.
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReaderDidStopRecording(SRSensorReader)](srsensorreaderdelegate/sensorreaderdidstoprecording(_:).md)
  Notifies the delegate when a reader stops recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:))*