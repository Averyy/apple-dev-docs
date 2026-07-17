# SubscriptionVersionImageLinkageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response with the related resource identifier for a subscription version’s image.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionVersionImageLinkageResponse
```

## Topics

### Objects and types
- [object SubscriptionVersionImageLinkageResponse.Data](subscriptionversionimagelinkageresponse/data-data.dictionary.md)
  The resource linkage data identifying the related resource.

## Properties

- `data` (SubscriptionVersionImageLinkageResponse.Data) *(required)*
- `links` (DocumentLinks) *(required)*

## See Also

- [object SubscriptionVersion](subscriptionversion.md)
  A draft version of an auto-renewable subscription that captures its localized metadata and review images for App Review submission.
- [object SubscriptionVersionCreateRequest](subscriptionversioncreaterequest.md)
  The request body you use to create a draft version of an auto-renewable subscription.
- [object SubscriptionVersionImagesLinkagesResponse](subscriptionversionimageslinkagesresponse.md)
  A response with the related resource identifiers for a subscription version’s images.
- [object SubscriptionVersionLocalizationsLinkagesResponse](subscriptionversionlocalizationslinkagesresponse.md)
  A response with the related resource identifiers for a subscription version’s localizations.
- [object SubscriptionVersionResponse](subscriptionversionresponse.md)
  The response body for endpoints that create or read a subscription version.
- [object SubscriptionVersionsLinkagesResponse](subscriptionversionslinkagesresponse.md)
  A response with the related resource identifiers for the versions of an auto-renewable subscription.
- [object SubscriptionVersionsResponse](subscriptionversionsresponse.md)
  The response body for endpoints that list subscription versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionversionimagelinkageresponse)*