# AgeRatingDeclarationUpdateRequest.Data.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes whose values you’re changing as part of the update request.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```
object AgeRatingDeclarationUpdateRequest.Data.Attributes
```

## Mentions

- [App Store Connect API 3.6 release notes](../../app-store-connect-api-3-6-release-notes.md)

## Discussion

For more information about app ratings, see [App ratings](https://help.apple.com/app-store-connect/#/dev269f11291).

## Properties

- `advertising` (boolean): A Boolean value that indicates whether the app contains advertising.
- `alcoholTobaccoOrDrugUseOrReferences` (string): Declaration for alcohol, tobacco, or drug use.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `contests` (string): Declaration for contests.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `gambling` (boolean): Declaration for gambling, provided as a Boolean value.
- `gamblingSimulated` (string): Declaration for simulated gambling.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `gunsOrOtherWeapons` (string): Declaration for guns or other weapons. Allowed values are NONE, INFREQUENT_OR_MILD, FREQUENT_OR_INTENSE, INFREQUENT, and FREQUENT.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `healthOrWellnessTopics` (boolean): A Boolean value that indicates whether the app contains health or wellness topics.
- `kidsAgeBand` (KidsAgeBand): Declaration for the Kids Age Band value.
- `lootBox` (boolean): A Boolean value that indicates whether the app contains loot boxes or other randomized virtual item mechanics.
- `medicalOrTreatmentInformation` (string): Declaration for medical or treatment-focused content.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `messagingAndChat` (boolean): A Boolean value that indicates whether the app includes messaging or chat functionality.
- `parentalControls` (boolean): A Boolean value that indicates whether the app offers parental controls.
- `profanityOrCrudeHumor` (string): Declaration for profanity or crude humor.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `ageAssurance` (boolean): A Boolean value that indicates whether the app uses age assurance to verify a person’s age.
- `sexualContentGraphicAndNudity` (string): Declaration for graphic sexual content and nudity.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `sexualContentOrNudity` (string): Declaration for sexual content or nudity.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `socialMedia` (boolean): A Boolean value that indicates whether the app includes social media features.
- `socialMediaAgeRestricted` (boolean): A Boolean value that indicates whether the app’s social media features are age restricted.
- `horrorOrFearThemes` (string): Declaration for horror or fear themed content.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `matureOrSuggestiveThemes` (string): Declaration for mature or suggestive themes.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `unrestrictedWebAccess` (boolean): Declaration for unrestricted web access, such as with an embedded browser, provided as a Boolean value.
- `userGeneratedContent` (boolean): A Boolean value that indicates whether the app includes user-generated content.
- `violenceCartoonOrFantasy` (string): Declaration for cartoon or fantasy violence.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `violenceRealisticProlongedGraphicOrSadistic` (string): Declaration for prolonged realistic or sadistic violence.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `violenceRealistic` (string): Declaration for realistic violence.

  **Allowed Values**: `NONE`, `INFREQUENT_OR_MILD`, `FREQUENT_OR_INTENSE`, `INFREQUENT`, `FREQUENT`
- `ageRatingOverride` (string) *(deprecated)*: An override you set for the app’s calculated age rating. Allowed values are NONE, NINE_PLUS, THIRTEEN_PLUS, SIXTEEN_PLUS, SEVENTEEN_PLUS, and UNRATED. This attribute is deprecated; use ageRatingOverrideV2 instead.

  **Allowed Values**: `NONE`, `NINE_PLUS`, `THIRTEEN_PLUS`, `SIXTEEN_PLUS`, `SEVENTEEN_PLUS`, `UNRATED`
- `ageRatingOverrideV2` (string): An override you set for the app’s calculated age rating. Allowed values are NONE, NINE_PLUS, THIRTEEN_PLUS, SIXTEEN_PLUS, EIGHTEEN_PLUS, and UNRATED.

  **Allowed Values**: `NONE`, `NINE_PLUS`, `THIRTEEN_PLUS`, `SIXTEEN_PLUS`, `EIGHTEEN_PLUS`, `UNRATED`
- `koreaAgeRatingOverride` (string): An override you set for the app’s calculated age rating in Korea.

  **Allowed Values**: `NONE`, `ALL`, `TWELVE_PLUS`, `FIFTEEN_PLUS`, `NINETEEN_PLUS`
- `gracRatingClassificationNumber` (string): The rating classification number provided by Game Rating and Administration Committee (GRAC). To learn more, see the [Game Rating and Administration Committee](https://www.gcrb.or.kr) website.
- `developerAgeRatingInfoUrl` (uri): The URL where people can find more information about how you determine the app’s age rating.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ageratingdeclarationupdaterequest/data-data.dictionary/attributes-data.dictionary)*