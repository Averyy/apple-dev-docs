# List beta app review details

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta app review details for all apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaAppReviewDetails]` ([string]): Fields to return for included related types.
- `filter[app]` ([string]) *(required)*: Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.

## See Also

- [Read beta app review detail information](get-v1-betaappreviewdetails-_id_.md)
  Get beta app review details for a specific app.
- [Read the app information of a beta app review detail](get-v1-betaappreviewdetails-_id_-app.md)
  Get the app information for a specific beta app review details resource.
- [Get the app ID for a beta app review detail](get-v1-betaappreviewdetails-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappreviewdetails)*