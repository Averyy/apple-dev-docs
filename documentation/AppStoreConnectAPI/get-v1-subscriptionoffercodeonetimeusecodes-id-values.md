# List one-time use offer code values

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of one-time use offer codes for an auto-renewable subscription in CSV format.

**Availability**:
- App Store Connect API 2.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionOfferCodeOneTimeUseCodes/{id}/values`

## Parameters

- `id` (string) *(required)*

## See Also

- [Create one-time use offer codes](post-v1-subscriptionoffercodeonetimeusecodes.md)
  Create one-time use codes for an auto-renewable subscription offer.
- [Read one-time use offer code information](get-v1-subscriptionoffercodeonetimeusecodes-_id_.md)
  Get details about a specific one-time use offer code for an auto-renewable subscription.
- [Deactivate one-time use offer codes](patch-v1-subscriptionoffercodeonetimeusecodes-_id_.md)
  Deactivate a batch of one-time use offer codes for an auto-renewable subscription.
- [List all one-time use offer codes for an auto-renewable subscription](get-v1-subscriptionoffercodes-_id_-onetimeusecodes.md)
  Get details about a one-time use code for a specific subscription offer for an auto-renewable subscription.
- [List one-time-use code IDs for a subscription offer code](get-v1-subscriptionoffercodes-_id_-relationships-onetimeusecodes.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionoffercodeonetimeusecodes-_id_-values)*