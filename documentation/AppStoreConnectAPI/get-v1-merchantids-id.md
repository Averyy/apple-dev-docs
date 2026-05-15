# Read Details for a Merchant ID

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information for a merchant ID.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/merchantIds/{id}`

## Parameters

- `fields[certificates]` ([string])
- `fields[merchantIds]` ([string])
- `include` ([string])
- `limit[certificates]` (integer)

## See Also

- [Managing merchant IDs and Payment Processing certificates](managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [List Merchant IDs](get-v1-merchantids.md)
  List all merchant Ids for your team.
- [List Certificates for a Merchant ID](get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [GET /v1/merchantIds/{id}/relationships/certificates](get-v1-merchantids-_id_-relationships-certificates.md)
- [Modify Merchant IDs](patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a Merchant ID](post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a Merchant ID](delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-merchantids-_id_)*