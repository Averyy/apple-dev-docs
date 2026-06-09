# Subscription Groups

**Framework**: App Store Connect API

Create, modify, and delete subscription groups for your app.

## Topics

### Endpoints
- [Create a subscription group](post-v1-subscriptiongroups.md)
  Create a subscription group for an app.
- [List all subscription groups for an app](get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [List subscription group IDs for an app](get-v1-apps-_id_-relationships-subscriptiongroups.md)
- [Read subscription group information](get-v1-subscriptiongroups-_id_.md)
  Get the details of a specific subscription group.
- [Modify a subscription group](patch-v1-subscriptiongroups-_id_.md)
  Update the reference name for a specific subscription group.
- [Delete a subscription group](delete-v1-subscriptiongroups-_id_.md)
  Delete a specific empty subscription group.
- [List all subscription group localizations](get-v1-subscriptiongroups-_id_-subscriptiongrouplocalizations.md)
  Get a list of all localized metadata for a specific subscription group.
- [List localization IDs for a subscription group](get-v1-subscriptiongroups-_id_-relationships-subscriptiongrouplocalizations.md)
- [List all subscriptions for a subscription group](get-v1-subscriptiongroups-_id_-subscriptions.md)
  Get a list of all auto-renewable subscriptions in a subscription group.
- [List subscription IDs for a subscription group](get-v1-subscriptiongroups-_id_-relationships-subscriptions.md)
### Objects
- [object SubscriptionGroupResponse](subscriptiongroupresponse.md)
  The response body for endpoints that create, read, or modify a single subscription group.
- [object SubscriptionGroup](subscriptiongroup.md)
  A group of related auto-renewable subscriptions that share upgrade, downgrade, and cross-grade eligibility for customers.
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

## See Also

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)
  Configure subscription groups with the App Store Connect API.
- [Subscription Group Localizations](subscription-group-localizations.md)
  Create, modify, and delete localized metadata for subscription groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-groups)*