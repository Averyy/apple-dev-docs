# List Custom Product Page Versions

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the versions for a custom product page version.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3/appCustomProductPageVersions
```

**Response**:

```json
{
  "data": [
    {
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
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3/appCustomProductPageVersions"
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

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPages/{id}/appCustomProductPageVersions`

## Parameters

- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.
- `fields[appCustomProductPageVersions]` ([string]): Additional fields to include for each app custom product page version resource returned by the response.
- `filter[state]` ([string]): Filter the returned app custom product page versions by state.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app custom product page version resources to return.
- `limit[appCustomProductPageLocalizations]` (integer): The maximum number of related app custom product page localizations resources to return.
- `fields[appCustomProductPages]` ([string]): Additional fields to include for each app custom product page resource returned by the response.

## See Also

- [Read Custom Product Page Version Information](get-v1-appcustomproductpageversions-_id_.md)
  Get information about a specific app custom product page version.
- [List Custom Product Pages Localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [List localization IDs for a custom product page version](get-v1-appcustomproductpageversions-_id_-relationships-appcustomproductpagelocalizations.md)
  Get a list of localization IDs for a specific custom product page version.
- [Create a Custom Product Page Version](post-v1-appcustomproductpageversions.md)
  Add a version for your app custom product page.
- [Modify a Custom Product Page Version](patch-v1-appcustomproductpageversions-_id_.md)
  Update the name and visibility status of an app custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpages-_id_-appcustomproductpageversions)*