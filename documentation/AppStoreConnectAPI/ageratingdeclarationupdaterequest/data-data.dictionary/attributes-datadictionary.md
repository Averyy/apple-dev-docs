# AgeRatingDeclarationUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes whose values you’re changing as part of the update request.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AgeRatingDeclarationUpdateRequest.Data.Attributes
```

## Mentions

- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)

#### Discussion

For more information about app ratings, see [`App ratings`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/dev269f11291).

## Properties

- `advertising` (boolean): A Boolean value that indicates whether the app contains advertising.
- `alcoholTobaccoOrDrugUseOrReferences` (string): Declaration for alcohol, tobacco, or drug use.
- `contests` (string): Declaration for contests.
- `gambling` (boolean): Declaration for gambling, provided as a Boolean value.
- `gamblingSimulated` (string): Declaration for simulated gambling.
- `gunsOrOtherWeapons` (string): Declaration for guns or other weapons. Allowed values are NONE, INFREQUENT_OR_MILD, FREQUENT_OR_INTENSE, INFREQUENT, and FREQUENT.
- `healthOrWellnessTopics` (boolean): A Boolean value that indicates whether the app contains health or wellness topics.
- `kidsAgeBand` (KidsAgeBand): Declaration for the Kids Age Band value.
- `lootBox` (boolean): A Boolean value that indicates whether the app contains loot boxes or other randomized virtual item mechanics.
- `medicalOrTreatmentInformation` (string): Declaration for medical or treatment-focused content.
- `messagingAndChat` (boolean): A Boolean value that indicates whether the app includes messaging or chat functionality.
- `parentalControls` (boolean): A Boolean value that indicates whether the app offers parental controls.
- `profanityOrCrudeHumor` (string): Declaration for profanity or crude humor.
- `ageAssurance` (boolean): A Boolean value that indicates whether the app uses age assurance to verify a person’s age.
- `sexualContentGraphicAndNudity` (string): Declaration for graphic sexual content and nudity.
- `sexualContentOrNudity` (string): Declaration for sexual content or nudity.
- `socialMedia` (boolean): A Boolean value that indicates whether the app includes social media features.
- `socialMediaAgeRestricted` (boolean): A Boolean value that indicates whether the app’s social media features are age restricted.
- `horrorOrFearThemes` (string): Declaration for horror or fear themed content.
- `matureOrSuggestiveThemes` (string): Declaration for mature or suggestive themes.
- `unrestrictedWebAccess` (boolean): Declaration for unrestricted web access, such as with an embedded browser, provided as a Boolean value.
- `userGeneratedContent` (boolean): A Boolean value that indicates whether the app includes user-generated content.
- `violenceCartoonOrFantasy` (string): Declaration for cartoon or fantasy violence.
- `violenceRealisticProlongedGraphicOrSadistic` (string): Declaration for prolonged realistic or sadistic violence.
- `violenceRealistic` (string): Declaration for realistic violence.
- `ageRatingOverride` (string): An override you set for the app’s calculated age rating. Allowed values are NONE, NINE_PLUS, THIRTEEN_PLUS, SIXTEEN_PLUS, SEVENTEEN_PLUS, and UNRATED. This attribute is deprecated; use ageRatingOverrideV2 instead.
- `ageRatingOverrideV2` (string): An override you set for the app’s calculated age rating. Allowed values are NONE, NINE_PLUS, THIRTEEN_PLUS, SIXTEEN_PLUS, EIGHTEEN_PLUS, and UNRATED.
- `koreaAgeRatingOverride` (string): An override you set for the app’s calculated age rating in Korea. Allowed values are NONE, FIFTEEN_PLUS, and NINETEEN_PLUS.
- `developerAgeRatingInfoUrl` (uri): The URL where people can find more information about how you determine the app’s age rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ageratingdeclarationupdaterequest/data-data.dictionary/attributes-data.dictionary)*