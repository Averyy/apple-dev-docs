# List subscription price tiers

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List the volume pricing tiers for a subscription’s prices.

**Availability**:
- App Store Connect API 4.6.1+

## Mentions

- [App Store Connect API 4.6.1 release notes](./app-store-connect-api-4-6-1-release-notes.md)
- [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPriceTiers`

## Parameters

### Query Parameters

- `filter[subscription]` ([string]) *(required)*: Filter the returned price tiers by subscription.
- `filter[territory]` ([string]): Filter the returned price tiers by territory. Tiers don’t identify their territory, so use this filter to know which territory the results belong to.
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
- `429` (`ErrorResponse`, `application/json`): The request rate limit was exceeded.

## See Also

### Getting price tiers
- [List additional price tiers for a subscription price](./get-v1-subscriptionprices-_id_-additionalpricetiers.md)
  List the additional volume pricing tiers for a subscription price.
- [List additional price tier IDs for a subscription price](./get-v1-subscriptionprices-_id_-relationships-additionalpricetiers.md)
  List the IDs of the additional volume pricing tiers for a subscription price.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionpricetiers)*