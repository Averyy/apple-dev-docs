# List Pass Type Ids

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Find and list pass type IDs that are registered to your team.

## Endpoint

`GET https://api.enterprise.developer.apple.com/v1/passTypeIds`

## Parameters

### Query Parameters

- `fields[certificates]` ([string]): **Allowed Values**: `certificateContent`, `certificateType`, `csrContent`, `displayName`, `expirationDate`, `name`, `passTypeId`, `platform`, `serialNumber`
- `fields[passTypeIds]` ([string]): **Allowed Values**: `certificates`, `identifier`, `name`
- `filter[id]` ([string])
- `filter[identifier]` ([string])
- `filter[name]` ([string])
- `include` ([string]): **Allowed Values**: `certificates`
- `limit` (integer): **Maximum**: `200`
- `limit[certificates]` (integer): **Maximum**: `50`
- `sort` ([string]): **Allowed Values**: `id`, `-id`, `identifier`, `-identifier`, `name`, `-name`

## Responses

- `200` OK (`PassTypeIdsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.

## See Also

### Managing Pass Type Ids
- [Create a PassTypeId](./create-a-passtypeid.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [Read PassTypeId Information](./read-passtypeid-information.md)
  Get information about a specific pass type ID.
- [List All Certificates for a PassTypeId](./list-all-certificates-for-a-passtypeid.md)
  List all certificates for a specific pass type ID.
- [Modify a PassTypeId](./modify-a-passtypeid.md)
  Update a specific pass type ID’s name.
- [Delete a PassTypeId](./delete-a-passtypeid.md)
  Delete a pass type ID that is used for app development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/list-pass-type-ids)*