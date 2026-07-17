# Delete an introductory offer from a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific introductory offer for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/introductoryOffers`

## Parameters

- `id` (string) *(required)*

## See Also

- [List all introductory offers for a subscription](get-v1-subscriptions-_id_-introductoryoffers.md)
  Get a list of introductory offers for a specific auto-renewable subscription.
- [List all introductory offer resource ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Get a list of resource IDs representing introductory offers for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptions-_id_-relationships-introductoryoffers)*