# List all subscription price point equalizations

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of subscription price points and their equivalent in a specified currency.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
- [Querying adjusted subscription price equalizations](querying-adjusted-subscription-price-equalizations.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/{id}/equalizations`

## Parameters

- `filter[territory]` ([string]): Filter the returned subscription price points by territory.
- `filter[subscription]` ([string]): Filter the returned subscription price points by subscription.
- `filter[upfrontPricePointId]` ([string]): Filter the returned subscription price points by upfront price point ID.
- `filter[planType]` ([string]): Filter the returned subscription price points by plan type.
- `fields[subscriptionPricePoints]` ([string]): Additional fields to include for each subscription price point resource returned by the response.
- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response.
- `limit` (integer): The maximum number of subscription price point resources to return.
- `include` ([string]): The relationship data to include in the response.

## See Also

- [Read subscription price point information](get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List equalization IDs for a subscription price point](get-v1-subscriptionpricepoints-_id_-relationships-equalizations.md)
- [List adjusted equalizations for a subscription price point](get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)
  List the adjusted territory equalizations for a subscription price point.
- [Create a subscription price change](post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.
- [Delete subscription prices](delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionpricepoints-_id_-equalizations)*