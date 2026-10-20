# List subcategory IDs for an app category

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}/relationships/subcategories`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app category resource ID from the [`List app categories`](./get-v1-appcategories.md) response.

### Query Parameters

- `limit` (integer): The maximum number of app category resource identifiers to return.

  **Maximum**: `200`

## Responses

- `200` OK (`AppCategorySubcategoriesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Listing Categories and Subcategories
- [List app categories](./get-v1-appcategories.md)
  List all categories on the App Store, including the category and subcategory hierarchy.
- [List all subcategories for an app category](./get-v1-appcategories-_id_-subcategories.md)
  List all App Store subcategories that belong to a specific category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_-relationships-subcategories)*