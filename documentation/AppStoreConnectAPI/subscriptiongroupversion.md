# SubscriptionGroupVersion

**Framework**: App Store Connect API  
**Kind**: dictionary

A draft version of a subscription group that captures its localized metadata for App Review submission.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionGroupVersion
```

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)

## Topics

### Objects and types
- [object SubscriptionGroupVersion.Attributes](subscriptiongroupversion/attributes-data.dictionary.md)
  Attributes that describe a subscription group version resource.
- [object SubscriptionGroupVersion.Relationships](subscriptiongroupversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (SubscriptionGroupVersion.Attributes)
- `relationships` (SubscriptionGroupVersion.Relationships)
- `links` (ResourceLinks)

## See Also

- [object SubscriptionGroupVersionCreateRequest](subscriptiongroupversioncreaterequest.md)
  The request body you use to create a draft version of a subscription group.
- [object SubscriptionGroupVersionLocalizationsLinkagesResponse](subscriptiongroupversionlocalizationslinkagesresponse.md)
  A response with the related resource identifiers for a subscription group version’s localizations.
- [object SubscriptionGroupVersionResponse](subscriptiongroupversionresponse.md)
  The response body for endpoints that create or read a subscription group version.
- [object SubscriptionGroupVersionsLinkagesResponse](subscriptiongroupversionslinkagesresponse.md)
  A response with the related resource identifiers for the versions of a subscription group.
- [object SubscriptionGroupVersionsResponse](subscriptiongroupversionsresponse.md)
  The response body for endpoints that list subscription group versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupversion)*