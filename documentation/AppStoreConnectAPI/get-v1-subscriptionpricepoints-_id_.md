# Read subscription price point information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific subscription price point.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionPricePoints]` ([string]): **Allowed Values**: `customerPrice`, `proceeds`, `proceedsYear2`, `territory`, `equalizations`, `adjustedEqualizations`
- `include` ([string]): **Allowed Values**: `territory`
- `fields[territories]` ([string]): **Allowed Values**: `currency`

## Responses

- `200` OK (`SubscriptionPricePointResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and managing subscription price points and prices
- [List all subscription price point equalizations](./get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [List equalization IDs for a subscription price point](./get-v1-subscriptionpricepoints-_id_-relationships-equalizations.md)
- [List adjusted equalizations for a subscription price point](./get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)
  List the adjusted territory equalizations for a subscription price point.
- [Create a subscription price change](./post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.
- [Delete subscription prices](./delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionpricepoints-_id_)*