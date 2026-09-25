# InAppPurchaseAvailability

**Framework**: App Store Connect API  
**Kind**: dictionary

The territory availability configuration for an In-App Purchase, specifying which App Store regions it’s offered in.

**Availability**:
- App Store Connect API 2.3+

## Declaration

```swift
object InAppPurchaseAvailability
```

## Topics

### Objects
- [object InAppPurchaseAvailability.Attributes](inapppurchaseavailability/attributes-data.dictionary.md)
  Attributes that describe an In-App Purchase availability resource.
- [object InAppPurchaseAvailability.Relationships](inapppurchaseavailability/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (InAppPurchaseAvailability.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchaseAvailability.Relationships)
- `type` (string) *(required)*

## See Also

- [object InAppPurchaseAvailabilityCreateRequest](inapppurchaseavailabilitycreaterequest.md)
  The request body you use to create an In-App Purchase availability.
- [object InAppPurchaseAvailabilityResponse](inapppurchaseavailabilityresponse.md)
  A response containing a single territory availability configuration for an In-App Purchase.
- [object InAppPurchaseAvailabilityAvailableTerritoriesLinkagesResponse](inapppurchaseavailabilityavailableterritorieslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaseavailability)*