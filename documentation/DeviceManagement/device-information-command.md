# Device Information

**Framework**: Device Management  
**Kind**: httpRequest

Get detailed information about a device.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.1+
- watchOS 10.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Deviceinformation Attestation Hardware Support

The following table indicates which System on Chips (SoCs) support DeviceInformation attestation. Unsupported devices ignore the DevicePropertiesAttestation and DeviceAttestationNonce keys.

| Support status | iPhone, iPad | Mac | Apple TV | Apple Watch | Vision Pro |
| --- | --- | --- | --- | --- | --- |
| Unsupported | A10x Fusion and earlier | Intel | A10x Fusion and earlier | S3 and earlier | none |
| Supported | A11 Bionic and laterAll M series | Apple Silicon | A12 Bionic and later | S4 and later | All |

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right | Special Case |

##### Example Request and Response

## Topics

### Commands and responses
- [object DeviceInformationCommand](deviceinformationcommand.md)
  The command to get detailed information about a device.
- [object DeviceInformationResponse](deviceinformationresponse.md)
  A response from the device after it processes the command to get detailed information about a device.

## Request Body

The request object the server returns for the Device Information Command.

## See Also

- [Installed Application List](installed-application-list-command.md)
  Get a list of the installed apps on a device.
- [Device Configured](device-configured-command.md)
  Inform the device that it can allow the user to continue in Setup Assistant.
- [User Configured](user-configured-command.md)
  Inform the device that it can continue past Setup Assistant and finish login.
- [Restrictions](restrictions-command.md)
  Get a list of restrictions on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/device-information-command)*