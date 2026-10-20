# List all search keywords for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get search keywords for a specific app.

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/searchKeywords`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[appKeywords]` ([string]): Additional fields to include for each app keyword resource returned by the response.
- `filter[locale]` ([string]): Filter the returned app keywords by locale.
- `filter[platform]` ([string]): Filter the returned app keywords by platform.
- `limit` (integer): The maximum number of app keyword resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppKeywordsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Search keywords
- [List search keyword IDs for an app](./get-v1-apps-_id_-relationships-searchkeywords.md)
  Get a list of search keyword IDs for a specific app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-searchkeywords)*