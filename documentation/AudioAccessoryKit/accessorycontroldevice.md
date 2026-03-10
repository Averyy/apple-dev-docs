# AccessoryControlDevice

**Framework**: AudioAccessoryKit  
**Kind**: class

A configuration object that manages audio accessory capabilities and state.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)

## Declaration

```swift
final class AccessoryControlDevice
```

## Mentions

- [Supporting automatic audio switching for third-party accessories](supporting-automatic-audio-switching.md)

#### Overview

This class registers your paired audio accessory with the system and provides updates about your device’s state changes. The configuration lets the system intelligently switch the audio output device, based on information you provide the system, such as placement and connected devices.

## Topics

### Accessing the current configuration
- [static func current(for: ASAccessory) throws -> AccessoryControlDevice](accessorycontroldevice/current(for:).md)
  Retrieves the accessory’s current configuration.
### Registering the device
- [static func register(ASAccessory, AccessoryControlDevice.Configuration) async throws](accessorycontroldevice/register(_:_:).md)
  Registers the audio accessory with the system and activates its configured capabilities.
### Updating device state
- [func update(AccessoryControlDevice.Configuration) async throws](accessorycontroldevice/update(_:).md)
  Updates the accessory’s configuration.
### Inspecting the accessory
- [let accessory: ASAccessory](accessorycontroldevice/accessory.md)
  An AccessorySetupKit accessory that represents the audio device.
- [var configuration: AccessoryControlDevice.Configuration](accessorycontroldevice/configuration-swift.property.md)
  The current configuration of the device.
### Defining device characteristics
- [AccessoryControlDevice.Placement](accessorycontroldevice/placement.md)
  The physical placement of an audio accessory.
- [AccessoryControlDevice.Capabilities](accessorycontroldevice/capabilities.md)
  A set of capabilities that an audio accessory supports.
- [AccessoryControlDevice.Configuration](accessorycontroldevice/configuration-swift.struct.md)
  The configuration for an accessory.
### Handling errors
- [AccessoryControlDevice.Error](accessorycontroldevice/error.md)
  An error that occurs during audio accessory configuration operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audioaccessorykit/accessorycontroldevice)*