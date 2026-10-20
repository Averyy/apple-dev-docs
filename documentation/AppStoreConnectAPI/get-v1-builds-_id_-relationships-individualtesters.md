# Get all resource ids of individual testers for a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of resource IDs of individual testers associated with a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/relationships/individualTesters`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

### Query Parameters

- `limit` (integer): Number of resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`BuildIndividualTestersLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing Individually Assigned Beta Testers
- [List all individual testers for a build](./get-v1-builds-_id_-individualtesters.md)
  Get a list of beta testers individually assigned to a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-relationships-individualtesters)*