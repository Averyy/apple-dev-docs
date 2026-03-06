# Create a custom product page localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Add a localization for your app custom product page.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
POST https://appstoreconnect.apple.com/v1/appCustomProductPageLocalizations
{
    "data": {
        "type": "appCustomProductPageLocalizations",
        "attributes": {
            "locale": "en-CA",
            "promotionalText": "There will be so much fun."
        },
        "relationships": {
            "appCustomProductPageVersion": {
                "data": {
                    "type": "appCustomProductPageVersions",
                    "id": "46e3a412-7248-43f8-a6bf-cf445eafa3ef"
                }
            }
        }
    }
}
```

**Response**:

```json
{
  "data" : {
    "type" : "appCustomProductPageLocalizations",
    "id" : "0ff34f9c-e2f9-4317-a3e5-44e012c2ffbc",
    "attributes" : {
      "locale" : "en-CA",
      "promotionalText" : "There will be so much fun."
    },
    "relationships" : {
      "appScreenshotSets" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/0ff34f9c-e2f9-4317-a3e5-44e012c2ffbc/relationships/appScreenshotSets",
          "related" : "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/0ff34f9c-e2f9-4317-a3e5-44e012c2ffbc/appScreenshotSets"
        }
      },
      "appPreviewSets" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/0ff34f9c-e2f9-4317-a3e5-44e012c2ffbc/relationships/appPreviewSets",
          "related" : "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/0ff34f9c-e2f9-4317-a3e5-44e012c2ffbc/appPreviewSets"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/0ff34f9c-e2f9-4317-a3e5-44e012c2ffbc"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations`

## See Also

- [List custom product pages localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Read custom product page localization information](get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [Modify custom product page localization information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.
- [Delete an app custom product page localization](delete-v1-appcustomproductpagelocalizations-_id_.md)
  Delete localized metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v1-appcustomproductpagelocalizations)*