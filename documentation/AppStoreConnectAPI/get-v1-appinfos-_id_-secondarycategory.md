# Read the secondary category information of an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get an app’s secondary App Store category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/secondaryCategory`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

### Query Parameters

- `fields[appCategories]` ([string]): Fields to return for included related types.

  **Allowed Values**: `platforms`, `subcategories`, `parent`
- `limit[subcategories]` (integer): **Maximum**: `50`
- `include` ([string]): **Allowed Values**: `subcategories`, `parent`

## Responses

- `200` OK (`AppCategoryResponse`, `application/json`): Request succeeded.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Categories
- [Read the primary category information of an app info](./get-v1-appinfos-_id_-primarycategory.md)
  Get an app’s primary App Store category.
- [Get the primary category ID for an app info](./get-v1-appinfos-_id_-relationships-primarycategory.md)
- [Get the secondary category ID for an app info](./get-v1-appinfos-_id_-relationships-secondarycategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-secondarycategory)*