# List all app clips for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

List your app’s associated App Clips.

**Availability**:
- App Store Connect API 1.6+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.comv1/apps/{id}/appClips
```

**Response**:

```json
{
  "data": [
    {
      "type": "appClips",
      "id": "37453eec-75b3-4578-aba4-ah345936650",
      "attributes": {
        "bundleId": "com.domain.app.AppClip"
      },
      "relationships": {
        "appClipDefaultExperiences": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/relationships/appClipDefaultExperiences",
            "related": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/appClipDefaultExperiences"
          }
        },
        "appClipAdvancedExperiences": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/relationships/appClipAdvancedExperiences",
            "related": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650/appClipAdvancedExperiences"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appClips/37453eec-75b3-4578-aba4-ah345936650"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/1000001234/appClips"
  },
  "meta": {
    "paging": {
      "total": 1,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appClips`

## Parameters

- `fields[appClipDefaultExperiences]` ([string]): Additional fields to include for each App Clips resource returned by the response.
- `fields[appClips]` ([string]): Additional fields to include for each App Clips resource returned by the response.
- `filter[bundleId]` ([string]): Filter the returned App Clips using the bundle ID of the App Clip.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The number of App Clips resources to return.
- `limit[appClipDefaultExperiences]` (integer): The number of included App Clips resources to return if the default App Clip experience localizations relationship is included.
- `fields[apps]` ([string])

## See Also

- [List App Clip IDs for an app](get-v1-apps-_id_-relationships-appclips.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appclips)*