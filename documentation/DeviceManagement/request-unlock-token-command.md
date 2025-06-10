# Request Unlock Token

**Framework**: Device Management  
**Kind**: httpRequest

Request an unlock token from a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS |
| User channel | NA |
| Requires supervision | iOS |
| Allowed in user enrollment | NA |
| Required access right | NA |

## Topics

### Commands and responses
- [object RequestUnlockTokenCommand](requestunlocktokencommand.md)
  The command to request an unlock token from a device.
- [object RequestUnlockTokenResponse](requestunlocktokenresponse.md)
  A response from the device after it processes the command to request an unlock token from a device.

## Request Body

The request object the server returns for the Request Unlock Token Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/request-unlock-token-command)*