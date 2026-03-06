# Delete an app custom product page localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete localized metadata that you configured for a custom product page.

**Availability**:
- App Store Connect API 1.7+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/736966e2-178b-4e3f-bfb9-474eb19fbd8c
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page localization resource ID from the [`List custom product pages localizations`](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md) response.

## See Also

- [List custom product pages localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Read custom product page localization information](get-v1-appcustomproductpagelocalizations-_id_.md)
  Get information about a specific app custom product page localization.
- [Create a custom product page localization](post-v1-appcustomproductpagelocalizations.md)
  Add a localization for your app custom product page.
- [Modify custom product page localization information](patch-v1-appcustomproductpagelocalizations-_id_.md)
  Update the promotional text for an app custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appcustomproductpagelocalizations-_id_)*