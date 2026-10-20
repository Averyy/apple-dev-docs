# List all offer codes for a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of subscription offer codes for a specific auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/offerCodes`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionOfferCodeCustomCodes]` ([string]): **Allowed Values**: `customCode`, `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `offerCode`
- `fields[subscriptionOfferCodeOneTimeUseCodes]` ([string]): **Allowed Values**: `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `environment`, `offerCode`, `values`
- `fields[subscriptionOfferCodePrices]` ([string]): **Allowed Values**: `territory`, `subscriptionPricePoint`
- `fields[subscriptionOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `offerEligibility`, `duration`, `offerMode`, `numberOfPeriods`, `totalNumberOfCodes`, `productionCodeCount`, `sandboxCodeCount`, `active`, `autoRenewEnabled`, `targetSubscriptionPlanType`, `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `fields[subscriptions]` ([string]): **Allowed Values**: `name`, `productId`, `familySharable`, `state`, `subscriptionPeriod`, `reviewNote`, `groupLevel`, `multiSeatStatus`, `marketSettings`, `subscriptionLocalizations`, `appStoreReviewScreenshot`, `group`, `introductoryOffers`, `promotionalOffers`, `offerCodes`, `prices`, `pricePoints`, `promotedPurchase`, `subscriptionAvailability`, `winBackOffers`, `images`, `planAvailabilities`, `versions`
- `filter[territory]` ([string])
- `include` ([string]): **Allowed Values**: `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`
- `limit` (integer): **Maximum**: `200`
- `limit[customCodes]` (integer): **Maximum**: `50`
- `limit[oneTimeUseCodes]` (integer): **Maximum**: `50`
- `limit[prices]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`SubscriptionOfferCodesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting offer codes
- [List offer code IDs for an auto-renewable subscription](./get-v1-subscriptions-_id_-relationships-offercodes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-offercodes)*