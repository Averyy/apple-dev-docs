# SRReader

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

`SRReader` serves as the primary interface for accessing sensor data from various device sensors.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+

## Declaration

```swift
final class SRReader<Sensor> where Sensor : SRDataSensor
```

## Topics

### Initializers
- [init(sensor: Sensor) throws](./srreader/init%28sensor%29.md)
  Creates a new sensor reader for the specified sensor type.
### Instance Properties
- [var authorizationStatus: SRAuthorizationStatus](./srreader/authorizationstatus.md)
  The current authorization status for accessing the sensor data.
- [var devices: [SRDevice]](./srreader/devices.md)
  Returns device information for all devices that have stored data for the given sensor in SensorKit
- [let sensor: Sensor](./srreader/sensor.md)
  The sensor instance associated with this reader.
### Instance Methods
- [func deletionRecords(matching: SRFetchRequest) -> some AsyncSequence<SRFetchResponse<SRDeletionRecord>, any Error>
](./srreader/deletionrecords%28matching%29.md)
  Fetches sensor data based on the provided request parameters. The reader must be authorized for the sensor for this to succeed.
- [func samples(matching: SRFetchRequest) -> some AsyncSequence<SRFetchResponse<Sensor.Sample>, any Error>
](./srreader/samples%28matching%29.md)
  Fetches sensor data based on the provided request parameters. The reader must be authorized for the sensor for this to succeed.
- [func startRecording() async throws](./srreader/startrecording%28%29.md)
  Starts recording sensor data.
- [func stopRecording() async throws](./srreader/stoprecording%28%29.md)
  Stops recording sensor data.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [Escapable](../Swift/escapable.md)
- [Observable](../Observation/observable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader)*