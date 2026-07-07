# samples(matching:)

**Framework**: SensorKit  
**Kind**: method

Fetches sensor data based on the provided request parameters. The reader must be authorized for the sensor for this to succeed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
final func samples(matching request: SRFetchRequest) -> some AsyncSequence<SRFetchResponse<Sensor.Sample>, any Error>
```

#### Return Value

An `AsyncSequence` that yields `SRFetchResponse<Sensor.Sample>` objects containing the sensor-specific data

#### Discussion

Creates an asynchronous stream of sensor data responses. The stream continues to yield data until the fetch request is complete, an error occurs, or the stream is cancelled.

#### Example

```swift
for try await response in reader.samples(matching: request) {
    // Process each data sample
    switch response.sample {
    case .success(let sample):
        print("Sample data: \(sample)")
    case .failure(let error):
        print("Failed to decode sample: \(error)")
    }

    print("Timestamp: \(response.timestamp)")
}
```

#### Cancellation

The stream can be cancelled by breaking out of the iteration loop or by the system when the reader is deallocated. Cancellation stops the fetch operation gracefully.

## Parameters

- `request`: An `SRFetchRequest` specifying the data range, filters, and other fetch parameters


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/samples(matching:))*