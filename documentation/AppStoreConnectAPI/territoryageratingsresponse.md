# TerritoryAgeRatingsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of age ratings assigned to an app across App Store territories.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```swift
object TerritoryAgeRatingsResponse
```

## Properties

- `data` ([TerritoryAgeRating]) *(required)*
- `included` ([Territory])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AgeRatingDeclaration](ageratingdeclaration.md)
  A set of content descriptors for your app that App Store Connect uses to assign an age rating.
- [object AgeRatingDeclarationResponse](ageratingdeclarationresponse.md)
  A response containing a single age rating declaration with your app’s content descriptors.
- [object AgeRatingDeclarationUpdateRequest](ageratingdeclarationupdaterequest.md)
  The request body you use to update an Age Rating Declaration.
- [object AppInfoAgeRatingDeclarationLinkageResponse](appinfoageratingdeclarationlinkageresponse.md)
- [object AppInfoTerritoryAgeRatingsLinkagesResponse](appinfoterritoryageratingslinkagesresponse.md)
  A response containing the resource identifiers of territory-specific age ratings for an app info record.
- [type AppStoreAgeRating](appstoreagerating.md)
  A string that represents the app’s age rating as it appears on the App Store for all platforms.
- [type BrazilAgeRating](brazilagerating.md)
  String that represents the app’s age rating as it appears on the App Store in Brazil for all platforms.
- [type KidsAgeBand](kidsageband.md)
  String that represents the age band for a Made for Kids app.
- [object TerritoryAgeRating](territoryagerating.md)
  The data structure that represent a territory age-rating resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/territoryageratingsresponse)*