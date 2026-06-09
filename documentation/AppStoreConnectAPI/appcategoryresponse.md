# AppCategoryResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that read a single App Store category.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppCategoryResponse
```

## Properties

- `data` (AppCategory) *(required)*
- `included` ([AppCategory])
- `links` (DocumentLinks) *(required)*

## See Also

- [object AppCategoriesResponse](appcategoriesresponse.md)
  The response body for endpoints that list App Store categories.
- [object AppCategory](appcategory.md)
  The data structure that represent an App Categories resource.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcategoryresponse)*