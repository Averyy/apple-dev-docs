# List build beta details

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list build beta details for all builds.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildBetaDetails`

## Parameters

- `fields[buildBetaDetails]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `filter[build]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[id]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.

## See Also

- [Read build beta detail information](get-v1-buildbetadetails-_id_.md)
  Get a specific build beta details resource.
- [Read the build information of a build beta detail](get-v1-buildbetadetails-_id_-build.md)
  Get the build information for a specific build beta details resource.
- [Get the build ID for a build beta detail](get-v1-buildbetadetails-_id_-relationships-build.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-buildbetadetails)*