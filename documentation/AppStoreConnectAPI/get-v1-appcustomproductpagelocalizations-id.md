# Read Custom Product Page Localization Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific app custom product page localization.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Other**:

```not specified
https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/dad51248-3c38-4f19-a814-3c4f6da719dd
```

**Other**:

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
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}`

## Parameters

- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appPreviewSets]` ([string])
- `fields[appScreenshotSets]` ([string])
- `include` ([string])
- `limit[appPreviewSets]` (integer)
- `limit[appScreenshotSets]` (integer)
- `limit[searchKeywords]` (integer)
- `fields[appCustomProductPageVersions]` ([string])

## See Also

- [Create a Custom Product Page Localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify Custom Product Page Localization Information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [List Custom Product Pages Localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [List App Preview Sets for a Custom Product Page Localization](get-v1-appcustomproductpagelocalizations-_id_-apppreviewsets.md)
  List the app preview sets for a specific custom product page localization.
- [List App Screenshot Sets for a Custom Product Page Localization](get-v1-appcustomproductpagelocalizations-_id_-appscreenshotsets.md)
  List the app screenshot sets for a specific custom product page localization.
- [List App Preview Set IDs for a Custom Product Page Localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-apppreviewsets.md)
  List the app preview set IDs for a specific custom product page localization.
- [List App Screenshot Sets IDs for a Custom Product Page Localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-appscreenshotsets.md)
  List the app screenshot set IDs for a specific custom product page localization.
- [Delete an App Custom Product Page Localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.
- [List Custom Product Pages Localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Create a Custom Product Page Localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify Custom Product Page Localization Information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [Delete an App Custom Product Page Localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpagelocalizations-_id_)*