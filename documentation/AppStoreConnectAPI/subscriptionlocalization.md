# SubscriptionLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The localized display name and description for an auto-renewable subscription shown to customers on the App Store.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`SubscriptionLocalizationV2`](./subscriptionlocalizationv2.md) instead.

## Declaration

```
object SubscriptionLocalization
```

## Topics

### Objects
- [object SubscriptionLocalization.Attributes](./subscriptionlocalization/attributes-data.dictionary.md)
  Attributes that describe a subscription localization resource.
- [object SubscriptionLocalization.Relationships](./subscriptionlocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionLocalization.Relationships)
- `type` (string) *(required)*: **Allowed Values**: `subscriptionLocalizations`

## See Also

### Objects
- [object SubscriptionLocalizationCreateRequest](./subscriptionlocalizationcreaterequest.md)
  The request body you use to create a subscription localization.
- [object SubscriptionLocalizationUpdateRequest](./subscriptionlocalizationupdaterequest.md)
  The request body you use to update a subscription localization update request.
- [object SubscriptionLocalizationResponse](./subscriptionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single subscription localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionlocalization)*