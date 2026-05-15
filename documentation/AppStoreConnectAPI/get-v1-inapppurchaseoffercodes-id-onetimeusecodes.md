# List All One-Time Use Codes for an In-App Purchase Offer Code

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of one-time use codes for a specific in-app purchase offer code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodes/{id}/oneTimeUseCodes`

## Parameters

- `fields[actors]` ([string])
- `fields[inAppPurchaseOfferCodeOneTimeUseCodes]` ([string])
- `include` ([string])
- `limit` (integer)

## See Also

- [Create an In-App Purchase Offer Code One-Time Use Code](post-v1-inapppurchaseoffercodeonetimeusecodes.md)
  Create a one-time use code for an in-app purchase offer code.
- [Read In-App Purchase Offer Code One-Time Use Code Information](get-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Get information about a specific in-app purchase offer code one-time use code.
- [Modify an In-App Purchase Offer Code One-Time Use Code](patch-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Update a specific in-app purchase offer code one-time use code.
- [List All Values for an In-App Purchase Offer Code One-Time Use Code](get-v1-inapppurchaseoffercodeonetimeusecodes-_id_-values.md)
  Get a list of values for a specific in-app purchase offer code one-time use code.
- [Get All One-Time Use Code IDs for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-relationships-onetimeusecodes.md)
  Get a list of one-time use code resource IDs for a specific in-app purchase offer code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseoffercodes-_id_-onetimeusecodes)*