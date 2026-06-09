# Delete an App Custom Product Page

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete metadata that you configured for a custom product page.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/appCustomProductPages/eb2b3606-2fef-4aab-a54e-b2e5547c9bc3
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appCustomProductPages/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page resource ID from the [`List All Custom Product Pages for an App`](get-v1-apps-_id_-appcustomproductpages.md) response.

## See Also

- [Create a Custom Product Page](post-v1-appcustomproductpages.md)
  Add a custom product page for your app.
- [Modify an App Custom Product Page](patch-v1-appcustomproductpages-_id_.md)
  Update the name and visibility status of an app custom product page.
- [List All Custom Product Pages for an App](get-v1-apps-_id_-appcustomproductpages.md)
  Get a list of all custom product pages for a specific app.
- [Read Custom Product Page Information](get-v1-appcustomproductpages-_id_.md)
  Get information about a specific app custom product page.
- [List Custom Product Page Versions](get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md)
  List the versions for a custom product page version.
- [Get all version ids for an app custom product page](get-v1-appcustomproductpages-_id_-relationships-appcustomproductpageversions.md)
  Get a list of custom product page version IDs associated with a custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appcustomproductpages-_id_)*