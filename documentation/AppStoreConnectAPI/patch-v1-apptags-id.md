# Modify App Tags

**Framework**: App Store Connect API  
**Kind**: httpRequest

Opt out of app tags for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appTags/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app tag resource ID from the [`List App Tags`](get-v1-apps-_id_-apptags.md) response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-apptags-_id_)*