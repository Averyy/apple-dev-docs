# devices

**Framework**: SensorKit  
**Kind**: property

Returns device information for all devices that have stored data for the given sensor in SensorKit

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
final var devices: [SRDevice] { get async throws }
```

#### Return Value

An array of `SRDevice` objects representing available sensor devices

#### Discussion

> **Note**: An error if the request failed

#### Example

```swift
do {
    let devices = try await reader.devices
    for device in devices {
        print("Device: \(device.name), Model: \(device.model)")
    }
} catch {
    print("Failed to fetch devices: \(error)")
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/devices)*