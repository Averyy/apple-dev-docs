# Cancel Enhanced Log Collection

**Framework**: Device Management  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Cancel enhanced log collection on the device.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

#### Discussion

##### Command availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS |
| User channel | macOS |
| Requires supervision | iOS, macOS, tvOS |
| Allowed in user enrollment | N/A |
| Required access right | N/A |

## Topics

### Commands and responses
- [object CancelEnhancedLogCollectionCommand](./cancelenhancedlogcollectioncommand.md)
  The command to cancel enhanced log collection on the device.
- [object CancelEnhancedLogCollectionResponse](./cancelenhancedlogcollectionresponse.md)
  A response from the device after it processes the command to cancel enhanced log collection on the device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

**Content-Type**: `application/x-apple-aspen-mdm`  
**Type**: `CancelEnhancedLogCollectionCommand`

The request object the server returns for the Cancel Enhanced Log Collection Command.

## Responses

- `200` OK (`CancelEnhancedLogCollectionResponse`, `application/xml`): The response object the system returns for the Cancel Enhanced Log Collection Command.

## See Also

### Enhanced logging
- [Trigger Enhanced Log Collection](./trigger-enhanced-log-collection-command.md)
  Trigger enhanced log collection on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cancel-enhanced-log-collection-command)*