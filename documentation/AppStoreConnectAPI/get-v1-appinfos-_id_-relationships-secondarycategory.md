# Get the secondary category ID for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/relationships/secondaryCategory`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppInfoSecondaryCategoryLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading Categories
- [Read the primary category information of an app info](./get-v1-appinfos-_id_-primarycategory.md)
  Get an app’s primary App Store category.
- [Read the secondary category information of an app info](./get-v1-appinfos-_id_-secondarycategory.md)
  Get an app’s secondary App Store category.
- [Get the primary category ID for an app info](./get-v1-appinfos-_id_-relationships-primarycategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-relationships-secondarycategory)*