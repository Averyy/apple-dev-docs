# Delete an introductory offer from a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a specific introductory offer for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/relationships/introductoryOffers`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionIntroductoryOffersLinkagesRequest`

## Responses

- `204` No Content
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting introductory offers
- [List all introductory offers for a subscription](./get-v1-subscriptions-_id_-introductoryoffers.md)
  Get a list of introductory offers for a specific auto-renewable subscription.
- [List all introductory offer resource ids for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Get a list of resource IDs representing introductory offers for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptions-_id_-relationships-introductoryoffers)*