# List localization IDs for a custom product page version

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of localization IDs for a specific custom product page version.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageVersions/{id}/relationships/appCustomProductPageLocalizations`

## Parameters

- `limit` (integer): The maximum number of app custom product page localization resource identifiers to return.

## See Also

- [Read Custom Product Page Version Information](get-v1-appcustomproductpageversions-_id_.md)
  Get information about a specific app custom product page version.
- [List Custom Product Page Versions](get-v1-appcustomproductpages-_id_-appcustomproductpageversions.md)
  List the versions for a custom product page version.
- [List Custom Product Pages Localizations](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md)
  List all localizations for an app custom product page.
- [Create a Custom Product Page Version](post-v1-appcustomproductpageversions.md)
  Add a version for your app custom product page.
- [Modify a Custom Product Page Version](patch-v1-appcustomproductpageversions-_id_.md)
  Update the name and visibility status of an app custom product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpageversions-_id_-relationships-appcustomproductpagelocalizations)*