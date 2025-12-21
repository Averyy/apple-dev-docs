# App Categories

**Framework**: App Store Connect API

Get App Store categories and subcategories for apps.

#### Overview

`appCategories` provides read-only information that includes the list of choices for an app’s App Store category, subcategory, and secondary category.

To update your app’s categories, use the [`App Infos`](app-infos.md) resource. For more information about categories, see [`Choosing a Category`](https://developer.apple.comhttps://developer.apple.com/app-store/categories/).

## Topics

### Listing Categories and Subcategories
- [List App Categories](get-v1-appcategories.md)
  List all categories on the App Store, including the category and subcategory hierarchy.
- [List All Subcategories for an App Category](get-v1-appcategories-_id_-subcategories.md)
  List all App Store subcategories that belong to a specific category.
- [GET /v1/appCategories/{id}/relationships/subcategories](get-v1-appcategories-_id_-relationships-subcategories.md)
### Reading App Category Information
- [Read App Category Information](get-v1-appcategories-_id_.md)
  Get a specific app category.
- [Read the Parent Information of an App Category](get-v1-appcategories-_id_-parent.md)
  Get the App Store category to which a specific subcategory belongs.
- [GET /v1/appCategories/{id}/relationships/parent](get-v1-appcategories-_id_-relationships-parent.md)
### Objects
- [object AppCategoriesResponse](appcategoriesresponse.md)
  A response that contains a list of App Category resources.
- [object AppCategory](appcategory.md)
  The data structure that represent an App Categories resource.
- [object AppCategoryResponse](appcategoryresponse.md)
  A response that contains a single App Categories resource.
- [object AppCategoriesWithoutIncludesResponse](appcategorieswithoutincludesresponse.md)
- [object AppCategoryWithoutIncludesResponse](appcategorywithoutincludesresponse.md)
- [object AppInfoPrimaryCategoryLinkageResponse](appinfoprimarycategorylinkageresponse.md)
- [object AppInfoPrimarySubcategoryOneLinkageResponse](appinfoprimarysubcategoryonelinkageresponse.md)
- [object AppInfoPrimarySubcategoryTwoLinkageResponse](appinfoprimarysubcategorytwolinkageresponse.md)
- [object AppInfoSecondaryCategoryLinkageResponse](appinfosecondarycategorylinkageresponse.md)
- [object AppInfoSecondarySubcategoryOneLinkageResponse](appinfosecondarysubcategoryonelinkageresponse.md)
- [object AppInfoSecondarySubcategoryTwoLinkageResponse](appinfosecondarysubcategorytwolinkageresponse.md)

## See Also

- [Age Ratings](age-ratings.md)
  Read and update age ratings and declarations for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-categories)*