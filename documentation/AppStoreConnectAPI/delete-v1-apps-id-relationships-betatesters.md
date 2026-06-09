# Remove specified beta testers from all groups and builds of an app

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

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](get-v1-apps.md) response.

## See Also

- [List all beta groups for an app](get-v1-apps-_id_-betagroups.md)
  Get a list of beta groups associated with a specific app.
- [List beta group IDs for an app](get-v1-apps-_id_-relationships-betagroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-apps-_id_-relationships-betatesters)*