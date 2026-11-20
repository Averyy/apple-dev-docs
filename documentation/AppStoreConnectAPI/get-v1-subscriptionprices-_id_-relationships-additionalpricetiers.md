# List additional price tier IDs for a subscription price

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the IDs of the additional volume pricing tiers for a subscription price.

**Availability**:
- App Store Connect API 4.6.1+

## Mentions

- [App Store Connect API 4.6.1 release notes](./app-store-connect-api-4-6-1-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPrices/{id}/relationships/additionalPriceTiers`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPrice` resource ID from the `GET-v1-subscriptions-_id_-prices` response.

### Query Parameters

- `limit` (integer): The maximum number of additional price tier resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionPriceAdditionalPriceTiersLinkagesResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting price tiers
- [List subscription price tiers](./get-v1-subscriptionpricetiers.md)
  List the volume pricing tiers for a subscription’s prices.
- [List additional price tiers for a subscription price](./get-v1-subscriptionprices-_id_-additionalpricetiers.md)
  List the additional volume pricing tiers for a subscription price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionprices-_id_-relationships-additionalpricetiers)*