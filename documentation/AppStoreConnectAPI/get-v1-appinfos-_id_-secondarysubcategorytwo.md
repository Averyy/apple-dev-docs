# Read the secondary subcategory two information of an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the second App Store subcategory within an app’s secondary category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/secondarySubcategoryTwo`

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

### Reading Subcategories
- [Read the primary subcategory one information of an app info](./get-v1-appinfos-_id_-primarysubcategoryone.md)
  Get the first App Store subcategory within an app’s primary category.
- [Read the primary subcategory two information of an app info](./get-v1-appinfos-_id_-primarysubcategorytwo.md)
  Get the second App Store subcategory within an app’s primary category.
- [Read the secondary subcategory one information of an app info](./get-v1-appinfos-_id_-secondarysubcategoryone.md)
  Get the first App Store subcategory within an app’s secondary category.
- [Get the first primary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-primarysubcategoryone.md)
- [Get the second primary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-primarysubcategorytwo.md)
- [Get the first secondary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-secondarysubcategoryone.md)
- [Get the second secondary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-secondarysubcategorytwo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-secondarysubcategorytwo)*