# List Beta License Agreements

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

- [Read Beta License Agreement Information](get-v1-betalicenseagreements-_id_.md)
  Get a specific beta license agreement.
- [Read the App Information of a Beta License Agreement](get-v1-betalicenseagreements-_id_-app.md)
  Get the app information for a specific beta license agreement.
- [GET /v1/betaLicenseAgreements/{id}/relationships/app](get-v1-betalicenseagreements-_id_-relationships-app.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betalicenseagreements)*