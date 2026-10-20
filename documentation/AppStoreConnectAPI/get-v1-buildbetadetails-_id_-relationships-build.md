# Get the build ID for a build beta detail

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildBetaDetails/{id}/relationships/build`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`BuildBetaDetailBuildLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting Build Beta Details Information
- [List build beta details](./get-v1-buildbetadetails.md)
  Find and list build beta details for all builds.
- [Read build beta detail information](./get-v1-buildbetadetails-_id_.md)
  Get a specific build beta details resource.
- [Read the build information of a build beta detail](./get-v1-buildbetadetails-_id_-build.md)
  Get the build information for a specific build beta details resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbetadetails-_id_-relationships-build)*