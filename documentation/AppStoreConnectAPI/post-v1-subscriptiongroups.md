# Create a subscription group

**Framework**: App Store Connect API  
**Kind**: httpRequest

Create a subscription group for an app.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Creating auto-renewable subscription groups](creating-auto-renewable-subscription-groups.md)

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionGroups`

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptiongroups)*