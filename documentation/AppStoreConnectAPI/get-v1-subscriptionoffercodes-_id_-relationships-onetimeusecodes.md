# List one-time use code IDs for a subscription offer code

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of one-time use code resource IDs for a specific subscription offer code.

**Availability**:
- App Store Connect API 4.4+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}/relationships/oneTimeUseCodes`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`SubscriptionOfferCodeOneTimeUseCodesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing One-Time Use Offer Codes
- [Create one-time use offer codes](./post-v1-subscriptionoffercodeonetimeusecodes.md)
  Create one-time use codes for an auto-renewable subscription offer.
- [Read one-time use offer code information](./get-v1-subscriptionoffercodeonetimeusecodes-_id_.md)
  Get details about a specific one-time use offer code for an auto-renewable subscription.
- [Deactivate one-time use offer codes](./patch-v1-subscriptionoffercodeonetimeusecodes-_id_.md)
  Deactivate a batch of one-time use offer codes for an auto-renewable subscription.
- [List all one-time use offer codes for an auto-renewable subscription](./get-v1-subscriptionoffercodes-_id_-onetimeusecodes.md)
  Get details about a one-time use code for a specific subscription offer for an auto-renewable subscription.
- [List one-time use offer code values](./get-v1-subscriptionoffercodeonetimeusecodes-_id_-values.md)
  Get a list of one-time use offer codes for an auto-renewable subscription in CSV format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_-relationships-onetimeusecodes)*