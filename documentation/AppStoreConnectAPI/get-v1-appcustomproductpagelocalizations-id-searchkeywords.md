# List keywords for a custom product page localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the search keywords for a specific custom product page localization.

**Availability**:
- App Store Connect API 4.1+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCustomProductPageLocalizations/{id}/searchKeywords`

## Parameters

- `fields[appKeywords]` ([string]): Additional fields to include for each app keyword resource returned by the response.
- `filter[locale]` ([string]): Filter the returned app keywords by locale.
- `filter[platform]` ([string]): Filter the returned app keywords by platform.
- `limit` (integer): The maximum number of app keyword resources to return.

## See Also

- [List all search keywords for a custom product page localization](get-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a custom product page localization.
- [Add a Search Keyword to a Custom Product Page Localization](post-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Assign one or more search keywords to a specific custom product page localization.
- [Remove a Search Keyword From a Custom Product Page Localization](delete-v1-appcustomproductpagelocalizations-_id_-relationships-searchkeywords.md)
  Unassign a search keyword from a specific custom product page localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcustomproductpagelocalizations-_id_-searchkeywords)*