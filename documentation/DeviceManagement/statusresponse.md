# StatusResponse

**Framework**: Device Management  
**Kind**: dictionary

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object StatusResponse
```

## Mentions

- [Handling Error Responses](handling-error-responses.md)
- [Managing Assets](managing-assets.md)
- [Managing Users](managing-users.md)

## Properties

- `eventStatus` (string)
- `eventType` (string)
- `failures` ([ErrorResponse])
- `mdmInfo` (MdmInfo)
- `numCompleted` (int32)
- `numRequested` (int32)
- `tokenExpirationDate` (string)
- `uId` (string)

## See Also

- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusresponse)*