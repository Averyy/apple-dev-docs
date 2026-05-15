# Delete a Merchant ID

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific merchant ID.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/merchantIds/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the merchant ID resource ID from the [`List Merchant IDs`](get-v1-merchantids.md) response.

## See Also

- [Managing merchant IDs and Payment Processing certificates](managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [List Merchant IDs](get-v1-merchantids.md)
  List all merchant Ids for your team.
- [Read Details for a Merchant ID](get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List Certificates for a Merchant ID](get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [GET /v1/merchantIds/{id}/relationships/certificates](get-v1-merchantids-_id_-relationships-certificates.md)
- [Modify Merchant IDs](patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a Merchant ID](post-v1-merchantids.md)
  Add a new merchant ID to your team.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-merchantids-_id_)*