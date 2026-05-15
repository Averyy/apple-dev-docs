# Read Build Upload Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about a specific build upload file for an app.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/buildUploads/{id}`

## Parameters

- `fields[buildUploads]` ([string])
- `include` ([string])
- `fields[buildUploadFiles]` ([string])
- `fields[builds]` ([string])

## See Also

- [List All Build Uploads for an App](get-v1-apps-_id_-builduploads.md)
  Get a list of all build uploads for a specific app.
- [List All Build Uploads IDs for an App](get-v1-apps-_id_-relationships-builduploads.md)
  Get a list of all build upload Ids for a specific app.
- [Create a Build Upload](post-v1-builduploads.md)
  Add a new build upload to an app.
- [Remove a Build Upload](delete-v1-builduploads-_id_.md)
  Remove a specific build upload for an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builduploads-_id_)*