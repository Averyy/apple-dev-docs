# Read an app asset library

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app’s asset library.

**Availability**:
- App Store Connect API 4.5+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890
```

**Response**:

```json
{
  "data" : {
    "type" : "appAssetLibraries",
    "id" : "1234567890",
    "relationships" : {
      "images" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/images",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/images"
        }
      },
      "videos" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/relationships/videos",
          "related" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890/videos"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraries/1234567890"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraries/{id}`

## Parameters

- `fields[appAssetLibraries]` ([string]): Additional fields to include for each app asset library resource returned by the response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraries-_id_)*