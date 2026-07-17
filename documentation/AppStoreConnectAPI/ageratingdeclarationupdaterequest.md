# AgeRatingDeclarationUpdateRequest

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update an Age Rating Declaration.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AgeRatingDeclarationUpdateRequest
```

## Mentions

- [App Store Connect API 4.4.1 release notes](app-store-connect-api-4-4-1-release-notes.md)

## Topics

### Objects
- [object AgeRatingDeclarationUpdateRequest.Data](ageratingdeclarationupdaterequest/data-data.dictionary.md)
  The data element of the request body.

## Properties

- `data` (AgeRatingDeclarationUpdateRequest.Data) *(required)*: The data element of the request body.

## See Also

- [object AgeRatingDeclaration](ageratingdeclaration.md)
  A set of content descriptors for your app that App Store Connect uses to assign an age rating.
- [object AgeRatingDeclarationResponse](ageratingdeclarationresponse.md)
  A response containing a single age rating declaration with your app’s content descriptors.
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
- [object TerritoryAgeRatingsResponse](territoryageratingsresponse.md)
  A response containing a list of age ratings assigned to an app across App Store territories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ageratingdeclarationupdaterequest)*