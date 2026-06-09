# List equalization IDs for a subscription price point

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionPricePoints/{id}/relationships/equalizations`

## Parameters

- `limit` (integer)

## See Also

- [Read subscription price point information](get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List all subscription price point equalizations](get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [Create a subscription price change](post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.
- [Delete subscription prices](delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionpricepoints-_id_-relationships-equalizations)*