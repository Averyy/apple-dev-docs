# List additional price tiers for a subscription price

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the additional volume pricing tiers for a subscription price.

**Availability**:
- App Store Connect API 4.6.1+

## Mentions

- [App Store Connect API 4.6.1 release notes](./app-store-connect-api-4-6-1-release-notes.md)
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)
- [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPrices/{id}/additionalPriceTiers`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionPrice` resource ID from the `GET-v1-subscriptions-_id_-prices` response.

### Query Parameters

- `filter[subscription]` ([string]): Filter the returned subscription price tiers by subscription.
- `filter[territory]` ([string]): Filter the returned subscription price tiers by territory.
- `fields[subscriptionPriceTiers]` ([string]): Additional fields to include for each subscription price tier resource that the response returns.

  **Allowed Values**: `minQuantity`, `subscriptionPricePoint`
- `fields[subscriptionPricePoints]` ([string]): Additional fields to include for each subscription price point resource that the response returns.

  **Allowed Values**: `customerPrice`, `proceeds`, `proceedsYear2`, `territory`, `equalizations`, `adjustedEqualizations`
- `limit` (integer): The maximum number of subscription price tier resources to return.

  **Maximum**: `200`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `subscriptionPricePoint`

## Responses

- `200` OK (`SubscriptionPriceTiersResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting price tiers
- [List subscription price tiers](./get-v1-subscriptionpricetiers.md)
  List the volume pricing tiers for a subscription’s prices.
- [List additional price tier IDs for a subscription price](./get-v1-subscriptionprices-_id_-relationships-additionalpricetiers.md)
  List the IDs of the additional volume pricing tiers for a subscription price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionprices-_id_-additionalpricetiers)*