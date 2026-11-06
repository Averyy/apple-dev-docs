# Modify a retention offer

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the customer eligibility rules of a specific retention offer.

**Availability**:
- App Store Connect API 4.6+

## Mentions

- [Setting up retention messaging for auto-renewable subscriptions](./setting-up-retention-messaging.md)

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/retentionOffers/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the retention offer resource ID from the [`List retention offers for a subscription`](./get-v1-subscriptions-_id_-retentionoffers.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `RetentionOfferUpdateRequest`

The request body you use to modify a retention offer.

## Responses

- `200` OK (`RetentionOfferResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`): The request data is not valid.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Managing retention offers
- [Create a retention offer](./post-v1-retentionoffers.md)
  Create a retention offer for an auto-renewable subscription.
- [Delete a retention offer](./delete-v1-retentionoffers-_id_.md)
  Delete a specific retention offer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-retentionoffers-_id_)*