# Read custom offer code information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get details about a specific offer code for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodeCustomCodes/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionOfferCodeCustomCodes]` ([string]): **Allowed Values**: `customCode`, `numberOfCodes`, `createdDate`, `expirationDate`, `active`, `offerCode`
- `include` ([string]): **Allowed Values**: `offerCode`
- `fields[subscriptionOfferCodes]` ([string]): **Allowed Values**: `name`, `customerEligibilities`, `offerEligibility`, `duration`, `offerMode`, `numberOfPeriods`, `totalNumberOfCodes`, `productionCodeCount`, `sandboxCodeCount`, `active`, `autoRenewEnabled`, `targetSubscriptionPlanType`, `subscription`, `oneTimeUseCodes`, `customCodes`, `prices`

## Responses

- `200` OK (`SubscriptionOfferCodeCustomCodeResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing Custom Offer Codes
- [Create custom offer codes](./post-v1-subscriptionoffercodecustomcodes.md)
  Create custom offer codes for an auto-renewable subscription offer.
- [List all custom offer codes for an auto-renewable subscription](./get-v1-subscriptionoffercodes-_id_-customcodes.md)
  Get details about a custom code for a specific subscription offer for an auto-renewable subscription.
- [List custom code IDs for a subscription offer code](./get-v1-subscriptionoffercodes-_id_-relationships-customcodes.md)
- [Deactivate custom offer codes](./patch-v1-subscriptionoffercodecustomcodes-_id_.md)
  Deactivate a batch of custom offer codes for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodecustomcodes-_id_)*