# List all certificates for a passtypeid

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all certificates for a specific pass type ID.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/passTypeIds/{id}/certificates`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `name`, `identifier`, `certificates`
- `filter[certificateType]` ([string]): **Allowed Values**: `APPLE_PAY`, `APPLE_PAY_MERCHANT_IDENTITY`, `APPLE_PAY_PSP_IDENTITY`, `APPLE_PAY_RSA`, `DEVELOPER_ID_KEXT`, `DEVELOPER_ID_KEXT_G2`, `DEVELOPER_ID_APPLICATION`, `DEVELOPER_ID_APPLICATION_G2`, `DEVELOPMENT`, `DISTRIBUTION`, `IDENTITY_ACCESS`, `IOS_DEVELOPMENT`, `IOS_DISTRIBUTION`, `MAC_APP_DISTRIBUTION`, `MAC_INSTALLER_DISTRIBUTION`, `MAC_APP_DEVELOPMENT`, `PASS_TYPE_ID`, `PASS_TYPE_ID_WITH_NFC`
- `filter[displayName]` ([string])
- `filter[id]` ([string])
- `filter[serialNumber]` ([string])
- `include` ([string]): **Allowed Values**: `passTypeId`
- `limit` (integer): **Maximum**: `200`
- `sort` ([string]): **Allowed Values**: `displayName`, `-displayName`, `certificateType`, `-certificateType`, `serialNumber`, `-serialNumber`, `id`, `-id`

## Responses

- `200` OK (`CertificatesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing pass type Ids
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-passtypeid.md)
  List all PassTypeID Ids for a specific certificate.
- [List passtypeid ids for a certificate](./get-v1-certificates-_id_-relationships-passtypeid.md)
  List all PassTypeIDId Ids for a specific certificate.
- [List pass type ids](./get-v1-passtypeids.md)
  Find and list pass type IDs that are registered to your team.
- [Read passtypeid information](./get-v1-passtypeids-_id_.md)
  Get information about a specific pass type ID.
- [List certificate ids for a passtypeid](./get-v1-passtypeids-_id_-relationships-certificates.md)
  List all certificate IDs for a specific pass type ID.
- [Modify a passtypeid](./patch-v1-passtypeids-_id_.md)
  Update a specific pass type ID’s name.
- [Create a passtypeid](./post-v1-passtypeids.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [Delete a passtypeid](./delete-v1-passtypeids-_id_.md)
  Delete a pass type ID that is used for app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-passtypeids-_id_-certificates)*