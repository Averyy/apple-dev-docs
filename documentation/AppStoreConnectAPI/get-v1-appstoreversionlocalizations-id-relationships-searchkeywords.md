# List search keyword IDs for an app store version localization

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of search keyword IDs for a specific App Store version localization.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appStoreVersionLocalizations/{id}/relationships/searchKeywords`

## Parameters

- `limit` (integer): The maximum number of app keyword resource identifiers to return.

## See Also

- [List all search keywords for an app store version localization](get-v1-appstoreversionlocalizations-_id_-searchkeywords.md)
  Get search keywords for a specific App Store version localization.
- [Add search keywords to an app store version localization](post-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Add search keywords to a specific App Store version localization.
- [Remove search keywords from an app store version localization](delete-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords.md)
  Remove search keywords from a specific App Store version localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appstoreversionlocalizations-_id_-relationships-searchkeywords)*