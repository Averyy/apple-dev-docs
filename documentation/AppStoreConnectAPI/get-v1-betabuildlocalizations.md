# List Beta Build Localizations

**Framework**: App Store Connect API  
**Kind**: httpRequest

Find and list beta build localizations currently associated with apps.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaBuildLocalizations`

## Parameters

- `fields[betaBuildLocalizations]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `filter[build]` ([string]): Attributes, relationships, and IDs by which to filter.
- `filter[locale]` ([string]): Attributes, relationships, and IDs by which to filter.
- `include` ([string]): Relationship data to include in the response.
- `limit` (integer): Number of resources to return.

## See Also

- [Read Beta Build Localization Information](get-v1-betabuildlocalizations-_id_.md)
  Get a specific beta build localization resource.
- [Read the Build Information of a Beta Build Localization](get-v1-betabuildlocalizations-_id_-build.md)
  Get the build information for a specific beta build localization.
- [GET /v1/betaBuildLocalizations/{id}/relationships/build](get-v1-betabuildlocalizations-_id_-relationships-build.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betabuildlocalizations)*