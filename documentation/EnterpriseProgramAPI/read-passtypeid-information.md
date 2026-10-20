# Read PassTypeId Information

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific pass type ID.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/passTypeIds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `certificates`, `identifier`, `name`
- `include` ([string]): **Allowed Values**: `certificates`
- `limit[certificates]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`PassTypeIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)

## See Also

### Managing Pass Type Ids
- [Create a PassTypeId](./create-a-passtypeid.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [List Pass Type Ids](./list-pass-type-ids.md)
  Find and list pass type IDs that are registered to your team.
- [List All Certificates for a PassTypeId](./list-all-certificates-for-a-passtypeid.md)
  List all certificates for a specific pass type ID.
- [Modify a PassTypeId](./modify-a-passtypeid.md)
  Update a specific pass type ID’s name.
- [Delete a PassTypeId](./delete-a-passtypeid.md)
  Delete a pass type ID that is used for app development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/read-passtypeid-information)*