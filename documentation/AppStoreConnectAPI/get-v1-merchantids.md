# List merchant ids

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all merchant Ids for your team.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/merchantIds`

## Parameters

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `fields[merchantIds]` ([string]): **Allowed Values**: `name`, `identifier`, `certificates`
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `include` ([string]): **Allowed Values**: `certificates`
- `limit` (integer): **Maximum**: `200`
- `limit[certificates]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `name`, `-name`, `identifier`, `-identifier`

## Responses

- `200` OK (`MerchantIdsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing merchant IDs
- [Managing merchant IDs and Payment Processing certificates](./managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [Read details for a merchant id](./get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List certificates for a merchant id](./get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [List certificate IDs for a merchant ID](./get-v1-merchantids-_id_-relationships-certificates.md)
- [Modify merchant ids](./patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a merchant id](./post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a merchant id](./delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-merchantids)*