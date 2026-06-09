# AppCategoriesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list App Store categories.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppCategoriesResponse
```

## Properties

- `data` ([AppCategory]) *(required)*
- `included` ([AppCategory])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppCategory](appcategory.md)
  The data structure that represent an App Categories resource.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appcategoriesresponse)*