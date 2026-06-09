# Read build beta detail information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific build beta details resource.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildBetaDetails/{id}`

## Parameters

- `fields[buildBetaDetails]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

## See Also

- [List build beta details](get-v1-buildbetadetails.md)
  Find and list build beta details for all builds.
- [Read the build information of a build beta detail](get-v1-buildbetadetails-_id_-build.md)
  Get the build information for a specific build beta details resource.
- [Get the build ID for a build beta detail](get-v1-buildbetadetails-_id_-relationships-build.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbetadetails-_id_)*