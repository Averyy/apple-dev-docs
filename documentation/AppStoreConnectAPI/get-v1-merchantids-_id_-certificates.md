# List certificates for a merchant id

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of all certificates for a specific merchant ID.

**Availability**:
- App Store Connect API 3.8+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/merchantIds/{id}/certificates`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the merchant ID resource ID from the [`List merchant ids`](./get-v1-merchantids.md) response.

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `filter[certificateType]` ([string]): **Allowed Values**: `APPLE_PAY`, `APPLE_PAY_MERCHANT_IDENTITY`, `APPLE_PAY_PSP_IDENTITY`, `APPLE_PAY_RSA`, `DEVELOPER_ID_KEXT`, `DEVELOPER_ID_KEXT_G2`, `DEVELOPER_ID_APPLICATION`, `DEVELOPER_ID_APPLICATION_G2`, `DEVELOPMENT`, `DISTRIBUTION`, `IDENTITY_ACCESS`, `IOS_DEVELOPMENT`, `IOS_DISTRIBUTION`, `MAC_APP_DISTRIBUTION`, `MAC_INSTALLER_DISTRIBUTION`, `MAC_APP_DEVELOPMENT`, `PASS_TYPE_ID`, `PASS_TYPE_ID_WITH_NFC`
- `filter[displayName]` ([string])
- `filter[id]` ([string])
- `filter[serialNumber]` ([string])
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `displayName`, `-displayName`, `certificateType`, `-certificateType`, `serialNumber`, `-serialNumber`, `id`, `-id`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `name`, `identifier`, `certificates`
- `include` ([string]): **Allowed Values**: `passTypeId`

## Responses

- `200` OK (`CertificatesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing merchant IDs
- [Managing merchant IDs and Payment Processing certificates](./managing-payment-processing-certificates.md)
  Create and update certificates so your app uses Apple Pay and Wallet.
- [List merchant ids](./get-v1-merchantids.md)
  List all merchant Ids for your team.
- [Read details for a merchant id](./get-v1-merchantids-_id_.md)
  Get information for a merchant ID.
- [List certificate IDs for a merchant ID](./get-v1-merchantids-_id_-relationships-certificates.md)
- [Modify merchant ids](./patch-v1-merchantids-_id_.md)
  Update a specific merchant ID.
- [Create a merchant id](./post-v1-merchantids.md)
  Add a new merchant ID to your team.
- [Delete a merchant id](./delete-v1-merchantids-_id_.md)
  Delete a specific merchant ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-merchantids-_id_-certificates)*