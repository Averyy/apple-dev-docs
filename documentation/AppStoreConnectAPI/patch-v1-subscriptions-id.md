# Modify an auto-renewable subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptions/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create an auto-renewable subscription](post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Read subscription information](get-v1-subscriptions-_id_.md)
  Get information about a specific auto-renewable subscription.
- [Delete a subscription](delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptions-_id_)*