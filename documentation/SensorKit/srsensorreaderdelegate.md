# SRSensorReaderDelegate

**Framework**: SensorKit  
**Kind**: protocol

A set of callbacks the framework invokes to notify the app of sensor-related events.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
protocol SRSensorReaderDelegate : NSObjectProtocol
```

#### Overview

To access sensor data, assign an object as the delegate and implement its callbacks.

## Topics

### Checking Authorization Status
- [func sensorReader(SRSensorReader, didChange: SRAuthorizationStatus)](srsensorreaderdelegate/sensorreader(_:didchange:).md)
  Notifies the delegate of the reader’s new authorization status.
### Fetching Devices
- [func sensorReader(SRSensorReader, didFetch: [SRDevice])](srsensorreaderdelegate/sensorreader(_:didfetch:).md)
  Provides the delegate with one or more devices.
- [func sensorReader(SRSensorReader, fetchDevicesDidFailWithError: any Error)](srsensorreaderdelegate/sensorreader(_:fetchdevicesdidfailwitherror:).md)
  Provides the delegate a reason when the reader fails to fetch devices.
- [class SRDevice](srdevice.md)
  A representation of a device that provides sample data.
### Recording Data
- [func sensorReaderWillStartRecording(SRSensorReader)](srsensorreaderdelegate/sensorreaderwillstartrecording(_:).md)
  Notifies the delegate when a reader starts recording.
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:startrecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReaderDidStopRecording(SRSensorReader)](srsensorreaderdelegate/sensorreaderdidstoprecording(_:).md)
  Notifies the delegate when a reader stops recording.
- [func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:stoprecordingfailedwitherror:).md)
  Provides the delegate with a reason when the reader fails to stop recording.
### Reading Recorded Data
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool](srsensorreaderdelegate/sensorreader(_:fetching:didfetchresult:).md)
  Provides the delegate with a fetch result.
- [func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)](srsensorreaderdelegate/sensorreader(_:didcompletefetch:).md)
  Provides the delegate with a completed fetch request.
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)](srsensorreaderdelegate/sensorreader(_:fetching:failedwitherror:).md)
  Provides the delegate with a fetch failure reason.
### Interpreting Errors
- [let SRErrorDomain: String](srerrordomain.md)
  An error domain that’s unique to the framework.
- [struct SRError](srerror.md)
  An error that SensorKit reports.
- [SRError.Code](srerror/code.md)
  The kinds of problems that stop a recording or a fetch.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any SRSensorReaderDelegate)?](srsensorreader/delegate.md)
  An object that responds to sensor-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)*