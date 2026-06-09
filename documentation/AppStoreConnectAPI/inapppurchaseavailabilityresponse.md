# InAppPurchaseAvailabilityResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single territory availability configuration for an in-app purchase.

**Availability**:
- App Store Connect API 2.3+

## Declaration

```swift
object InAppPurchaseAvailabilityResponse
```

## Properties

- `data` (InAppPurchaseAvailability) *(required)*
- `included` ([Territory])
- `links` (DocumentLinks) *(required)*

## See Also

- [object InAppPurchaseAvailability](inapppurchaseavailability.md)
  The territory availability configuration for an in-app purchase, specifying which App Store regions it’s offered in.
- [object InAppPurchaseAvailabilityCreateRequest](inapppurchaseavailabilitycreaterequest.md)
  The request body you use to create an in-app purchase availability.
- [object InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse](inapppurchaseavailabilityavailableterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseavailabilityresponse)*