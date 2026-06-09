# List beta license agreements

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta license agreements for all apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaLicenseAgreements`

## Parameters

- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[betaLicenseAgreements]` ([string]): Fields to return for included related types.
- `filter[app]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.

## See Also

- [Read beta license agreement information](get-v1-betalicenseagreements-_id_.md)
  Get a specific beta license agreement.
- [Read the app information of a beta license agreement](get-v1-betalicenseagreements-_id_-app.md)
  Get the app information for a specific beta license agreement.
- [Get the app ID for a beta license agreement](get-v1-betalicenseagreements-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betalicenseagreements)*