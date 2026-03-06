# Modify custom product page localization information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Update the promotional text for an app custom product page localization.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c
{
    "data": {
        "id": "736966e2-178b-4e3f-bfb9-474eb19fbd8c",
        "type": "appCustomProductPageLocalizations",
        "attributes": {
            "promotionalText": "Ogenblik!"
        }
    }
}
```

**Response**:

```json
{
  "data": {
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
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c"
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page localization resource ID from the [`List custom product pages localizations`](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md) response.

## See Also

- [List custom product pages localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Read custom product page localization information](get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [Create a custom product page localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Delete an app custom product page localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-appcustomproductpagelocalizations-_id_)*