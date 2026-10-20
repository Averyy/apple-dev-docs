# Delete subscription prices

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a scheduled price change for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/subscriptionPrices/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Read subscription price point information](get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List all subscription price point equalizations](get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [List equalization IDs for a subscription price point](get-v1-subscriptionpricepoints-_id_-relationships-equalizations.md)
- [List adjusted equalizations for a subscription price point](get-v1-subscriptionpricepoints-_id_-adjustedequalizations.md)
  List the adjusted territory equalizations for a subscription price point.
- [Create a subscription price change](post-v1-subscriptionprices.md)
  Schedule a subscription price change for a specific territory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-subscriptionprices-_id_)*