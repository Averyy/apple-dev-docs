# Read Usage Metrics for a Beta Build

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get usage metrics for a specific build.

**Availability**:
- App Store Connect API 3.1+

#### Discussion

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/builds/ace4f47a-60ae-4ed6-954f-c4e61c7baab0/metrics/betaBuildUsages
```

**Response**:

```json
{
  “data”: [
    {
      “type”: “betaBuildUsages”,
      “dataPoints”: [
        {
          “start”: “2022-10-05”,
          “end”: “2023-10-05”,
          “values”: {
            “installCount”: 2,
            “crashCount”: 0,
            “sessionCount”: 0,
            “inviteCount”: 0,
            “feedbackCount”: 0
          }
        }
      ]
    }
  ],
  “links”: {
    “self”: “https://api.appstoreconnect.apple.com/v1/builds/ace4f47a-60ae-4ed6-954f-c4e61c7baab0/metrics/betaBuildUsages”
  },
  “meta”: {
    “paging”: {
      “total”: 1,
      “limit”: 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/builds/{id}/metrics/betaBuildUsages`

## Parameters

- `limit` (integer)

## See Also

- [List Builds](get-v1-builds.md)
  Find and list builds for all apps in App Store Connect.
- [Read Build Information](get-v1-builds-_id_.md)
  Get information about a specific build.
- [Read the App Information of a Build](get-v1-builds-_id_-app.md)
  Get the app information for a specific build.
- [Read the App ID of a Build](get-v1-builds-_id_-relationships-app.md)
  Get the app ID for a specific build.
- [Read the App Store Version Information of a Build](get-v1-builds-_id_-appstoreversion.md)
  Get the App Store version of a specific build.
- [GET /v1/builds/{id}/relationships/appStoreVersion](get-v1-builds-_id_-relationships-appstoreversion.md)
- [Read the Prerelease Version of a Build](get-v1-builds-_id_-prereleaseversion.md)
  Get the prerelease version for a specific build.
- [GET /v1/builds/{id}/relationships/preReleaseVersion](get-v1-builds-_id_-relationships-prereleaseversion.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-builds-_id_-metrics-betabuildusages)*