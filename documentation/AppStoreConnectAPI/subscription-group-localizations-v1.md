# Subscription group localizations (v1)

**Framework**: App Store Connect API

Create, modify, and delete localized metadata for subscription groups.

**Availability**:
- App Store Connect API 2.0+

#### Overview

> ❗ **Important**:  This is deprecated. Use [`Subscription Group Localizations`](subscription-group-localizations.md) instead.

## Topics

### Endpoints
- [Create a subscription group localization (v1)](post-v1-subscriptiongrouplocalizations.md)
  Create a localized display name and optional custom app name for a subscription group.
- [Read subscription group localization information (v1)](get-v1-subscriptiongrouplocalizations-_id_.md)
  Get the specific localized subscription group display name and optional custom app name for a subscription group.
- [Modify a subscription group localization (v1)](patch-v1-subscriptiongrouplocalizations-_id_.md)
  Update a specific localized display name and optional custom app name for a subscription group.
- [Delete a subscription group localization (v1)](delete-v1-subscriptiongrouplocalizations-_id_.md)
  Delete localized metadata that you configured for a subscription group.
### Objects
- [object SubscriptionGroupLocalization](subscriptiongrouplocalization.md)
  The localized display name and optional custom app name for a subscription group, shown to customers on the App Store.
- [object SubscriptionGroupLocalizationResponse](subscriptiongrouplocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single subscription group localization.
- [object SubscriptionGroupLocalizationCreateRequest](subscriptiongrouplocalizationcreaterequest.md)
  The request body you use to create a subscription group localization.
- [object SubscriptionGroupLocalizationUpdateRequest](subscriptiongrouplocalizationupdaterequest.md)
  The request body you use to update a subscription group localization update request.

## See Also

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)
  Configure subscription groups with the App Store Connect API.
- [Working with subscription group versions](working-with-subscription-group-versions.md)
  Manage draft versions of a subscription group’s localized metadata before submitting for App Review.
- [Subscription Group Versions](subscription-group-versions.md)
  Create and read draft versions of a subscription group with their localized metadata.
- [Subscription Groups](subscription-groups.md)
  Create, modify, and delete subscription groups for your app.
- [Subscription Group Localizations](subscription-group-localizations.md)
  Create, modify, and delete localized metadata for subscription groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-group-localizations-v1)*