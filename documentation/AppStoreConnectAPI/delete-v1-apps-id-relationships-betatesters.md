# Remove Specified Beta Testers From All Groups and Builds of an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove one or more beta testers’ access to test any builds of a specific app.

**Availability**:
- App Store Connect API 1.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/1000001234/relationships/betaTesters -d
"{
  "data": [
    {
      "type": "betaTesters",
      "id": "b6318884-4aa6-4586-bf0b-be97cf991817"
    }
  ]
}
"
```

**Response**:

```json
204 No Content
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/apps/{id}/relationships/betaTesters`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List Apps`](get-v1-apps.md) response.

## See Also

- [List All Beta Groups for an App](get-v1-apps-_id_-betagroups.md)
  Get a list of beta groups associated with a specific app.
- [GET /v1/apps/{id}/relationships/betaGroups](get-v1-apps-_id_-relationships-betagroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-apps-_id_-relationships-betatesters)*