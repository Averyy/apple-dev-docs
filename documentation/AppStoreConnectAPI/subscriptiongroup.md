# SubscriptionGroup

**Framework**: App Store Connect API  
**Kind**: dictionary

A group of related auto-renewable subscriptions that share upgrade, downgrade, and cross-grade eligibility for customers.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionGroup
```

## Topics

### Objects
- [object SubscriptionGroup.Attributes](subscriptiongroup/attributes-data.dictionary.md)
  Attributes that describe a subscription group resource.
- [object SubscriptionGroup.Relationships](subscriptiongroup/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionGroup.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionGroup.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionGroupResponse](subscriptiongroupresponse.md)
  The response body for endpoints that create, read, or modify a single subscription group.
- [object SubscriptionGroupLocalizationsResponse](subscriptiongrouplocalizationsresponse.md)
  The response body for endpoints that list localizations for a subscription group.
- [object SubscriptionGroupLocalization](subscriptiongrouplocalization.md)
  The localized display name and optional custom app name for a subscription group, shown to customers on the App Store.
- [object SubscriptionGroupCreateRequest](subscriptiongroupcreaterequest.md)
  The request body you use to create a subscription group.
- [object SubscriptionGroupUpdateRequest](subscriptiongroupupdaterequest.md)
  The request body you use to update a subscription group update request.
- [object SubscriptionGroupsResponse](subscriptiongroupsresponse.md)
  The response body for endpoints that list subscription groups for an app.
- [object AppSubscriptionGroupsLinkagesResponse](appsubscriptiongroupslinkagesresponse.md)
- [object SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse](subscriptiongroupsubscriptiongrouplocalizationslinkagesresponse.md)
- [object SubscriptionGroupSubscriptionsLinkagesResponse](subscriptiongroupsubscriptionslinkagesresponse.md)
  A response containing the resource identifiers of subscriptions within a subscription group.
- [object SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse](subscriptiongroupsubscriptiongrouplocalizationslinkagesresponse.md)
- [object SubscriptionGroupSubscriptionsLinkagesResponse](subscriptiongroupsubscriptionslinkagesresponse.md)
  A response containing the resource identifiers of subscriptions within a subscription group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroup)*