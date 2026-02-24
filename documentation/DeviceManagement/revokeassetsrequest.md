# RevokeAssetsRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for asset revocation.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object RevokeAssetsRequest
```

## Mentions

- [Managing Assets](managing-assets.md)

## Properties

- `clientUserIds` ([string]): The set of identifiers for users in your organization.
- `serialNumbers` ([string]): The set of identifiers for devices in your organization.

## See Also

- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/revokeassetsrequest)*