# Cancel Enhanced Log Collection

**Framework**: Device Management  
**Kind**: httpRequest

Cancel enhanced log collection on the device.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

#### Discussion

##### Command Availability

|  |  |
| --- | --- |
| Device channel | iOS, Shared iPad, tvOS |
| User channel | macOS |
| Requires supervision | iOS, macOS, tvOS |
| Allowed in user enrollment | N/A |
| Required access right | N/A |

## Topics

### Commands and responses
- [object CancelEnhancedLogCollectionCommand](cancelenhancedlogcollectioncommand.md)
  The command to cancel enhanced log collection on the device.
- [object CancelEnhancedLogCollectionResponse](cancelenhancedlogcollectionresponse.md)
  A response from the device after it processes the command to cancel enhanced log collection on the device.

## Endpoint

`PUT https://yourmdmhost.example.com/mdm`

## Request Body

The request object the server returns for the Cancel Enhanced Log Collection Command.

## See Also

- [Trigger Enhanced Log Collection](trigger-enhanced-log-collection-command.md)
  Trigger enhanced log collection on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/cancel-enhanced-log-collection-command)*