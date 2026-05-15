# Read Custom Product Page Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific app custom product page version.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a
```

**Response**:

```json
{
  "data": {
    "type": "appCustomProductPageVersions",
    "id": "c7eadc0b-48d9-48c4-bdb2-109dd94a793a",
    "attributes": {
      "version": "1",
      "state": "PREPARE_FOR_SUBMISSION"
    },
    "relationships": {
      "appCustomProductPageLocalizations": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a/relationships/appCustomProductPageLocalizations",
          "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a/appCustomProductPageLocalizations"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/c7eadc0b-48d9-48c4-bdb2-109dd94a793a"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/{id}`

## Parameters

- `fields[appCustomProductPageLocalizations]` ([string])
- `fields[appCustomProductPageVersions]` ([string])
- `include` ([string])
- `limit[appCustomProductPageLocalizations]` (integer)
- `fields[appCustomProductPages]` ([string])

## See Also

- [List Custom Product Page Versions](get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md)
  List the versions for a custom product page version.
- [List Custom Product Pages Localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [GET /v1/appCustomProductPageVersions/{id}/relationships/appCustomProductPageLocalizations](get-v1-appcustomproductpageversions-_id_-relationships-appcustomproductpagelocalizations.md)
- [Create a Custom Product Page Version](post-v1-appcustomproductpageversions.md)
  Add a version for your app custom product page.
- [Modify a Custom Product Page Version](patch-v1-appcustomproductpageversions-_id_.md)
  Update the name and visibility status of an app custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpageversions-_id_)*