# Read custom product page information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about a specific app custom product page.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3
```

**Response**:

```json
{
  "data": {
    "type": "appCustomProductPages",
    "id": "eb2b3606-2fef-4aab-a54e-b2e5547c9bc3",
    "attributes": {
      "name": "Custom Product Page May 1",
      "url": "https://apps.apple.com/us/app/gersey-numba/id1526908970?ppid=eb2b3606-2fef-4aab-a54e-b2e5547c9bc3",
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
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPages/{id}`

## Parameters

- `fields[appCustomProductPageVersions]` ([string])
- `fields[appCustomProductPages]` ([string])
- `include` ([string])
- `limit[appCustomProductPageVersions]` (integer)

## See Also

- [Create a custom product page](post-v1-appcustomproductpages.md)
  Add a custom product page for your app.
- [Modify an app custom product page](patch-v1-appcustomproductpages-_id_.md)
  Update the name and visibility status of an app custom product page.
- [List all custom product pages for an app](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [List custom product page versions](get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md)
  List the versions for a custom product page version.
- [Get all version IDs for an app custom product page](get-v1-appcustomproductpages-_id_-relationships-appcustomproductpageversions.md)
  Get a list of custom product page version IDs associated with a custom product page.
- [Delete an app custom product page](delete-v1-appcustomproductpages-_id_.md)
  Delete metadata that you configured for a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpages-_id_)*