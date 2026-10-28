# SRSensorReaderDelegate

**Framework**: SensorKit  
**Kind**: protocol  
**Role**: Protocol

A set of callbacks the framework invokes to notify the app of sensor-related events.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0

> **Deprecated**: Use SRReader<Sensor> class

## Declaration

```swift
protocol SRSensorReaderDelegate : NSObjectProtocol
```

```objc
@protocol SRSensorReaderDelegate <NSObject>
```

## Overview

To access sensor data, assign an object as the delegate and implement its callbacks.

## Topics

### Checking Authorization Status
- [func sensorReader(SRSensorReader, didChange: SRAuthorizationStatus)](./srsensorreaderdelegate/sensorreader%28_,didchange%29.md)
  Notifies the delegate of the reader’s new authorization status.
### Fetching Devices
- [func sensorReader(SRSensorReader, didFetch: [SRDevice])](./srsensorreaderdelegate/sensorreader%28_,didfetch%29.md)
  Provides the delegate with one or more devices.
- [func sensorReader(SRSensorReader, fetchDevicesDidFailWithError: any Error)](./srsensorreaderdelegate/sensorreader%28_,fetchdevicesdidfailwitherror%29.md)
  Provides the delegate a reason when the reader fails to fetch devices.
- [class SRDevice](./srdevice.md)
  A representation of a device that provides sample data.
### Recording Data
- [func sensorReaderWillStartRecording(SRSensorReader)](./srsensorreaderdelegate/sensorreaderwillstartrecording%28_%29.md)
  Notifies the delegate when a reader starts recording.
- [func sensorReader(SRSensorReader, startRecordingFailedWithError: any Error)](./srsensorreaderdelegate/sensorreader%28_,startrecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to record.
- [func sensorReaderDidStopRecording(SRSensorReader)](./srsensorreaderdelegate/sensorreaderdidstoprecording%28_%29.md)
  Notifies the delegate when a reader stops recording.
- [func sensorReader(SRSensorReader, stopRecordingFailedWithError: any Error)](./srsensorreaderdelegate/sensorreader%28_,stoprecordingfailedwitherror%29.md)
  Provides the delegate with a reason when the reader fails to stop recording.
### Reading Recorded Data
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, didFetchResult: SRFetchResult<AnyObject>) -> Bool](./srsensorreaderdelegate/sensorreader%28_,fetching,didfetchresult%29.md)
  Provides the delegate with a fetch result.
- [func sensorReader(SRSensorReader, didCompleteFetch: SRFetchRequest)](./srsensorreaderdelegate/sensorreader%28_,didcompletefetch%29.md)
  Provides the delegate with a completed fetch request.
- [func sensorReader(SRSensorReader, fetching: SRFetchRequest, failedWithError: any Error)](./srsensorreaderdelegate/sensorreader%28_,fetching,failedwitherror%29.md)
  Provides the delegate with a fetch failure reason.
### Interpreting Errors
- [let SRErrorDomain: String](./srerrordomain.md)
  An error domain that’s unique to the framework.
- [struct SRError](./srerror.md)
  An error that SensorKit reports.
- [SRError.Code](./srerror/code.md)
  The kinds of problems that stop a recording or a fetch.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Responding to sensor events
- [var delegate: (any SRSensorReaderDelegate)?](./srsensorreader/delegate.md)
  An object that responds to sensor-related events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srsensorreaderdelegate)*