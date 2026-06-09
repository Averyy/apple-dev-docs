# SubscriptionGroupSubscriptionsLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the resource identifiers of subscriptions within a subscription group.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object SubscriptionGroupSubscriptionsLinkagesResponse
```

## Topics

### Dictionaries
- [object SubscriptionGroupSubscriptionsLinkagesResponse.Data](subscriptiongroupsubscriptionslinkagesresponse/data-data.dictionary.md)
  The resource linkage data identifying a subscription within a subscription group.

## Properties

- `data` ([SubscriptionGroupSubscriptionsLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

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
- [object SubscriptionGroupSubscriptionGroupLocalizationsLinkagesResponse](subscriptiongroupsubscriptiongrouplocalizationslinkagesresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupsubscriptionslinkagesresponse)*