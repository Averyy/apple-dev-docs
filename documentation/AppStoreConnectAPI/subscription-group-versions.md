# Subscription Group Versions

**Framework**: App Store Connect API

Create and read draft versions of a subscription group with their localized metadata.

## Topics

### Endpoints
- [Create a subscription group version](post-v1-subscriptiongroupversions.md)
  Create a draft version of a subscription group, capturing its current localized metadata for App Review submission.
- [Read subscription group version information](get-v1-subscriptiongroupversions-_id_.md)
  Get information about a specific draft version of a subscription group.
- [List the localizations of a subscription group version](get-v1-subscriptiongroupversions-_id_-localizations.md)
  List the localized custom names captured in a draft version of a subscription group.
- [Get the resource IDs of the localizations of a subscription group version](get-v1-subscriptiongroupversions-_id_-relationships-localizations.md)
  Get the related resource IDs for the localizations captured in a draft version of a subscription group.
- [List the versions of a subscription group](get-v1-subscriptiongroups-_id_-versions.md)
  List the draft versions of a subscription group.
- [Get the resource IDs of the versions of a subscription group](get-v1-subscriptiongroups-_id_-relationships-versions.md)
  Get the related resource IDs for the draft versions of a subscription group.
### Objects
- [object SubscriptionGroupVersion](subscriptiongroupversion.md)
  A draft version of a subscription group that captures its localized metadata for App Review submission.
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

## See Also

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)
  Configure subscription groups with the App Store Connect API.
- [Working with subscription group versions](working-with-subscription-group-versions.md)
  Manage draft versions of a subscription group’s localized metadata before submitting for App Review.
- [Subscription Groups](subscription-groups.md)
  Create, modify, and delete subscription groups for your app.
- [Subscription Group Localizations](subscription-group-localizations.md)
  Create, modify, and delete localized metadata for subscription groups.
- [Subscription group localizations (v1)](subscription-group-localizations-v1.md)
  Create, modify, and delete localized metadata for subscription groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-group-versions)*