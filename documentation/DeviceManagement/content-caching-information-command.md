# Content Caching Information

**Framework**: Device Management  
**Kind**: httpRequest

Get the status of the content caches on a device.

**Availability**:
- macOS 10.15.4+

#### Discussion

##### Command Availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | NA |
| Requires supervision | macOS |
| Allowed in user enrollment | NA |
| Required access right | AllowQueryNetworkInformation |

## Topics

### Commands and responses
- [object ContentCachingInformationCommand](contentcachinginformationcommand.md)
  The command to get the status of the content caches on a device.
- [object ContentCachingInformationResponse](contentcachinginformationresponse.md)
  A response from the device after it processes the command to get the status of the content caches on a device.

## Request Body

The request object the server returns for the Content Caching Information Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/content-caching-information-command)*