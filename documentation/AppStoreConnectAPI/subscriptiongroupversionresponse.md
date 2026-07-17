# SubscriptionGroupVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create or read a subscription group version.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionGroupVersionResponse
```

## Properties

- `data` (SubscriptionGroupVersion) *(required)*
- `included` ([*])
- `links` (DocumentLinks) *(required)*

## See Also

- [object SubscriptionGroupVersion](subscriptiongroupversion.md)
  A draft version of a subscription group that captures its localized metadata for App Review submission.
- [object SubscriptionGroupVersionCreateRequest](subscriptiongroupversioncreaterequest.md)
  The request body you use to create a draft version of a subscription group.
- [object SubscriptionGroupVersionLocalizationsLinkagesResponse](subscriptiongroupversionlocalizationslinkagesresponse.md)
  A response with the related resource identifiers for a subscription group version’s localizations.
- [object SubscriptionGroupVersionsLinkagesResponse](subscriptiongroupversionslinkagesresponse.md)
  A response with the related resource identifiers for the versions of a subscription group.
- [object SubscriptionGroupVersionsResponse](subscriptiongroupversionsresponse.md)
  The response body for endpoints that list subscription group versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupversionresponse)*