# Deactivate custom offer codes

**Framework**: App Store Connect API  
**Kind**: httpRequest

Deactivate a batch of custom offer codes for an auto-renewable subscription.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodeCustomCodes/{id}`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create custom offer codes](post-v1-subscriptionoffercodecustomcodes.md)
  Create custom offer codes for an auto-renewable subscription offer.
- [List all custom offer codes for an auto-renewable subscription](get-v1-subscriptionoffercodes-_id_-customcodes.md)
  Get details about a custom code for a specific subscription offer for an auto-renewable subscription.
- [List custom code IDs for a subscription offer code](get-v1-subscriptionoffercodes-_id_-relationships-customcodes.md)
- [Read custom offer code information](get-v1-subscriptionoffercodecustomcodes-_id_.md)
  Get details about a specific offer code for an auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptionoffercodecustomcodes-_id_)*