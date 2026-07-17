# SubscriptionLocalizationV2

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized display name and description for an auto-renewable subscription configured with the v2 API, shown to customers in a specific language.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionLocalizationV2
```

## Topics

### Objects and types
- [object SubscriptionLocalizationV2.Attributes](subscriptionlocalizationv2/attributes-data.dictionary.md)
  Attributes that describe a SubscriptionLocalizationV2 resource.
- [object SubscriptionLocalizationV2.Relationships](subscriptionlocalizationv2/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (SubscriptionLocalizationV2.Attributes)
- `relationships` (SubscriptionLocalizationV2.Relationships)
- `links` (ResourceLinks)

## See Also

- [object SubscriptionLocalizationV2CreateRequest](subscriptionlocalizationv2createrequest.md)
  The request body you use to create a subscription localization with the v2 API.
- [object SubscriptionLocalizationV2Response](subscriptionlocalizationv2response.md)
  The response body for endpoints that create, read, or modify a subscription localization with the v2 API.
- [object SubscriptionLocalizationV2UpdateRequest](subscriptionlocalizationv2updaterequest.md)
  The request body you use to update a subscription localization with the v2 API.
- [object SubscriptionLocalizationsV2Response](subscriptionlocalizationsv2response.md)
  The response body for endpoints that list subscription localizations configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionlocalizationv2)*