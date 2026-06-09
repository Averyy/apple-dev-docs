# Modify an introductory offer

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update a specific introductory offer for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionIntroductoryOffers/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create an introductory offer](post-v1-subscriptionintroductoryoffers.md)
  Create an introductory offer for an auto-renewable subscription.
- [Delete an introductory offer for a subscription](delete-v1-subscriptionintroductoryoffers-_id_.md)
  Delete a specific introductory offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionintroductoryoffers-_id_)*