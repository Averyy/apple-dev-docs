# Read Custom Product Page Version Information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get information about a specific app custom product page version.

**Availability**:
- App Store Connect API 1.7+

## Discussion

### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page version resource ID from the [`List Custom Product Page Versions`](./get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md) response.

### Query Parameters

- `fields[appCustomProductPageLocalizations]` ([string]): Additional fields to include for each app custom product page localization resource returned by the response.

  **Allowed Values**: `locale`, `promotionalText`, `appCustomProductPageVersion`, `appScreenshotSets`, `appPreviewSets`, `searchKeywords`, `placements`
- `fields[appCustomProductPageVersions]` ([string]): Additional fields to include for each app custom product page version resource returned by the response.

  **Allowed Values**: `version`, `state`, `deepLink`, `appCustomProductPage`, `appCustomProductPageLocalizations`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `appCustomProductPage`, `appCustomProductPageLocalizations`
- `limit[appCustomProductPageLocalizations]` (integer): The maximum number of related app custom product page localizations resources to return.

  **Maximum**: `50`
- `fields[appCustomProductPages]` ([string]): **Allowed Values**: `name`, `url`, `visible`, `app`, `appCustomProductPageVersions`

## Responses

- `200` OK (`AppCustomProductPageVersionResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [List Custom Product Page Versions](./get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md)
  List the versions for a custom product page version.
- [List Custom Product Pages Localizations](./get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [List localization IDs for a custom product page version](./get-v1-appcustomproductpageversions-_id_-relationships-appcustomproductpagelocalizations.md)
  Get a list of localization IDs for a specific custom product page version.
- [Create a Custom Product Page Version](./post-v1-appcustomproductpageversions.md)
  Add a version for your app custom product page.
- [Modify a Custom Product Page Version](./patch-v1-appcustomproductpageversions-_id_.md)
  Update the name and visibility status of an app custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpageversions-_id_)*