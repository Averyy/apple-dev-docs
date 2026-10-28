# List Custom Product Pages Localizations

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all localizations for an app custom product page.

**Availability**:
- App Store Connect API 1.7+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/6c0df710-d69a-454f-be7c-f5b014788dee/appCustomProductPageLocalizations
```

**Response**:

```json
{
  "data": {
    "type": "appCustomProductPageLocalizations",
    "id": "dad51248-3c38-4f19-a814-3c4f6da719dd",
    "attributes": {
      "locale": "en-US",
      "promotionalText": "This app will inspire!"
    },
    "relationships": {
      "appScreenshotSets": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/relationships/appScreenshotSets",
          "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/appScreenshotSets"
        }
      },
      "appPreviewSets": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/relationships/appPreviewSets",
          "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/appPreviewSets"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd"
  }
}a{
  "data": [
    {
      "type": "appCustomProductPageLocalizations",
      "id": "77cefe66-a51a-4d4d-a5bd-cc40a733def0",
      "attributes": {
        "locale": "en-CA",
        "promotionalText": "This app will bring you inspiration."
      },
      "relationships": {
        "appScreenshotSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/77cefe66-a51a-4d4d-a5bd-cc40a733def0/relationships/appScreenshotSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/77cefe66-a51a-4d4d-a5bd-cc40a733def0/appScreenshotSets"
          }
        },
        "appPreviewSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/77cefe66-a51a-4d4d-a5bd-cc40a733def0/relationships/appPreviewSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/77cefe66-a51a-4d4d-a5bd-cc40a733def0/appPreviewSets"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/77cefe66-a51a-4d4d-a5bd-cc40a733def0"
      }
    },
    {
      "type": "appCustomProductPageLocalizations",
      "id": "dad51248-3c38-4f19-a814-3c4f6da719dd",
      "attributes": {
        "locale": "en-US",
        "promotionalText": "This app will inspire!"
      },
      "relationships": {
        "appScreenshotSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/relationships/appScreenshotSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/appScreenshotSets"
          }
        },
        "appPreviewSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/relationships/appPreviewSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd/appPreviewSets"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd"
      }
    },
    {
      "type": "appCustomProductPageLocalizations",
      "id": "736966e2-178b-4e3f-bfb9-474eb19fbd8c",
      "attributes": {
        "locale": "nl-NL",
        "promotionalText": "Ogenblik!"
      },
      "relationships": {
        "appScreenshotSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c/relationships/appScreenshotSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c/appScreenshotSets"
          }
        },
        "appPreviewSets": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c/relationships/appPreviewSets",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c/appPreviewSets"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/6c0df710-d69a-454f-be7c-f5b014788dee/appCustomProductPageLocalizations"
  },
  "meta": {
    "paging": {
      "total": 3,
      "limit": 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/{id}/appCustomProductPageLocalizations`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page version resource ID from the [`List Custom Product Page Versions`](./get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md) response.

### Query Parameters

- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.

  **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appPreviewSets]` ([string]): Additional fields to include for each app preview set resource returned by the response.

  **Allowed Values**: `previewType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appPreviews`
- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.

  **Allowed Values**: `screenshotDisplayType`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`, `appScreenshots`
- `filter[locale]` ([string]): Filter the returned app custom product page localizations by locale.
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `limit` (integer): The maximum number of app custom product page localization resources to return.

  **Maximum**: `200`
- `limit[appPreviewSets]` (integer): The maximum number of related app preview sets resources to return.

  **Maximum**: `50`
- `limit[appScreenshotSets]` (integer): The maximum number of related app screenshot sets resources to return.

  **Maximum**: `50`
- `fields[appCustomProductPageVersions]` ([string]): Additional fields to include for each app custom product page version resource returned by the response.

  **Allowed Values**: `version`, `state`, `deepLink`, `appCustomProductPage`, `appCustomProductPageLocalizations`
- `fields[appAssetLibraryPlacements]` ([string]): **Allowed Values**: `mediaType`, `placementType`, `placementGroup`, `createdDate`, `lastModifiedDate`, `state`, `stateDetails`, `image`, `video`, `appEventLocalization`, `appStoreVersionLocalization`, `appCustomProductPageLocalization`, `appStoreVersionExperimentTreatmentLocalization`
- `fields[appKeywords]` ([string])
- `limit[placements]` (integer): **Maximum**: `50`
- `limit[searchKeywords]` (integer): **Maximum**: `50`

## Responses

- `200` OK (`AppCustomProductPageLocalizationsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Managing localizations
- [Read Custom Product Page Localization Information](./get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [Create a Custom Product Page Localization](./post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify Custom Product Page Localization Information](./patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [Delete an App Custom Product Page Localization](./delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations)*