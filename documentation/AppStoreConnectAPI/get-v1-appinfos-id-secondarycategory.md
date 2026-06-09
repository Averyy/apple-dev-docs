# Read the secondary category information of an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get an app’s secondary App Store category.

**Availability**:
- App Store Connect API 1.2+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/secondaryCategory`

## Parameters

- `fields[appCategories]` ([string]): Fields to return for included related types.
- `limit[subcategories]` (integer)
- `include` ([string])

## See Also

- [Read the primary category information of an app info](get-v1-appinfos-_id_-primarycategory.md)
  Get an app’s primary App Store category.
- [Get the primary category ID for an app info](get-v1-appinfos-_id_-relationships-primarycategory.md)
- [Get the secondary category ID for an app info](get-v1-appinfos-_id_-relationships-secondarycategory.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-secondarycategory)*