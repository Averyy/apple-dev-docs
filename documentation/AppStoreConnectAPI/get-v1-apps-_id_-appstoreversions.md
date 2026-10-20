# List all app store versions for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all App Store versions of an app across all platforms.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [Creating alternative distribution packages](creating-alternative-distribution-packages.md)
- [App Store Connect API 1.3 release notes](app-store-connect-api-1-3-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446998023/appStoreVersions
```

**Response**:

```json
{
  "data": [
    {
      "type": "appStoreVersions",
      "id": "2395b439-fccd-4645-95bc-97afbe9e379e",
      "attributes": {
        "platform": "IOS",
        "versionString": "1.0",
        "appStoreState": "PREPARE_FOR_SUBMISSION",
        "copyright": "2022 YNC",
        "releaseType": "MANUAL",
        "earliestReleaseDate": null,
        "usesIdfa": null,
        "downloadable": true,
        "createdDate": "2022-08-31T09:28:28-07:00"
      },
      "relationships": {
        "appStoreVersionLocalizations": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionLocalizations",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionLocalizations"
          }
        },
        "build": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/build",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/build"
          }
        },
        "appStoreVersionPhasedRelease": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionPhasedRelease",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionPhasedRelease"
          }
        },
        "routingAppCoverage": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/routingAppCoverage",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/routingAppCoverage"
          }
        },
        "appStoreReviewDetail": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreReviewDetail",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreReviewDetail"
          }
        },
        "appStoreVersionSubmission": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionSubmission",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionSubmission"
          }
        },
        "idfaDeclaration": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/idfaDeclaration",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/idfaDeclaration"
          }
        },
        "appClipDefaultExperience": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appClipDefaultExperience",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appClipDefaultExperience"
          }
        },
        "appStoreVersionExperiments": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/appStoreVersionExperiments",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/appStoreVersionExperiments"
          }
        },
        "customerReviews": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/relationships/customerReviews",
            "related": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e/customerReviews"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appStoreVersions/2395b439-fccd-4645-95bc-97afbe9e379e"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/6446998023/appStoreVersions"
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

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appStoreVersions`

## Parameters

- `limit` (integer): Number of resources to return.
- `include` ([string]): Relationship data to include in the response.
- `fields[apps]` ([string]): Fields to return for included related types.
- `fields[appStoreVersionSubmissions]` ([string]): Fields to return for included related types.
- `fields[builds]` ([string]): Fields to return for included related types.
- `fields[appStoreVersions]` ([string]): Fields to return for included related types.
- `fields[appStoreReviewDetails]` ([string]): Fields to return for included related types.
- `fields[appStoreVersionPhasedReleases]` ([string]): Fields to return for included related types.
- `fields[routingAppCoverages]` ([string]): Fields to return for included related types.
- `fields[appStoreVersionLocalizations]` ([string]): Fields to return for included related types.
- `filter[id]` ([string]): Fields to return for included related types.
- `filter[versionString]` ([string]): Fields to return for included related types.
- `filter[platform]` ([string]): Fields to return for included related types.
- `filter[appStoreState]` ([string]): Fields to return for included related types.
- `limit[appStoreVersionLocalizations]` (integer)
- `fields[appStoreVersionExperiments]` ([string])
- `limit[appStoreVersionExperiments]` (integer)
- `fields[appClipDefaultExperiences]` ([string])
- `limit[appStoreVersionExperimentsV2]` (integer)
- `filter[appVersionState]` ([string])
- `fields[alternativeDistributionPackages]` ([string])
- `fields[gameCenterAppVersions]` ([string])

## See Also

- [List all app infos for an app](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](get-v1-apps-_id_-relationships-appinfos.md)
- [List App Store version IDs for an app](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the end user license agreement information of an app](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [Get the end user license agreement ID for an app](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List All Custom Product Pages for an App](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource ids for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List all app store experiments for an app](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
  Get a list of all App Store version experiments for a specific app.
- [List App Store version experiment IDs for an app](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appstoreversions)*