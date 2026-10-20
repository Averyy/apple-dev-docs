# Get the first secondary subcategory ID for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/relationships/secondarySubcategoryOne`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppInfoSecondarySubcategoryOneLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Subcategories
- [Read the primary subcategory one information of an app info](./get-v1-appinfos-_id_-primarysubcategoryone.md)
  Get the first App Store subcategory within an app’s primary category.
- [Read the primary subcategory two information of an app info](./get-v1-appinfos-_id_-primarysubcategorytwo.md)
  Get the second App Store subcategory within an app’s primary category.
- [Read the secondary subcategory one information of an app info](./get-v1-appinfos-_id_-secondarysubcategoryone.md)
  Get the first App Store subcategory within an app’s secondary category.
- [Read the secondary subcategory two information of an app info](./get-v1-appinfos-_id_-secondarysubcategorytwo.md)
  Get the second App Store subcategory within an app’s secondary category.
- [Get the first primary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-primarysubcategoryone.md)
- [Get the second primary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-primarysubcategorytwo.md)
- [Get the second secondary subcategory ID for an app info](./get-v1-appinfos-_id_-relationships-secondarysubcategorytwo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-relationships-secondarysubcategoryone)*