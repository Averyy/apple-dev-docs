# List App Screenshot Sets for a Custom Product Page Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the app screenshot sets for a specific custom product page localization.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Other**:

```not specified
https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/e0e9216a-338c-4616-9fd5-0ec6c14c6950/appCustomProductPageLocalizations
```

**Other**:

```json
{
  "data": [
    {
      "type": "appScreenshotSets",
      "id": "3d87ecbb-bcdc-4c2f-b34f-ced3cf666de7",
      "attributes": {
        "screenshotDisplayType": "APP_IPHONE_65"
      },
      "relationships": {
        "appScreenshots": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/3d87ecbb-bcdc-4c2f-b34f-ced3cf666de7/relationships/appScreenshots",
            "related": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/3d87ecbb-bcdc-4c2f-b34f-ced3cf666de7/appScreenshots"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/3d87ecbb-bcdc-4c2f-b34f-ced3cf666de7"
      }
    },
    {
      "type": "appScreenshotSets",
      "id": "a59be7c9-8f97-45cc-939d-09c101c483e3",
      "attributes": {
        "screenshotDisplayType": "APP_IPHONE_55"
      },
      "relationships": {
        "appScreenshots": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/a59be7c9-8f97-45cc-939d-09c101c483e3/relationships/appScreenshots",
            "related": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/a59be7c9-8f97-45cc-939d-09c101c483e3/appScreenshots"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/a59be7c9-8f97-45cc-939d-09c101c483e3"
      }
    },
    {
      "type": "appScreenshotSets",
      "id": "69a9c45d-4508-4b4a-a08e-03e0bc018903",
      "attributes": {
        "screenshotDisplayType": "APP_IPAD_PRO_3GEN_129"
      },
      "relationships": {
        "appScreenshots": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/69a9c45d-4508-4b4a-a08e-03e0bc018903/relationships/appScreenshots",
            "related": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/69a9c45d-4508-4b4a-a08e-03e0bc018903/appScreenshots"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/69a9c45d-4508-4b4a-a08e-03e0bc018903"
      }
    },
    {
      "type": "appScreenshotSets",
      "id": "51bc2274-7517-4e56-82e4-c80f6014d44a",
      "attributes": {
        "screenshotDisplayType": "APP_IPAD_PRO_129"
      },
      "relationships": {
        "appScreenshots": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/51bc2274-7517-4e56-82e4-c80f6014d44a/relationships/appScreenshots",
            "related": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/51bc2274-7517-4e56-82e4-c80f6014d44a/appScreenshots"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appScreenshotSets/51bc2274-7517-4e56-82e4-c80f6014d44a"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/0d95bf9e-8256-4abf-83e2-9b428919100f/appScreenshotSets"
  },
  "meta": {
    "paging": {
      "total": 4,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}/appScreenshotSets`

## Parameters

- `fields[appScreenshotSets]` ([string]): Additional fields to include for each app screenshot set resource returned by the response.
- `fields[appScreenshots]` ([string]): Additional fields to include for each app screenshot resource returned by the response.
- `filter[appStoreVersionExperimentTreatmentLocalization]` ([string]): Filter the returned app screenshot sets by App Store version experiment treatment localization.
- `filter[appStoreVersionLocalization]` ([string]): Filter the returned app screenshot sets by App Store version localization.
- `filter[screenshotDisplayType]` ([string]): Filter the returned app screenshot sets by screenshot display type.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app screenshot set resources to return.
- `limit[appScreenshots]` (integer): The maximum number of related app screenshots resources to return.
- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.
- `fields[appStoreVersionExperimentTreatmentLocalizations]` ([string]): Additional fields to include for each App Store version experiment treatment localization resource returned by the response.
- `fields[appStoreVersionLocalizations]` ([string]): Additional fields to include for each App Store version localization resource returned by the response.

## See Also

- [Create a Custom Product Page Localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify Custom Product Page Localization Information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [List Custom Product Pages Localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Read Custom Product Page Localization Information](get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [List App Preview Sets for a Custom Product Page Localization](get-v1-appcustomproductpagelocalizations-_id_-apppreviewsets.md)
  List the app preview sets for a specific custom product page localization.
- [List app preview set IDs for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-apppreviewsets.md)
  List the app preview set IDs for a specific custom product page localization.
- [List app screenshot sets IDs for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-appscreenshotsets.md)
  List the app screenshot set IDs for a specific custom product page localization.
- [Delete an App Custom Product Page Localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.
- [List app screenshot sets IDs for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-appscreenshotsets.md)
  List the app screenshot set IDs for a specific custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpagelocalizations-_id_-appscreenshotsets)*