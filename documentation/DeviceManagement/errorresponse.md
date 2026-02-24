# ErrorResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains the error that occurs.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ErrorResponse
```

## Mentions

- [Handling Error Responses](handling-error-responses.md)

## Topics

### Objects and Data Types
- [object ResponseErrorInfo](responseerrorinfo.md)
  Information about the error.

## Properties

- `errorInfo` (ResponseErrorInfo): The request-specific information regarding the failure.
- `errorMessage` (string): The human-readable error message that describes the failure.
- `errorNumber` (int32): The error number that represents the failure.

## See Also

- [object ManageAssetsRequest](manageassetsrequest.md)
  The request for asset management.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorresponse)*