# Read an app asset library ref data

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app asset library reference data resource.

**Availability**:
- App Store Connect API 4.5+

## Mentions

- [Discovering asset specifications](discovering-asset-specifications.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appAssetLibraryRefData/1?fields[appAssetLibraryRefData]=imageSpecs
```

**Response**:

```json
{
  "data" : {
    "type" : "appAssetLibraryRefData",
    "id" : "1",
    "attributes" : {
      "features" : [ {
        "featureId" : "APP_STORE_VERSIONS",
        "placementPolicies" : [ {
          "placementType" : "APP_SCREENSHOT",
          "groupLimits" : [ {
            "groupIds" : [ "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE", "MAC_PROFILE" ],
            "maxCount" : 10
          } ]
        } ]
      } ],
      "placementProfileGroups" : [ {
        "placementProfileGroupId" : "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE",
        "platform" : "IPHONE_APP_STORE",
        "displayClassId" : "IPHONE_DYNAMIC_ISLAND_LARGE_DISPLAY"
      } ],
      "imageSpecs" : [ {
        "specId" : "f56c777c-99ea-5760-97ae-27c5f8cbb884",
        "shortName" : "i1290x2796a0",
        "dimensions" : {
          "minWidth" : 1290,
          "maxWidth" : 1290,
          "minHeight" : 2796,
          "maxHeight" : 2796
        },
        "aspectRatio" : "6:13",
        "compatiblePlacementTypes" : [ "APP_SCREENSHOT", "IMESSAGE_APP_SCREENSHOT" ],
        "alphaAllowed" : false,
        "fileExtensions" : [ ".jpg", ".jpeg", ".png" ],
        "maxFileSize" : 524288000,
        "mimeTypes" : [ "image/jpeg", "image/png" ],
        "universalAsset" : false
      } ],
      "videoSpecs" : [ {
        "specId" : "1861fdcb-eb99-59e6-8c6c-5a07479d9a84",
        "shortName" : "v886x1920f23~30t15~30u1",
        "dimensions" : {
          "minWidth" : 886,
          "maxWidth" : 886,
          "minHeight" : 1920,
          "maxHeight" : 1920
        },
        "aspectRatio" : "6:13",
        "compatiblePlacementTypes" : [ "APP_PREVIEW" ],
        "frameRates" : [ {
          "minFps" : 23,
          "maxFps" : 30
        } ],
        "duration" : {
          "min" : "PT15S",
          "max" : "PT30S"
        },
        "audioRequired" : true,
        "fileExtensions" : [ ".mp4", ".m4v", ".mov" ],
        "maxFileSize" : 524288000,
        "mimeTypes" : [ "video/quicktime", "video/mp4", "video/x-m4v" ],
        "universalAsset" : false
      } ],
      "placementTypes" : [ {
        "placementTypeId" : "APP_SCREENSHOT",
        "acceptsAssetCategories" : [ "APP_SCREENSHOTS_AND_PREVIEWS" ],
        "specMappings" : [ {
          "placementGroupId" : "IPHONE_DYNAMIC_ISLAND_LARGE_PROFILE",
          "specs" : [ "f56c777c-99ea-5760-97ae-27c5f8cbb884" ]
        } ]
      } ],
      "displayClasses" : [ {
        "displayClassId" : "IPHONE_DYNAMIC_ISLAND_LARGE_DISPLAY",
        "deviceFamily" : "IPHONE",
        "screenDimensions" : [ "6.9" ]
      } ]
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryRefData/1"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appAssetLibraryRefData/1"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appAssetLibraryRefData/{id}`

## Parameters

- `fields[appAssetLibraryRefData]` ([string]): Additional fields to include for each app asset library reference data resource returned by the response.

## See Also

- [List app asset library ref data](get-v1-appassetlibraryrefdata.md)
  List app asset library reference data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appassetlibraryrefdata-_id_)*