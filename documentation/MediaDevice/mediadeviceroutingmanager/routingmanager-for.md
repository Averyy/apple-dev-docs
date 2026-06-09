# routingManager(for:)

**Framework**: Media Device  
**Kind**: method

Returns the shared routing manager instance for a media device extension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
static func routingManager(for extension: any MediaDeviceExtension) -> MediaDeviceRoutingManager
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Return Value

The shared [`MediaDeviceRoutingManager`](mediadeviceroutingmanager.md) instance.

#### Discussion

Use this method to obtain the shared [`MediaDeviceRoutingManager`](mediadeviceroutingmanager.md) instance for your extension. The routing manager is how your extension reports device discovery, state changes, and playback events to the system.

> **Note**: The routing manager is a shared instance. Calling this method multiple times for a given extension returns the same [`MediaDeviceRoutingManager`](mediadeviceroutingmanager.md) instance.

## Parameters

- `extension`: The extension to obtain the routing manager for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/routingmanager(for:))*