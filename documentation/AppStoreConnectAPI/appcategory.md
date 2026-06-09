# AppCategory

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Categories resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppCategory
```

## Topics

### Objects
- [object AppCategory.Attributes](appcategory/attributes-data.dictionary.md)
  Attributes that describe an App Categories resource.
- [object AppCategory.Relationships](appcategory/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppCategory.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppCategory.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppCategoriesResponse](appcategoriesresponse.md)
  The response body for endpoints that list App Store categories.
- [object AppCategoryResponse](appcategoryresponse.md)
  The response body for endpoints that read a single App Store category.
- [object AppCategoriesWithoutIncludesResponse](appcategorieswithoutincludesresponse.md)
  A response containing a list of App Store categories, without including subcategory resources.
- [object AppCategoryWithoutIncludesResponse](appcategorywithoutincludesresponse.md)
  A response containing a single App Store category, without including subcategory resources.
- [object AppInfoPrimaryCategoryLinkageResponse](appinfoprimarycategorylinkageresponse.md)
- [object AppInfoPrimarySubcategoryOneLinkageResponse](appinfoprimarysubcategoryonelinkageresponse.md)
- [object AppInfoPrimarySubcategoryTwoLinkageResponse](appinfoprimarysubcategorytwolinkageresponse.md)
- [object AppInfoSecondaryCategoryLinkageResponse](appinfosecondarycategorylinkageresponse.md)
- [object AppInfoSecondarySubcategoryOneLinkageResponse](appinfosecondarysubcategoryonelinkageresponse.md)
- [object AppInfoSecondarySubcategoryTwoLinkageResponse](appinfosecondarysubcategorytwolinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcategory)*