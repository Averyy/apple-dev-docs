# Return To Service

**Framework**: Device Management  
**Kind**: httpRequest

Gets the return-to-service configuration from the server.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Mentions

- [Returning a managed device to service](returning-a-managed-device-to-service.md)

#### Discussion

The device sends the `ReturnToService` message when the user triggers a return to service, or when the device’s idle timeout expires. The device only sends this message when it’s in the return-to-service mode that its Automated Device Enrollment profile sets.

##### Check in Availability

|  |  |
| --- | --- |
| Device channel | iOS, visionOS |
| User channel | NA |
| Requires supervision | iOS, visionOS |
| Allowed in user enrollment | NA |

## Topics

### Requests and responses
- [object ReturnToServiceRequest](returntoservicerequest.md)
  The return-to-service request details.
- [object ReturnToServiceResponse](returntoserviceresponse.md)
  The return-to-service response details.

## Request Body

The request object the system sends for the `ReturnToService` request.

## See Also

- [Authenticate](authenticate.md)
  Authenticates a user during MDM payload installation.
- [User Authenticate](user-authenticate.md)
  Authenticates a user with a two-step authentication protocol.
- [Check Out](check-out.md)
  Responds to the removal of the MDM enrollment profile from a device.
- [Get Token](get-token.md)
  Gets a token from the server.
- [Token Update](token-update.md)
  Updates the token for a device on the server.
- [Get Bootstrap Token](get-bootstrap-token.md)
  Gets the bootstrap token from the server.
- [Set Bootstrap Token](set-bootstrap-token.md)
  Sends the bootstrap token to the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/return-to-service)*