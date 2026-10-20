# configureDevice(named:in:)

**Framework**: MatterSupport  
**Kind**: method  
**Role**: Instance Method

Configures the device with selected attributes.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
func configureDevice(named name: String, in room: MatterAddDeviceRequest.Room?) async
```

## Parameters

- `name`: The selected name for the device.
- `room`: The selected room for the device.

## See Also

### Configuring and validating the device
- [func validateDeviceCredential(MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws](./validatedevicecredential%28_%29.md)
  Performs verification and attestation checks.
- [MatterAddDeviceExtensionRequestHandler.DeviceCredential](./devicecredential.md)
  A collection of device credentials the device presents during commissioning.
- [func rooms(in: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room]](./rooms%28in%29.md)
  Provides rooms that correspond to a home in the device setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/configuredevice(named:in:))*