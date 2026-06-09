# Read beta app review detail information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get beta app review details for a specific app.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaAppReviewDetails/{id}`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaAppReviewDetails]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

## See Also

- [List beta app review details](get-v1-betaappreviewdetails.md)
  Find and list beta app review details for all apps.
- [Read the app information of a beta app review detail](get-v1-betaappreviewdetails-_id_-app.md)
  Get the app information for a specific beta app review details resource.
- [Get the app ID for a beta app review detail](get-v1-betaappreviewdetails-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betaappreviewdetails-_id_)*