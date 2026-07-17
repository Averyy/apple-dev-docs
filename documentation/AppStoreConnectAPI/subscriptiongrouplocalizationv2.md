# SubscriptionGroupLocalizationV2

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized custom name for a subscription group configured with the v2 API, shown to customers in a specific language.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionGroupLocalizationV2
```

## Topics

### Objects and types
- [object SubscriptionGroupLocalizationV2.Attributes](subscriptiongrouplocalizationv2/attributes-data.dictionary.md)
  Attributes that describe a subscription group localization resource.
- [object SubscriptionGroupLocalizationV2.Relationships](subscriptiongrouplocalizationv2/relationships-data.dictionary.md)
  The relationship you include in the request and the one on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (SubscriptionGroupLocalizationV2.Attributes)
- `relationships` (SubscriptionGroupLocalizationV2.Relationships)
- `links` (ResourceLinks)

## See Also

- [object SubscriptionGroupLocalizationV2CreateRequest](subscriptiongrouplocalizationv2createrequest.md)
  The request body you use to create a subscription group localization with the v2 API.
- [object SubscriptionGroupLocalizationV2Response](subscriptiongrouplocalizationv2response.md)
  The response body for endpoints that create, read, or modify a subscription group localization with the v2 API.
- [object SubscriptionGroupLocalizationV2UpdateRequest](subscriptiongrouplocalizationv2updaterequest.md)
  The request body you use to modify a subscription group localization.
- [object SubscriptionGroupLocalizationsV2Response](subscriptiongrouplocalizationsv2response.md)
  The response body for endpoints that list subscription group localizations configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongrouplocalizationv2)*