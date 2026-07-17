# SubscriptionVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

A draft version of an auto-renewable subscription that captures its localized metadata and review images for App Review submission.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionVersion
```

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)

## Topics

### Objects and types
- [object SubscriptionVersion.Attributes](subscriptionversion/attributes-data.dictionary.md)
  Attributes that describe a SubscriptionVersion resource.
- [object SubscriptionVersion.Relationships](subscriptionversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (SubscriptionVersion.Attributes)
- `relationships` (SubscriptionVersion.Relationships)
- `links` (ResourceLinks)

## See Also

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
- [object SubscriptionVersionsResponse](subscriptionversionsresponse.md)
  The response body for endpoints that list subscription versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionversion)*