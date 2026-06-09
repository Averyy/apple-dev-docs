# init(id:name:type:capabilities:)

**Framework**: Now Playing  
**Kind**: init

Creates a media device with the specified identifier, name, type, and capabilities.

**Availability**:
- iOS 27.0+ (Beta)
- iOS App Extension 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
init(id: String, name: String, type: MediaDevice.DeviceType, capabilities: [MediaDevice.Capability])
```

#### Discussion

> **Note**: `id` should be a stable identifier for the device that works across sessions.

## Parameters

- `id`: A stable, unique identifier for the device.
- `name`: The human-readable name the system displays for the device.
- `type`: The kind of device that plays media.
- `capabilities`: The capabilities the device supports. Each value in the array describes one operation the device supports, built from a [`MediaDevice.Capability`](mediadevice/capability.md), such as [`absoluteVolume(_:onChange:)`](mediadevice/capability/absolutevolume(_:onchange:).md) or [`relativeVolume(onIncrement:onDecrement:)`](mediadevice/capability/relativevolume(onincrement:ondecrement:).md). Pass an empty array if the device exposes no controllable capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nowplaying/mediadevice/init(id:name:type:capabilities:))*