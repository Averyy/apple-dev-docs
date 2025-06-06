# validateDeviceCredential(_:)

**Framework**: MatterSupport  
**Kind**: method

Performs verification and attestation checks.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
func validateDeviceCredential(_ deviceCredential: MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws
```

#### Overview

Override this method to perform additional verification and attestation checks, which execute after Apple’s built-in device attestation checks. If either attestation fails as indicated by an exception thrown here, a warning dialog appears before proceeding.

This is the first callback that the system invokes during the setup flow. It runs after selecting a device but before commissioning, and can abort commissioning if the credential is rejected by throwing an exception.

## See Also

- [func configureDevice(named: String, in: MatterAddDeviceRequest.Room?) async](matteradddeviceextensionrequesthandler/configuredevice(named:in:).md)
  Configures the device with selected attributes.
- [MatterAddDeviceExtensionRequestHandler.DeviceCredential](matteradddeviceextensionrequesthandler/devicecredential.md)
  A collection of device credentials the device presents during commissioning.
- [func rooms(in: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room]](matteradddeviceextensionrequesthandler/rooms(in:).md)
  Provides rooms that correspond to a home in the device setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/validatedevicecredential(_:))*