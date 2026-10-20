# List all subcategories for an app category

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

List all App Store subcategories that belong to a specific category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}/subcategories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app category resource ID from the [`List app categories`](./get-v1-appcategories.md) response.

### Query Parameters

- `fields[appCategories]` ([string]): Additional fields to include for each app categories resource returned by the response.

  **Allowed Values**: `platforms`, `subcategories`, `parent`
- `limit` (integer): The maximum number of app categories resources to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppCategoriesWithoutIncludesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing Categories and Subcategories
- [List app categories](./get-v1-appcategories.md)
  List all categories on the App Store, including the category and subcategory hierarchy.
- [List subcategory IDs for an app category](./get-v1-appcategories-_id_-relationships-subcategories.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_-subcategories)*