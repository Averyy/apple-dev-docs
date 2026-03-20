# register(_:_:)

**Framework**: AudioAccessoryKit  
**Kind**: method

Registers the audio accessory with the system and activates its configured capabilities.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
nonisolated
(nonsending) static func register(_ accessory: ASAccessory, _ configuration: AccessoryControlDevice.Configuration) async throws
```

#### Discussion

> ❗ **Important**: Call this method only from your container app.

To activate audio features like automatic switching, call this method after pairing your accessory using AccessorySetupKit.

This method throws an error if registration fails.

## Parameters

- `accessory`: The accessory to register.
- `configuration`: The configuration for the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice/register(_:_:))*