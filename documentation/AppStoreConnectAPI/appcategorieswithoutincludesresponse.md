# AppCategoriesWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of App Store categories, without including subcategory resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```swift
object AppCategoriesWithoutIncludesResponse
```

## Properties

- `data` ([AppCategory]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppCategoriesResponse](appcategoriesresponse.md)
  The response body for endpoints that list App Store categories.
- [object AppCategory](appcategory.md)
  The data structure that represent an App Categories resource.
- [object AppCategoryResponse](appcategoryresponse.md)
  The response body for endpoints that read a single App Store category.
- [object AppCategoryWithoutIncludesResponse](appcategorywithoutincludesresponse.md)
  A response containing a single App Store category, without including subcategory resources.
- [object AppInfoPrimaryCategoryLinkageResponse](appinfoprimarycategorylinkageresponse.md)
- [object AppInfoPrimarySubcategoryOneLinkageResponse](appinfoprimarysubcategoryonelinkageresponse.md)
- [object AppInfoPrimarySubcategoryTwoLinkageResponse](appinfoprimarysubcategorytwolinkageresponse.md)
- [object AppInfoSecondaryCategoryLinkageResponse](appinfosecondarycategorylinkageresponse.md)
- [object AppInfoSecondarySubcategoryOneLinkageResponse](appinfosecondarysubcategoryonelinkageresponse.md)
- [object AppInfoSecondarySubcategoryTwoLinkageResponse](appinfosecondarysubcategorytwolinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcategorieswithoutincludesresponse)*