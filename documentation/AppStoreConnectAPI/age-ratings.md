# Age Ratings

**Framework**: App Store Connect API

Read and update age ratings and declarations for your app.

#### Overview

`ageRatingDeclarations` handles your answers to the app-characteristic questions that affect your app’s age rating. This resource enables you to answer the questions and update your answers. You must fill out this information before submitting your app for review.

`territoryAgeRatings` allows you to read the age ratings per territory that are calculated by your age rating declaration responses.

For more information about age ratings, see [`Set an app age rating`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/manage-app-information/set-an-app-age-rating).

> ❗ **Important**: The age-rating declaration attributes `INFREQUENT_OR_MILD` and `FREQUENT_OR_INTENSE` are deprecated. Instead, use `INFREQUENT` or `FREQUENT`.

## Topics

### Reading and modifying declarations
- [Read age rating declaration](get-v1-appinfos-_id_-ageratingdeclaration.md)
  Get the age rating declaration for the app info.
- [GET /v1/appInfos/{id}/relationships/ageRatingDeclaration](get-v1-appinfos-_id_-relationships-ageratingdeclaration.md)
- [Modify an Age Rating Declaration](patch-v1-ageratingdeclarations-_id_.md)
  Provide age-related information so the App Store can determine the age rating for your app.
### Reading territory age rating
- [List territory age ratings for an app info](get-v1-appinfos-_id_-territoryageratings.md)
  List all territory age ratings for a specific app info.
- [List territory age rating Ids for an app info](get-v1-appinfos-_id_-relationships-territoryageratings.md)
  List all territory age rating IDs for a specific app info.
### Objects and data types
- [object AgeRatingDeclaration](ageratingdeclaration.md)
  The data structure that represents an Age Rating Declarations resource.
- [object AgeRatingDeclarationResponse](ageratingdeclarationresponse.md)
  A response that contains a single Age Rating Declarations resource.
- [object AgeRatingDeclarationUpdateRequest](ageratingdeclarationupdaterequest.md)
  The request body you use to update an Age Rating Declaration.
- [object AgeRatingDeclarationWithoutIncludesResponse](ageratingdeclarationwithoutincludesresponse.md)
- [object AppInfoAgeRatingDeclarationLinkageResponse](appinfoageratingdeclarationlinkageresponse.md)
- [object AppInfoTerritoryAgeRatingsLinkagesResponse](appinfoterritoryageratingslinkagesresponse.md)
- [type AppStoreAgeRating](appstoreagerating.md)
  String that represents the app’s age rating as it appears on the App Store for all platforms.
- [type BrazilAgeRating](brazilagerating.md)
  String that represents the app’s age rating as it appears on the App Store in Brazil for all platforms.
- [type KidsAgeBand](kidsageband.md)
  String that represents a Made for Kids app’s age band.
- [object TerritoryAgeRating](territoryagerating.md)
  The data structure that represent a territory age-rating resource.
- [object TerritoryAgeRatingsResponse](territoryageratingsresponse.md)
  A response that contains a list of territory age-rating resources.

## See Also

- [App Categories](app-categories.md)
  Get App Store categories and subcategories for apps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/age-ratings)*