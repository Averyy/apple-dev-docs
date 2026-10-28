# Read the end user license agreement information of an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.

**Availability**:
- App Store Connect API 1.2+

## Discussion

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v1/apps/1000001234/endUserLicenseAgreement
```

**Response**:

```json
{
  "data": {
    "type": "endUserLicenseAgreements",
    "id": "d187a413-70fb-45c7-ae43-12345ea0d40",
    "attributes": {
      "agreementText": "This is the agreement. It is vital you read it."
    },
    "relationships": {
      "territories": {
        "links": {
          "self": "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/d187a413-70fb-45c7-ae43-12345ea0d40/relationships/territories",
          "related": "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/d187a413-70fb-45c7-ae43-12345ea0d40/territories"
        }
      }
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/d187a413-70fb-45c7-ae43-12345ea0d40"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/1000001234/endUserLicenseAgreement"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/endUserLicenseAgreement`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[endUserLicenseAgreements]` ([string]): Additional fields to include for each end user license agreement resource returned by the response.

  **Allowed Values**: `agreementText`, `app`, `territories`

## Responses

- `200` OK (`EndUserLicenseAgreementWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Store details for your app
- [List all app infos for an app](./get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](./get-v1-apps-_id_-relationships-appinfos.md)
- [List all app store versions for an app](./get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [List App Store version IDs for an app](./get-v1-apps-_id_-relationships-appstoreversions.md)
- [Get the end user license agreement ID for an app](./get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [List All Custom Product Pages for an App](./get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Get all custom product page resource ids for an app](./get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List all app store experiments for an app](./get-v1-apps-_id_-appstoreversionexperimentsv2.md)
  Get a list of all App Store version experiments for a specific app.
- [List App Store version experiment IDs for an app](./get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-enduserlicenseagreement)*