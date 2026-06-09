# Create a subscription price change

**Framework**: App Store Connect API  
**Kind**: httpRequest

Schedule a subscription price change for a specific territory.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)

#### Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/subscriptionPrices`

## See Also

- [Read subscription price point information](get-v1-subscriptionpricepoints-_id_.md)
  Get details about a specific subscription price point.
- [List all subscription price point equalizations](get-v1-subscriptionpricepoints-_id_-equalizations.md)
  Get a list of subscription price points and their equivalent in a specified currency.
- [List equalization IDs for a subscription price point](get-v1-subscriptionpricepoints-_id_-relationships-equalizations.md)
- [Delete subscription prices](delete-v1-subscriptionprices-_id_.md)
  Delete a scheduled price change for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-subscriptionprices)*