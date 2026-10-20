# Read subscription offer code information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionOfferCodeCustomCodes]` ([string]): **Allowed Values**: `customCode`, `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `offerCode`
- `fields[subscriptionOfferCodeOneTimeUseCodes]` ([string]): **Allowed Values**: `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `environment`, `offerCode`, `values`
- `fields[subscriptionOfferCodePrices]` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `fields[subscriptionOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `offerEligibility`, `duration`, `offerMode`, `numberOfPeriods`, `totalNumberOfCodes`, `productionCodeCount`, `sandboxCodeCount`, `active`, `autoRenewEnabled`, `targetSubscriptionPlanType`, `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `include` ([string]): **Allowed Values**: `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `limit[customCodes]` (integer): **Maximum**: `50`
- `limit[oneTimeUseCodes]` (integer): **Maximum**: `50`
- `limit[prices]` (integer): **Maximum**: `50`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`

## Responses

- `200` OK (`SubscriptionOfferCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating and Managing Subscription Offers
- [Create a subscription offer](./post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Deactivate a subscription offer with offer codes](./patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List all subscription offer code prices](./get-v1-subscriptionoffercodes-_id_-prices.md)
  Get a list of price tiers for a subscription offer code.
- [List price IDs for a subscription offer code](./get-v1-subscriptionoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific subscription offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_)*