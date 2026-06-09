# updateDevices(_:)

**Framework**: Media Device  
**Kind**: method

Notifies the system that one or more devices have changed state, so their information can be refreshed in device lists.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
@MainActor
final func updateDevices(_ devices: [MediaOutputDevice])
```

## Mentions

- [Creating a media device extension](creating-a-media-device-extension.md)

#### Discussion

Call this function when [`MediaOutputDevice`](mediaoutputdevice.md) instances have had their state updated. This may be called after an activate or deactivate call to reflect updated grouping information.

## Parameters

- `devices`: The devices whose state has been updated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediadevice/mediadeviceroutingmanager/updatedevices(_:))*