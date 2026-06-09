# List custom code IDs for a subscription offer code

**Framework**: App Store Connect API  
**Kind**: httpRequest

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodes/{id}/relationships/customCodes`

## Parameters

- `limit` (integer)

## See Also

- [Create custom offer codes](post-v1-subscriptionoffercodecustomcodes.md)
  Create custom offer codes for an auto-renewable subscription offer.
- [List all custom offer codes for an auto-renewable subscription](get-v1-subscriptionoffercodes-_id_-customcodes.md)
  Get details about a custom code for a specific subscription offer for an auto-renewable subscription.
- [Read custom offer code information](get-v1-subscriptionoffercodecustomcodes-_id_.md)
  Get details about a specific offer code for an auto-renewable subscription.
- [Deactivate custom offer codes](patch-v1-subscriptionoffercodecustomcodes-_id_.md)
  Deactivate a batch of custom offer codes for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodes-_id_-relationships-customcodes)*