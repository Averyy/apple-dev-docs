# List merchant ids

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all merchant Ids for your team.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/merchantIds`

## Parameters

- `fields[certificates]` ([string])
- `fields[merchantIds]` ([string])
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[certificates]` (integer)
- `sort` ([string])

## See Also

- [Managing merchant IDs and Payment Processing certificates](managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [Read details for a merchant id](get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List certificates for a merchant id](get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [List certificate IDs for a merchant ID](get-v1-merchantids-_id_-relationships-certificates.md)
- [Modify merchant ids](patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a merchant id](post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a merchant id](delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-merchantids)*