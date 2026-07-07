# SRFetchResponse

**Framework**: SensorKit  
**Kind**: struct

A generic container that holds sensor data samples retrieved from SensorKit data streams.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
struct SRFetchResponse<Sample>
```

#### Overview

`SRFetchResponse` is a type-safe container that wraps individual sensor data samples. It serves as the primary data delivery mechanism for sensor information retrieved through `SRReader.fetch(_:)` operations.

#### Usage Example

```swift
let request = SRFetchRequest()
for try await response in reader.fetch(request) {
    // Extract the sensor sample
    switch response.sample {
    case .success(let sample):
        print("Sample data: \(sample)")
    case .failure(let error):
        print("Failed to decode sample: \(error)")
    }

    // Get the timestamp when data was recorded
    let timestamp = response.timestamp()
    print("Recorded at: \(Date(timeIntervalSinceReferenceDate: timestamp))")
}
```

## Topics

### Instance Properties
- [var sample: Result<Sample, any Error>](srfetchresponse/sample.md)
  Retrieves the sensor-specific data sample contained in this response.
- [var sourceDevice: SRSourceDevice?](srfetchresponse/sourcedevice.md)
  The source of the sample data.
- [var timestamp: SRAbsoluteTime](srfetchresponse/timestamp.md)
  Retrieves the timestamp when the sensor sample was written to the data store.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srfetchresponse)*