# Read beta build localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a specific beta build localization resource.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/betaBuildLocalizations/{id}`

## Parameters

- `fields[betaBuildLocalizations]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.

## See Also

- [List beta build localizations](get-v1-betabuildlocalizations.md)
  Find and list beta build localizations currently associated with apps.
- [Read the build information of a beta build localization](get-v1-betabuildlocalizations-_id_-build.md)
  Get the build information for a specific beta build localization.
- [Get the build ID for a beta build localization](get-v1-betabuildlocalizations-_id_-relationships-build.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-betabuildlocalizations-_id_)*