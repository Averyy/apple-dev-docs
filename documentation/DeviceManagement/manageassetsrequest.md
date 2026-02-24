# ManageAssetsRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for asset management.

**Availability**:
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object ManageAssetsRequest
```

## Mentions

- [Managing Assets](managing-assets.md)

## Topics

### Objects and Data Types
- [object Asset](asset.md)
  A product in the store.

## Properties

- `assets` ([Asset]) *(required)*: The set of `adamId` and `pricingParam values`.
- `clientUserIds` ([string]): The set of identifiers for users in your organization.
- `serialNumbers` ([string]): The set of identifiers for devices in your organization.

## See Also

- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/manageassetsrequest)*