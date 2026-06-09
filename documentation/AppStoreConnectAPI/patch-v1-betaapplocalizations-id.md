# Modify a beta app localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the localized information for a specific beta app and locale.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [App Store Connect API 3.7 release notes](app-store-connect-api-3-7-release-notes.md)

#### Overview

> ❗ **Important**:  A description is required for all `betaAppLocalizations` before you can submit to beta app review. After you have added data to the fields for this resource, you can change that data, but you cannot remove data.

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/betaAppLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `betaAppLocalizations` resource ID from the [`List beta app localizations`](get-v1-betaapplocalizations.md) response.

## See Also

- [Create a beta app localization](post-v1-betaapplocalizations.md)
  Create localized descriptive information for an app.
- [Delete a beta app localization](delete-v1-betaapplocalizations-_id_.md)
  Delete a beta app localization associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-betaapplocalizations-_id_)*