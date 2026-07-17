# SubscriptionGroupLocalizationV2Response

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a subscription group localization with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionGroupLocalizationV2Response
```

## Properties

- `data` (SubscriptionGroupLocalizationV2) *(required)*
- `included` ([SubscriptionGroupVersion])
- `links` (DocumentLinks) *(required)*

## See Also

- [object SubscriptionGroupLocalizationV2](subscriptiongrouplocalizationv2.md)
  The localized custom name for a subscription group configured with the v2 API, shown to customers in a specific language.
- [object SubscriptionGroupLocalizationV2CreateRequest](subscriptiongrouplocalizationv2createrequest.md)
  The request body you use to create a subscription group localization with the v2 API.
- [object SubscriptionGroupLocalizationV2UpdateRequest](subscriptiongrouplocalizationv2updaterequest.md)
  The request body you use to modify a subscription group localization.
- [object SubscriptionGroupLocalizationsV2Response](subscriptiongrouplocalizationsv2response.md)
  The response body for endpoints that list subscription group localizations configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongrouplocalizationv2response)*