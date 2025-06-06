# configureDevice(named:in:)

**Framework**: MatterSupport  
**Kind**: method

Configures the device with selected attributes.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
func configureDevice(named name: String, in room: MatterAddDeviceRequest.Room?) async
```

## Parameters

- `name`: The selected name for the device.
- `room`: The selected room for the device.

## See Also

- [func validateDeviceCredential(MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws](matteradddeviceextensionrequesthandler/validatedevicecredential(_:).md)
  Performs verification and attestation checks.
- [MatterAddDeviceExtensionRequestHandler.DeviceCredential](matteradddeviceextensionrequesthandler/devicecredential.md)
  A collection of device credentials the device presents during commissioning.
- [func rooms(in: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room]](matteradddeviceextensionrequesthandler/rooms(in:).md)
  Provides rooms that correspond to a home in the device setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/configuredevice(named:in:))*