# List All Custom Product Pages for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of all custom product pages for a specific app.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/01234/appCustomProductPages
```

**Response**:

```json
{
  "data": [
    {
      "type": "appCustomProductPages",
      "id": "eb2b3606-2fef-4aab-a54e-b2e5547c9bc3",
      "attributes": {
        "name": "Custom Product Page May 1",
        "url": "https://apps.apple.com/us/app/name/id01234?ppid=eb2b3606-2fef-4aab-a54e-b2e5547c9bc3",
        "visible": false
      },
      "relationships": {
        "appCustomProductPageVersions": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3/relationships/appCustomProductPageVersions",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3/appCustomProductPageVersions"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3"
      }
    },
    {
      "type": "appCustomProductPages",
      "id": "2a92bd8e-e59a-4b6e-bca0-04209c16fc7e",
      "attributes": {
        "name": "Customer Product Page 1",
        "url": "https://apps.apple.com/us/app/gersey-numba/id1526908970?ppid=2a92bd8e-e59a-4b6e-bca0-04209c16fc7e",
        "visible": true
      },
      "relationships": {
        "appCustomProductPageVersions": {
          "links": {
            "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/2a92bd8e-e59a-4b6e-bca0-04209c16fc7e/relationships/appCustomProductPageVersions",
            "related": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/2a92bd8e-e59a-4b6e-bca0-04209c16fc7e/appCustomProductPageVersions"
          }
        }
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/2a92bd8e-e59a-4b6e-bca0-04209c16fc7e"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/apps/01234/appCustomProductPages"
  },
  "meta": {
    "paging": {
      "total": 2,
      "limit": 50
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appCustomProductPages`

## Parameters

- `fields[appCustomProductPageVersions]` ([string]): Additional fields to include for each app custom product page version resource returned by the response.
- `fields[appCustomProductPages]` ([string]): Additional fields to include for each app custom product page resource returned by the response.
- `filter[visible]` ([string]): Filter the returned app custom product pages by visible.
- `include` ([string]): The relationship data to include in the response.
- `limit` (integer): The maximum number of app custom product page resources to return.
- `limit[appCustomProductPageVersions]` (integer): The maximum number of related app custom product page versions resources to return.
- `fields[apps]` ([string]): Additional fields to include for each app resource returned by the response.

## See Also

- [List all app infos for an app](get-v1-apps-_id_-appinfos.md)
  Get information about an app that is currently live on App Store, or that goes live with the next version.
- [List app info IDs for an app](get-v1-apps-_id_-relationships-appinfos.md)
- [List all app store versions for an app](get-v1-apps-_id_-appstoreversions.md)
  Get a list of all App Store versions of an app across all platforms.
- [List App Store version IDs for an app](get-v1-apps-_id_-relationships-appstoreversions.md)
- [Read the end user license agreement information of an app](get-v1-apps-_id_-enduserlicenseagreement.md)
  Get the custom end user license agreement (EULA) for a specific app and the territories where the agreement applies.
- [Get the end user license agreement ID for an app](get-v1-apps-_id_-relationships-enduserlicenseagreement.md)
- [Get all custom product page resource ids for an app](get-v1-apps-_id_-relationships-appcustomproductpages.md)
  Get a list of custom product page resource IDs associated with an app.
- [List all app store experiments for an app](get-v1-apps-_id_-appstoreversionexperimentsv2.md)
  Get a list of all App Store version experiments for a specific app.
- [List App Store version experiment IDs for an app](get-v1-apps-_id_-relationships-appstoreversionexperimentsv2.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-appcustomproductpages)*