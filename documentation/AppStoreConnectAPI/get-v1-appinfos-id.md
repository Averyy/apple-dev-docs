# Read App Info Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read App Store information including your App Store state, age ratings, Brazil age rating, and kids’ age band.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

#### Discussion

For request and response examples for reading an age rating declaration, see [`Read age rating declaration`](get-v1-appinfos-_id_-ageratingdeclaration.md).

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}`

## Parameters

- `fields[appCategories]` ([string]): Fields to return for included related types.
- `fields[appInfoLocalizations]` ([string]): Fields to return for included related types.
- `fields[appInfos]` ([string]): Fields to return for included related types.
- `include` ([string]): Relationship data to include in the response.
- `limit[appInfoLocalizations]` (integer): Number of included related resources to return.
- `fields[ageRatingDeclarations]` ([string]): Fields to return for included related types.

## See Also

- [List All App Infos for an App](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List All App Info Localizations for an App Info](get-v1-appinfos-_id_-appinfolocalizations.md)
  Get a list of localized, app-level information for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_)*