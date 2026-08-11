# deletionRecords(matching:)

**Framework**: SensorKit  
**Kind**: method

Fetches sensor data based on the provided request parameters. The reader must be authorized for the sensor for this to succeed.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func deletionRecords(matching request: SRFetchRequest) -> some AsyncSequence<SRFetchResponse<SRDeletionRecord>, any Error>
```

#### Return Value

An `AsyncSequence` that yields `SRFetchResponse<SRDeletionRecord>` objects.

#### Discussion

Creates an asynchronous stream of deletion records. The stream continues to yield data until the fetch request is complete, an error occurs, or the stream is cancelled.

#### Example

```swift
let fetchRequest = SRFetchRequest()
for try await response in visitsReader.deletionRecords(matching: fetchRequest) {
    switch response.sample {
    case .success(let sample):
        print("Start Time:\(sample.startTime)")
        print("Reason \(sample.reason)")
    case .failure(let error):
        print("Error decoding sample: \(error)")
    }
}
```

#### Cancellation

The stream can be cancelled by breaking out of the iteration loop or by the system when the reader is deallocated. Cancellation stops the fetch operation gracefully.

## Parameters

- `request`: An `SRFetchRequest` specifying the data range, filters, and other fetch parameters


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/deletionrecords(matching:))*