# startRecording()

**Framework**: SensorKit  
**Kind**: method

Starts recording sensor data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final func startRecording() async throws
```

#### Discussion

The reader must be authorized for the sensor for this to succeed. This starts recording on this device and any paired devices. If other readers have already started the sensor recording this reader’s interest in recording will be maintained. Other readers in other apps for the same sensor will not affect the recording status of this reader.

> **Note**: An error if recording cannot be started due to permissions, hardware limitations, or other system restrictions

#### Example

```swift
do {
    try await reader.startRecording()
} catch {
    print("Failed to start recording: \(error)")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/startrecording())*