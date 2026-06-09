# List all search keywords for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get search keywords for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/searchKeywords`

## Parameters

- `fields[appKeywords]` ([string]): Additional fields to include for each app keyword resource returned by the response.
- `filter[locale]` ([string]): Filter the returned app keywords by locale.
- `filter[platform]` ([string]): Filter the returned app keywords by platform.
- `limit` (integer): The maximum number of app keyword resources to return.

## See Also

- [List search keyword IDs for an app](get-v1-apps-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-searchkeywords)*