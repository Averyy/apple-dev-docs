# List custom product pages localizations

**Framework**: App Store Connect API  
**Kind**: httpRequest

List all localizations for an app custom product page.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
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

- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appPreviewSets]` ([string])
- `fields[appScreenshotSets]` ([string])
- `filter[locale]` ([string])
- `include` ([string])
- `limit` (integer)
- `limit[appPreviewSets]` (integer)
- `limit[appScreenshotSets]` (integer)
- `fields[appCustomProductPageVersions]` ([string])
- `fields[appKeywords]` ([string])
- `limit[searchKeywords]` (integer)

## See Also

- [Read custom product page localization information](get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [Create a custom product page localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify custom product page localization information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [Delete an app custom product page localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations)*