# Read In-App Purchase Offer Code Custom Code Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific in-app purchase offer code custom code.

**Availability**:
- App Store Connect API 4.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/inAppPurchaseOfferCodeCustomCodes/{id}`

## Parameters

- `fields[inAppPurchaseOfferCodeCustomCodes]` ([string])
- `include` ([string])
- `fields[actors]` ([string])

## See Also

- [Create an In-App Purchase Offer Code Custom Code](post-v1-inapppurchaseoffercodecustomcodes.md)
  Create a custom code for an in-app purchase offer code.
- [List All Custom Codes for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-customcodes.md)
  Get a list of custom codes for a specific in-app purchase offer code.
- [Get All Custom Code IDs for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-relationships-customcodes.md)
  Get a list of custom code resource IDs for a specific in-app purchase offer code.
- [Modify an In-App Purchase Offer Code Custom Code](patch-v1-inapppurchaseoffercodecustomcodes-_id_.md)
  Update a specific in-app purchase offer code custom code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-inapppurchaseoffercodecustomcodes-_id_)*