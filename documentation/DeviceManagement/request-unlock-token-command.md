# Request the Unlock Token

**Framework**: Device Management  
**Kind**: httpRequest

Request an unlock token from a device.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Device Assignment Services ?+
- VPP License Management ?+

#### Discussion

Refer to the following sections to determine supported channels and requirements, and to see an example request and response.

##### Command Availability

|  |  |
| --- | --- |
| Device Channel | iOS |
| User Channel | - |
| Requires Supervision | iOS |
| Allowed in User Enrollment | - |
| Required Access Right | AllowPasscodeRemovalAndLock |

## Topics

### Command and Response
- [object RequestUnlockTokenCommand](requestunlocktokencommand.md)
  The command to request an unlock token from a device.
- [object RequestUnlockTokenResponse](requestunlocktokenresponse.md)
  A response from the device after it processes a request for an unlock token.

## Request Body

The command to request an unlock token from a device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/request-unlock-token-command)*