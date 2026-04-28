# EraseDeviceCommand.Command.ReturnToService

**Framework**: Device Management  
**Kind**: dictionary

The configuration settings for return to service.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 18.0+
- visionOS 26.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object EraseDeviceCommand.Command.ReturnToService
```

## Properties

- `BootstrapToken` (data): The bootstrap token the system uses to implement return to service with app preservation. Required when enabling return to service through the cloud configuration.
- `Enabled` (boolean) *(required)*: If `true`, the device tries to reenroll itself automatically after erasure. The user needs to deactivate all activation locks for this feature to work correctly.
- `MDMProfileData` (data): The MDM profile that installs after erasure when using return to service. This key is required for all unsupervised devices, as well as supervised devices that don’t enroll with Automated Device Enrollment. If provided, the device uses this profile directly instead of fetching it from the server. For devices that enroll with Automated Device Enrollment, this key isn’t necessary unless the cloud configuration profile of the device contains the `configuration-web-url` key. The cloud configuration still downloads from Apple’s servers when the profile contains this key, so the supervision identity, MDM removability, and other settings from the cloud configuration still apply. However, the device doesn’t use the specified URL in the cloud configuration to fetch the MDM profile.
- `WiFiProfileData` (data): The Wi-Fi profile that installs after erasure when using return to service. This is required when the device doesn’t have an Ethernet or cellular connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/erasedevicecommand/command-data.dictionary/returntoservice-data.dictionary)*