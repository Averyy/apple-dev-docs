# List App Tags

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all app tags for a specific app.

**Availability**:
- App Store Connect API 4.1+

## Mentions

- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/appTags`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[appTags]` ([string]): Additional fields to include for each app tag resource returned by the response. Note: `territories` is deprecated; after the relationship is removed, requests that use it return an error.

  **Allowed Values**: `name`, `visibleInAppStore`, `territories`
- `fields[territories]` ([string]): Additional fields to include for each territory resource returned by the response. Note: this parameter is deprecated; after the `territories` relationship is removed, requests that use it return an error.

  **Allowed Values**: `currency`
- `filter[visibleInAppStore]` ([string]): Filter the returned app tags by visibility in the App Store.
- `include` ([string]): The relationship data to include in the response. Note: `territories` is deprecated; after the relationship is removed, requests that include it return an error.

  **Allowed Values**: `territories`
- `limit` (integer): The maximum number of app tag resources to return.

  **Maximum**: `200`
- `limit[territories]` (integer): The maximum number of related territory resources to return. Note: this parameter is deprecated; after the `territories` relationship is removed, requests that use it return an error.

  **Maximum**: `50`
- `sort` ([string]): Attributes by which to sort.

  **Allowed Values**: `name`, `-name`

## Responses

- `200` OK (`AppTagsResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading app tag information
- [List app tags IDs](./get-v1-apps-_id_-relationships-apptags.md)
  List all app tag IDs for a specific app.
- [List territory IDs for an app tag](./get-v1-apptags-_id_-relationships-territories.md)
  List territory IDs for an app tag.
- [List Territories for an App Tag](./get-v1-apptags-_id_-territories.md)
  List territory availability for a specific app tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-apptags)*