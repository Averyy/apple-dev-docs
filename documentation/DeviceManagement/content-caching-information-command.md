# Content Caching Information

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the status of the content caches on a device.

**Availability**:
- macOS 10.15.4+

#### Discussion

##### Command availability

|  |  |
| --- | --- |
| Device channel | macOS |
| User channel | N/A |
| Requires supervision | macOS |
| Allowed in user enrollment | N/A |
| Required access right | AllowQueryNetworkInformation |

## Topics

### Commands and responses
- [object ContentCachingInformationCommand](./contentcachinginformationcommand.md)
  The command to get the status of the content caches on a device.
- [object ContentCachingInformationResponse](./contentcachinginformationresponse.md)
  A response from the device after it processes the command to get the status of the content caches on a device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `ContentCachingInformationCommand`

The request object the server returns for the Content Caching Information Command.

## Responses

- `200` OK (`ContentCachingInformationResponse`, `application/xml`): The response object the system returns for the Content Caching Information Command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/content-caching-information-command)*