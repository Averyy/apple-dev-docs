# Modify a PassTypeId

**Framework**: Enterprise Program API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update a specific pass type ID’s name.

## Overview

- HTTPBody

## Endpoint

`PATCH https://api.enterprise.developer.apple.com/v1/passTypeIds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `PassTypeIdUpdateRequest`

## Responses

- `200` OK (`PassTypeIdResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)

## See Also

### Managing Pass Type Ids
- [Create a PassTypeId](./create-a-passtypeid.md)
  Create a new identifier for use with a pass type ID certificate using a certificate signing request.
- [List Pass Type Ids](./list-pass-type-ids.md)
  Find and list pass type IDs that are registered to your team.
- [Read PassTypeId Information](./read-passtypeid-information.md)
  Get information about a specific pass type ID.
- [List All Certificates for a PassTypeId](./list-all-certificates-for-a-passtypeid.md)
  List all certificates for a specific pass type ID.
- [Delete a PassTypeId](./delete-a-passtypeid.md)
  Delete a pass type ID that is used for app development.


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/modify-a-passtypeid)*