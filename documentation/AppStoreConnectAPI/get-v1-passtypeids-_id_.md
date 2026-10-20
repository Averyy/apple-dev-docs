# Read passtypeid information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific pass type ID.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/passTypeIds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `name`, `certificateType`, `displayName`, `serialNumber`, `platform`, `expirationDate`, `certificateContent`, `activated`, `passTypeId`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `name`, `identifier`, `certificates`
- `include` ([string]): **Allowed Values**: `certificates`
- `limit[certificates]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`PassTypeIdResponse`, `application/json`)
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
- [List all certificates for a passtypeid](./get-v1-passtypeids-_id_-certificates.md)
  List all certificates for a specific pass type ID.
- [List certificate ids for a passtypeid](./get-v1-passtypeids-_id_-relationships-certificates.md)
  List all certificate IDs for a specific pass type ID.
- [Modify a passtypeid](./patch-v1-passtypeids-_id_.md)
  Update a specific pass type ID’s name.
- [Create a passtypeid](./post-v1-passtypeids.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [Delete a passtypeid](./delete-v1-passtypeids-_id_.md)
  Delete a pass type ID that is used for app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-passtypeids-_id_)*