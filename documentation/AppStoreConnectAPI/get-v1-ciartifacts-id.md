# Read xcode cloud artifact information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the artifact Xcode Cloud created for a specific action when it performed a build.

**Availability**:
- App Store Connect API 1.5+

#### Discussion

The example request below retrieves detailed information about a specific artifact Xcode Cloud created when it performed a build. Use the information provided to download the artifact and store it on your own servers. Note that the returned download URL is only valid for a limited amount of time.

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/ciArtifacts/73be0e4e-6da2-471a-b652-47bd99885dbc
```

**Response**:

```json
{    
"data": {
        "type": "ciArtifacts",
        "id": "73be0e4e-6da2-471a-b652-47bd99885dbc",
        "attributes": {
            "fileType": "LOG_BUNDLE",
            "fileName": "exampleName",
            "fileSize": 19,
            "downloadUrl": "https://example.com/url-to-artifact"
        },
        "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/ciArtifacts/73be0e4e-6da2-471a-b652-47bd99885dbc"
        }
    },
    "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/ciArtifacts/73be0e4e-6da2-471a-b652-47bd99885dbc"
    }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/ciArtifacts/{id}`

## Parameters

- `fields[ciArtifacts]` ([string]): Additional fields to include for the Artifacts resource returned by the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-ciartifacts-_id_)*