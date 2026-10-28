# Modify a build

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Expire a build or change its encryption exemption setting.

**Availability**:
- App Store Connect API 1.0+

## Mentions

- [App Store Connect API 3.0 release notes](./app-store-connect-api-3-0-release-notes.md)

## Discussion

### Example Request and Response

**Request**:

```
PATCH https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee
-d {
  “data” : {
    “type”: “builds”,
    “id”: “932eff64-a144-4350-8d10-9e54d5834aee”,
    “attributes”: {
      “usesNonExemptEncryption” : true      
    },
    “relationships”: {
      “appEncryptionDeclaration”: {
        “data”: {
          “type”: “appEncryptionDeclarations”,
          “id”: “51f19f70-ccd2-4ab9-986b-d7c38ee3e60c”
        }
      }
    }
  }
}’

```

**Response**:

```json
{
  “data” : {
    “type” : “builds”,
    “id” : “932eff64-a144-4350-8d10-9e54d5834aee”,
    “attributes” : {
      “version” : “153”,
      “uploadedDate” : “2022-04-14T11:11:14-07:00”,
      “expirationDate” : “2022-07-13T11:11:14-07:00”,
      “expired” : false,
      “minOsVersion” : “14.3”,
      “lsMinimumSystemVersion” : “11.0”,
      “computedMinMacOsVersion” : “11.0”,
      “iconAssetToken” : {
        “templateUrl” : “https://is1.mzstatic.com/image/thumb/Purple123/v4/0b/84/ee/0b84eed1-e323-8b13-591b-163e1cfa8d67/Icon-83.5@2x.png.png/{w}x{h}bb.{f}”,
        “width” : 167,
        “height” : 167
      },
      “processingState” : “VALID”,
      “buildAudienceType” : null,
      “usesNonExemptEncryption” : true,
      “isWatchOnly” : false,
      “hasMessagesExtension” : false,
      “hasStickers” : false,
      “isLaunchProhibited” : false,
      “qcState” : “BETA_INTERNAL_TESTING”,
      “deviceFamilies” : [ “IPHONE”, “IPAD” ]
    },
    “relationships” : {
      “ciBuildGroup” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/ciBuildGroup”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/ciBuildGroup”
        }
      },
      “preReleaseVersion” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/preReleaseVersion”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/preReleaseVersion”
        }
      },
      “individualTesters” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/individualTesters”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/individualTesters”
        }
      },
      “betaBuildMetrics” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/betaBuildMetrics”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/betaBuildMetrics”
        }
      },
      “betaGroups” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/betaGroups”
        }
      },
      “betaBuildLocalizations” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/betaBuildLocalizations”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/betaBuildLocalizations”
        }
      },
      “appEncryptionDeclaration” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/appEncryptionDeclaration”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/appEncryptionDeclaration”
        }
      },
      “betaAppReviewSubmission” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/betaAppReviewSubmission”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/betaAppReviewSubmission”
        }
      },
      “app” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/app”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/app”
        }
      },
      “buildBetaDetail” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/buildBetaDetail”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/buildBetaDetail”
        }
      },
      “appStoreVersion” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/appStoreVersion”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/appStoreVersion”
        }
      },
      “icons” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/icons”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/icons”
        }
      },
      “perfPowerMetrics” : {
        “links” : {
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/perfPowerMetrics”
        }
      },
      “diagnosticSignatures” : {
        “links” : {
          “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/relationships/diagnosticSignatures”,
          “related” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee/diagnosticSignatures”
        }
      }
    },
    “links” : {
      “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee”
    }
  },
  “links” : {
    “self” : “https://api.appstoreconnect.apple.com/v1/builds/932eff64-a144-4350-8d10-9e54d5834aee”
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/builds/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the build resource ID from the [`List builds`](./get-v1-builds.md) response.

## Request Body

**Content-Type**: `application/json`  
**Type**: `BuildUpdateRequest`

## Responses

- `200` OK (`BuildResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Modifying Builds
- [Assign the app encryption declaration for a build](./patch-v1-builds-_id_-relationships-appencryptiondeclaration.md)
  Assign an app encryption declaration to a build.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-builds-_id_)*