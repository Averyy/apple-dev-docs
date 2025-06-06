# Enable Declarative Management

**Framework**: Device Management  
**Kind**: httpRequest

Enable your server to support declarative management or trigger a declarative management synchronization operation on the device.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.1+
- watchOS 10.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS, macOS, Shared iPad, tvOS, watchOS |
| User Channel | - |
| Requires Supervision | - |
| Allowed in User Enrollment | iOS, macOS |
| Required Access Right | - |

##### Example Request and Response

## Topics

### Command and Response
- [object DeclarativeManagementCommand](declarativemanagementcommand.md)
  The command to issue declarations to a device.
- [object DeclarativeManagementResponse](declarativemanagementresponse.md)
  A response from the device after it processes the command to issue declarations to a device.

## Request Body

The command to issue declarations to a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarative-management-command)*