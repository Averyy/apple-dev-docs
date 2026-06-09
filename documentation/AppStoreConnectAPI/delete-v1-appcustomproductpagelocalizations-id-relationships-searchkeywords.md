# Remove a Search Keyword From a Custom Product Page Localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Unassign a search keyword from a specific custom product page localization.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}/relationships/searchKeywords`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app custom product page localization resource ID from the [`List Custom Product Pages Localizations`](get-v1-appcustomproductpageversions-_id_-appcustomproductpagelocalizations.md) response.

## See Also

- [List keywords for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-searchkeywords.md)
  List the search keywords for a specific custom product page localization.
- [List all search keywords for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a custom product page localization.
- [Add a Search Keyword to a Custom Product Page Localization](post-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Assign one or more search keywords to a specific custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords)*