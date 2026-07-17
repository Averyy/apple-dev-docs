# SubscriptionVersionsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list subscription versions.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionVersionsResponse
```

## Properties

- `data` ([SubscriptionVersion]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object SubscriptionVersion](subscriptionversion.md)
  A draft version of an auto-renewable subscription that captures its localized metadata and review images for App Review submission.
- [object SubscriptionVersionCreateRequest](subscriptionversioncreaterequest.md)
  The request body you use to create a draft version of an auto-renewable subscription.
- [object SubscriptionVersionImageLinkageResponse](subscriptionversionimagelinkageresponse.md)
  A response with the related resource identifier for a subscription version’s image.
- [object SubscriptionVersionImagesLinkagesResponse](subscriptionversionimageslinkagesresponse.md)
  A response with the related resource identifiers for a subscription version’s images.
- [object SubscriptionVersionLocalizationsLinkagesResponse](subscriptionversionlocalizationslinkagesresponse.md)
  A response with the related resource identifiers for a subscription version’s localizations.
- [object SubscriptionVersionResponse](subscriptionversionresponse.md)
  The response body for endpoints that create or read a subscription version.
- [object SubscriptionVersionsLinkagesResponse](subscriptionversionslinkagesresponse.md)
  A response with the related resource identifiers for the versions of an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionversionsresponse)*