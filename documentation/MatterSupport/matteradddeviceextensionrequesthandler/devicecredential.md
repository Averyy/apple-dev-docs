# MatterAddDeviceExtensionRequestHandler.DeviceCredential

**Framework**: MatterSupport  
**Kind**: struct  
**Role**: Structure

A collection of device credentials the device presents during commissioning.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.1+
- macOS 14.0+
- visionOS

## Declaration

```swift
struct DeviceCredential
```

## Topics

### Creating the credential
- [init(certificationDeclaration: Data, deviceAttestationCertificate: Data, productAttestationIntermediateCertificate: Data)](./devicecredential/init%28certificationdeclaration,deviceattestationcertificate,productattestationintermediatecertificate%29.md)
  Creates the credential object.
### Getting the properties
- [var certificationDeclaration: Data](./devicecredential/certificationdeclaration.md)
  The device’s Certification Declaration as defined in the Matter specification.
- [var deviceAttestationCertificate: Data](./devicecredential/deviceattestationcertificate.md)
  The device’s Device Attestation Certificate as defined in the Matter specification.
- [var productAttestationIntermediateCertificate: Data](./devicecredential/productattestationintermediatecertificate.md)
  The device’s Product Attestation Intermediate Certificate as defined in the Matter specification.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring and validating the device
- [func configureDevice(named: String, in: MatterAddDeviceRequest.Room?) async](./configuredevice%28named,in%29.md)
  Configures the device with selected attributes.
- [func validateDeviceCredential(MatterAddDeviceExtensionRequestHandler.DeviceCredential) async throws](./validatedevicecredential%28_%29.md)
  Performs verification and attestation checks.
- [func rooms(in: MatterAddDeviceRequest.Home?) async -> [MatterAddDeviceRequest.Room]](./rooms%28in%29.md)
  Provides rooms that correspond to a home in the device setup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mattersupport/matteradddeviceextensionrequesthandler/devicecredential)*