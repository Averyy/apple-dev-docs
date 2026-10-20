# Modify an introductory offer

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific introductory offer for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionIntroductoryOffers/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `SubscriptionIntroductoryOfferUpdateRequest`

## Responses

- `200` OK (`SubscriptionIntroductoryOfferResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Create an introductory offer](./post-v1-subscriptionintroductoryoffers.md)
  Create an introductory offer for an auto-renewable subscription.
- [Delete an introductory offer for a subscription](./delete-v1-subscriptionintroductoryoffers-_id_.md)
  Delete a specific introductory offer for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionintroductoryoffers-_id_)*