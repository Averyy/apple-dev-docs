# Delete a beta build localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific beta build localization associated with a build.

**Availability**:
- App Store Connect API 1.0+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/betaBuildLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## See Also

- [Create a beta build localization](post-v1-betabuildlocalizations.md)
  Create localized What’s New text for a build.
- [Modify a beta build localization](patch-v1-betabuildlocalizations-_id_.md)
  Update the localized What’s New text for a specific beta build and locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-betabuildlocalizations-_id_)*