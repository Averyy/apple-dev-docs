# Get the parent category ID for an app category

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appCategories/{id}/relationships/parent`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app category resource ID from the [`List app categories`](./get-v1-appcategories.md) response.

## Responses

- `200` OK (`AppCategoryParentLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading App Category Information
- [Read app category information](./get-v1-appcategories-_id_.md)
  Get a specific app category.
- [Read the parent information of an app category](./get-v1-appcategories-_id_-parent.md)
  Get the App Store category to which a specific subcategory belongs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appcategories-_id_-relationships-parent)*