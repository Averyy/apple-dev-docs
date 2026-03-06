# GET /v1/gameCenterAppVersions/{id}

**Framework**: App Store Connect API  
**Kind**: httpRequest

Read the Game Center enablement state and related app version information.

**Availability**:
- App Store Connect API 3.6+

#### Discussion

##### Example Request and Response

**Other**:

```not specified
https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc
```

**Other**:

```json
{
  “data” : {
    “type” : “gameCenterAppVersions”,
    “id” : “1d9b87fb-80c4-44eb-a114-a51aeebd82fc”,
    “attributes” : {
      “enabled” : false
    },
    “relationships” : {
      “compatibilityVersions” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc/relationships/compatibilityVersions”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc/compatibilityVersions”
        }
      },
      “appStoreVersion” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc/relationships/appStoreVersion”,
          “related” : “https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc/appStoreVersion”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/1d9b87fb-80c4-44eb-a114-a51aeebd82fc”
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/gameCenterAppVersions/{id}`

## Parameters

- `fields[appStoreVersions]` ([string])
- `fields[gameCenterAppVersions]` ([string])
- `include` ([string])
- `limit[compatibilityVersions]` (integer)

## See Also

- [Read app versions for a Game Center detail](get-v1-gamecenterdetails-_id_-gamecenterappversions.md)
  Get a list of app versions for a Game Center detail.
- [GET /v1/gameCenterDetails/{id}/relationships/gameCenterAppVersions](get-v1-gamecenterdetails-_id_-relationships-gamecenterappversions.md)
- [GET /v1/gameCenterAppVersions/{id}/appStoreVersion](get-v1-gamecenterappversions-_id_-appstoreversion.md)
  Read the app store version and related information for an app version.
- [GET /v1/gameCenterAppVersions/{id}/relationships/appStoreVersion](get-v1-gamecenterappversions-_id_-relationships-appstoreversion.md)
- [GET /v1/gameCenterAppVersions/{id}/compatibilityVersions](get-v1-gamecenterappversions-_id_-compatibilityversions.md)
  Get compatibility version information for a specific app version.
- [GET /v1/gameCenterAppVersions/{id}/relationships/compatibilityVersions](get-v1-gamecenterappversions-_id_-relationships-compatibilityversions.md)
  List all compatible verisons for an app version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-gamecenterappversions-_id_)*