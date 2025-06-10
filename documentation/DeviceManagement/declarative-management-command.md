# Declarative Management

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

#### Discussion

The server uses this command to turn on the declarative management engine on the device the first time the server sends it. Subsequent commands trigger a declarative management synchronization operation.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, macOS, Shared iPad, tvOS, visionOS, watchOS |
| User channel | macOS, Shared iPad |
| Requires supervision | NA |
| Allowed in user enrollment | iOS, macOS, visionOS |
| Required access right |  |

##### Example Request and Response

## Topics

### Commands and responses
- [object DeclarativeManagementCommand](declarativemanagementcommand.md)
  The command to enable your server to support declarative management or trigger a declarative management synchronization operation on the device.
- [object DeclarativeManagementResponse](declarativemanagementresponse.md)
  A response from the device after it processes the command to enable your server to support declarative management or trigger a declarative management synchronization operation on the device.

## Request Body

The request object the server returns for the Declarative Management Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/declarative-management-command)*