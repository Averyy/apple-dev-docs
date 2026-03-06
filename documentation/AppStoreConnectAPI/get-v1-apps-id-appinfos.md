# List All App Infos for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about an app that is currently live on App Store, or that goes live with the next version.

**Availability**:
- App Store Connect API 1.2+

#### Discussion

Use this endpoint to retrieve the derived app-level information for an app. If the app has both a “Ready for Sale” version and a version you’re preparing for release, it will have two app infos. One represents information about the app currently in the App Store, and the other represents the information that takes effect when you release the next version. Use the `appStoreState` attribute to differentiate them.

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/1462965264/appInfos
```

**Response**:

```json
{
  "data": [
    {
      "type": "appInfos",
      "id": "726ad1bb-3e1e-40eb-a986-d8a9897e4f1d",
      "attributes": {
        "appStoreState": "PREPARE_FOR_SUBMISSION",
        "appStoreAgeRating": "NINE_PLUS",
        "brazilAgeRating": "TEN",
        "kidsAgeBand": null
      },
      "relationships": {
        "app": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/app",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/app"
          }
        },
        "appInfoLocalizations": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/appInfoLocalizations",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/appInfoLocalizations"
          }
        },
        "primaryCategory": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/primaryCategory",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/primaryCategory"
          }
        },
        "primarySubcategoryOne": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/primarySubcategoryOne",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/primarySubcategoryOne"
          }
        },
        "primarySubcategoryTwo": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/primarySubcategoryTwo",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/primarySubcategoryTwo"
          }
        },
        "secondaryCategory": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/secondaryCategory",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/secondaryCategory"
          }
        },
        "secondarySubcategoryOne": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/secondarySubcategoryOne",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/secondarySubcategoryOne"
          }
        },
        "secondarySubcategoryTwo": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/relationships/secondarySubcategoryTwo",
            "related": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d/secondarySubcategoryTwo"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appInfos/726ad1bb-3e1e-40eb-a986-d8a9897e4f1d"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/1462965264/appInfos"
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appInfos`

## Parameters

- `fields[appInfos]` ([string]): Fields to return for included related types.
- `limit` (integer): Number of resources to return.
- `include` ([string]): Relationship data to include in the response.
- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[appInfoLocalizations]` ([string]): Fields to return for included related types.
- `fields[appCategories]` ([string]): Fields to return for included related types.
- `fields[ageRatingDeclarations]` ([string]): Fields to return for included related types.
- `limit[appInfoLocalizations]` (integer)

## See Also

- [GET /v1/apps/{id}/relationships/appInfos](get-v1-apps-_id_-relationships-appinfos.md)
- [List All App Store Versions for an App](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [GET /v1/apps/{id}/relationships/appStoreVersions](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the End User License Agreement Information of an App](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [GET /v1/apps/{id}/relationships/endUserLicenseAgreement](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List all custom product pages for an app](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource IDs for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [GET /v1/apps/{id}/appStoreVersionExperimentsV2](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
- [GET /v1/apps/{id}/relationships/appStoreVersionExperimentsV2](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appinfos)*