# List All Build Uploads for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all build uploads for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/buildUploads`

## Parameters

- `fields[buildUploadFiles]` ([string])
- `fields[buildUploads]` ([string])
- `fields[builds]` ([string])
- `filter[cfBundleShortVersionString]` ([string])
- `filter[cfBundleVersion]` ([string])
- `filter[platform]` ([string])
- `filter[state]` ([string])
- `include` ([string])
- `limit` (integer)
- `sort` ([string])

## See Also

- [List all build uploads ids for an app](get-v1-apps-_id_-relationships-builduploads.md)
  Get a list of all build upload Ids for a specific app.
- [Read Build Upload Information](get-v1-builduploads-_id_.md)
  Get details about a specific build upload file for an app.
- [Create a Build Upload](post-v1-builduploads.md)
  Add a new build upload to an app.
- [Remove a Build Upload](delete-v1-builduploads-_id_.md)
  Remove a specific build upload for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-builduploads)*