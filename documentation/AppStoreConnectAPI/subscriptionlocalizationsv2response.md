# SubscriptionLocalizationsV2Response

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list subscription localizations configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object SubscriptionLocalizationsV2Response
```

## Properties

- `data` ([SubscriptionLocalizationV2]) *(required)*
- `included` ([SubscriptionVersion])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object SubscriptionLocalizationV2](subscriptionlocalizationv2.md)
  The localized display name and description for an auto-renewable subscription configured with the v2 API, shown to customers in a specific language.
- [object SubscriptionLocalizationV2CreateRequest](subscriptionlocalizationv2createrequest.md)
  The request body you use to create a subscription localization with the v2 API.
- [object SubscriptionLocalizationV2Response](subscriptionlocalizationv2response.md)
  The response body for endpoints that create, read, or modify a subscription localization with the v2 API.
- [object SubscriptionLocalizationV2UpdateRequest](subscriptionlocalizationv2updaterequest.md)
  The request body you use to update a subscription localization with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionlocalizationsv2response)*