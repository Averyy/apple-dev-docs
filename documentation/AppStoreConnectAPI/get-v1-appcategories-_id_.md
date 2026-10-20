# Read app category information

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a specific app category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app category resource ID from the [`List app categories`](./get-v1-appcategories.md) response.

### Query Parameters

- `fields[appCategories]` ([string]): Additional fields to include for each app categories resource returned by the response.

  **Allowed Values**: `platforms`, `subcategories`, `parent`
- `include` ([string]): The relationship data to include in the response.

  **Allowed Values**: `subcategories`, `parent`
- `limit[subcategories]` (integer): The maximum number of related subcategories resources to return.

  **Maximum**: `50`

## Responses

- `200` OK (`AppCategoryResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading App Category Information
- [Read the parent information of an app category](./get-v1-appcategories-_id_-parent.md)
  Get the App Store category to which a specific subcategory belongs.
- [Get the parent category ID for an app category](./get-v1-appcategories-_id_-relationships-parent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_)*