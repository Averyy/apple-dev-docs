# Read the primary subcategory two information of an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the second App Store subcategory within an app’s primary category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/primarySubcategoryTwo`

## Parameters

- `fields[appCategories]` ([string]): Fields to return for included related types.
- `limit[subcategories]` (integer)
- `include` ([string])

## See Also

- [Read the primary subcategory one information of an app info](get-v1-appinfos-_id_-primarysubcategoryone.md)
  Get the first App Store subcategory within an app’s primary category.
- [Read the secondary subcategory one information of an app info](get-v1-appinfos-_id_-secondarysubcategoryone.md)
  Get the first App Store subcategory within an app’s secondary category.
- [Read the secondary subcategory two information of an app info](get-v1-appinfos-_id_-secondarysubcategorytwo.md)
  Get the second App Store subcategory within an app’s secondary category.
- [Get the first primary subcategory ID for an app info](get-v1-appinfos-_id_-relationships-primarysubcategoryone.md)
- [Get the second primary subcategory ID for an app info](get-v1-appinfos-_id_-relationships-primarysubcategorytwo.md)
- [Get the first secondary subcategory ID for an app info](get-v1-appinfos-_id_-relationships-secondarysubcategoryone.md)
- [Get the second secondary subcategory ID for an app info](get-v1-appinfos-_id_-relationships-secondarysubcategorytwo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-primarysubcategorytwo)*