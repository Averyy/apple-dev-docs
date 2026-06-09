# stopRecording()

**Framework**: SensorKit  
**Kind**: method

Stops recording sensor data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func stopRecording() async throws
```

#### Discussion

The reader must be authorized for the sensor for this to succeed. This stops recording on this device and any paired devices. Sensor recording will continue until the last interested reader has stopped recording.

> **Note**: An error if the stop operation fails

#### Example

```swift
do {
    try await reader.stopRecording()
} catch {
    print("Failed to stop recording: \(error)")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/stoprecording())*