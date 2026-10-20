# Modify merchant ids

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific merchant ID.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/merchantIds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the merchant ID resource ID from the [`List merchant ids`](./get-v1-merchantids.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `MerchantIdUpdateRequest`

## Responses

- `200` OK (`MerchantIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing merchant IDs
- [Managing merchant IDs and Payment Processing certificates](./managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [List merchant ids](./get-v1-merchantids.md)
  List all merchant Ids for your team.
- [Read details for a merchant id](./get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List certificates for a merchant id](./get-v1-merchantids-_id_-certificates.md)
  Get a list of all certificates for a specific merchant ID.
- [List certificate IDs for a merchant ID](./get-v1-merchantids-_id_-relationships-certificates.md)
- [Create a merchant id](./post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a merchant id](./delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-merchantids-_id_)*