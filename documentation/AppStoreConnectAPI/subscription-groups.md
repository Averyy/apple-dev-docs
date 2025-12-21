# Subscription Groups

**Framework**: App Store Connect API

Create, modify, and delete subscription groups for your app.

## Topics

### Endpoints
- [Create a Subscription Group](post-v1-subscriptiongroups.md)
  Create a subscription group for an app.
- [List All Subscription Groups for an App](get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [GET /v1/apps/{id}/relationships/subscriptionGroups](get-v1-apps-_id_-relationships-subscriptiongroups.md)
- [Read Subscription Group Information](get-v1-subscriptiongroups-_id_.md)
  Get the details of a specific subscription group.
- [Modify a Subscription Group](patch-v1-subscriptiongroups-_id_.md)
  Update the reference name for a specific subscription group.
- [Delete a Subscription Group](delete-v1-subscriptiongroups-_id_.md)
  Delete a specific empty subscription group.
- [List All Subscription Group Localizations](get-v1-subscriptiongroups-_id_-subscriptiongrouplocalizations.md)
  Get a list of all localized metadata for a specific subscription group.
- [GET /v1/subscriptionGroups/{id}/relationships/subscriptionGroupLocalizations](get-v1-subscriptiongroups-_id_-relationships-subscriptiongrouplocalizations.md)
- [List All Subscriptions for a Subscription Group](get-v1-subscriptiongroups-_id_-subscriptions.md)
  Get a list of all auto-renewable subscriptions in a subscription group.
- [GET /v1/subscriptionGroups/{id}/relationships/subscriptions](get-v1-subscriptiongroups-_id_-relationships-subscriptions.md)
### Objects
- [object SubscriptionGroupResponse](subscriptiongroupresponse.md)
- [object SubscriptionGroup](subscriptiongroup.md)
- [object SubscriptionGroupLocalizationsResponse](subscriptiongrouplocalizationsresponse.md)
- [object SubscriptionGroupLocalization](subscriptiongrouplocalization.md)
- [object SubscriptionGroupCreateRequest](subscriptiongroupcreaterequest.md)
- [object SubscriptionGroupUpdateRequest](subscriptiongroupupdaterequest.md)
- [object SubscriptionGroupsResponse](subscriptiongroupsresponse.md)
- [object AppSubscriptionGroupsLinkagesResponse](appsubscriptiongroupslinkagesresponse.md)
- [object SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse](subscriptiongroupsubscriptiongrouplocalizationslinkagesresponse.md)
- [object SubscriptionGroupSubscriptionsLinkagesResponse](subscriptiongroupsubscriptionslinkagesresponse.md)
  A response that contains a list of IDs of related resources.
- [object SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse](subscriptiongroupsubscriptiongrouplocalizationslinkagesresponse.md)
- [object SubscriptionGroupSubscriptionsLinkagesResponse](subscriptiongroupsubscriptionslinkagesresponse.md)
  A response that contains a list of IDs of related resources.

## See Also

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)
  Configure subscription groups with the App Store Connect API.
- [Subscription Group Localizations](subscription-group-localizations.md)
  Create, modify, and delete localized metadata for subscription groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-groups)*