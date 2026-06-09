# init(sensor:)

**Framework**: SensorKit  
**Kind**: init

Creates a new sensor reader for the specified sensor type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(sensor: Sensor) throws
```

#### Return Value

A new `SRReader` instance

#### Discussion

This initializer attempts to create a reader for the given sensor.

> **Note**: An error if cannot create reader due to hardware limitations or internal error

#### Example

```swift
do {
    let reader = try SRReader(sensor: .wristTemperature)
} catch {
    NSLog("Failed to create reader: \(error)")
    return
}
```

## Parameters

- `sensor`: The sensor type to create a reader for (e.g., `.wristTemperature`, `.heartRate`)


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srreader/init(sensor:))*