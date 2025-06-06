# MatterAddDeviceExtensionRequestHandler.DeviceCredential

**Framework**: MatterSupport  
**Kind**: struct

A collection of device credentials the device presents during commissioning.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 14.0+
- visionOS ?+

## Declaration

```swift
struct DeviceCredential
```

## Topics

### Creating the credential
- [init(certificationDeclaration: Data, deviceAttestationCertificate: Data, productAttestationIntermediateCertificate: Data)](matteradddeviceextensionrequesthandler/devicecredential/init(certificationdeclaration:deviceattestationcertificate:productattestationintermediatecertificate:).md)
  Creates the credential object.
### Getting the properties
- [var certificationDeclaration: Data](matteradddeviceextensionrequesthandler/devicecredential/certificationdeclaration.md)
  The device’s Certification Declaration as defined in the Matter specification.
- [var deviceAttestationCertificate: Data](matteradddeviceextensionrequesthandler/devicecredential/deviceattestationcertificate.md)
  The device’s Device Attestation Certificate as defined in the Matter specification.
- [var productAttestationIntermediateCertificate: Data](matteradddeviceextensionrequesthandler/devicecredential/productattestationintermediatecertificate.md)
  The device’s Product Attestation Intermediate Certificate as defined in the Matter specification.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func configureDevice(named: String, in: MatterAddDeviceRequest.Room?) async](matteradddeviceextensionrequesthandler/configuredevice(named:in:).md)
  Configures the device with selected attributes.
- [func validateDeviceCredential(MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws](matteradddeviceextensionrequesthandler/validatedevicecredential(_:).md)
  Performs verification and attestation checks.
- [func rooms(in: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room]](matteradddeviceextensionrequesthandler/rooms(in:).md)
  Provides rooms that correspond to a home in the device setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/devicecredential)*