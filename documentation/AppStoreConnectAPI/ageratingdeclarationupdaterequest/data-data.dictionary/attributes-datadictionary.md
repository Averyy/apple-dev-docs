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

- `alcoholTobaccoOrDrugUseOrReferences` (string): Declaration for alcohol, tobacco, or drug use.
- `kidsAgeBand` (KidsAgeBand): Declaration for the Kids Age Band value.
- `medicalOrTreatmentInformation` (string): Declaration for medical or treatment-focused content.
- `profanityOrCrudeHumor` (string): Declaration for profanity or crude humor.
- `sexualContentOrNudity` (string): Declaration for sexual content or nudity.
- `unrestrictedWebAccess` (boolean): Declaration for unrestricted web access, such as with an embedded browser, provided as a Boolean value.
- `gamblingSimulated` (string): Declaration for simulated gambling.
- `horrorOrFearThemes` (string): Declaration for horror or fear themed content.
- `matureOrSuggestiveThemes` (string): Declaration for mature or suggestive themes.
- `sexualContentGraphicAndNudity` (string): Declaration for graphic sexual content and nudity.
- `violenceCartoonOrFantasy` (string): Declaration for cartoon or fantasy violence.
- `violenceRealistic` (string): Declaration for realistic violence.
- `violenceRealisticProlongedGraphicOrSadistic` (string): Declaration for prolonged realistic or sadistic violence.
- `contests` (string): Declaration for contests.
- `gambling` (boolean): Declaration for gambling, provided as a Boolean value.
- `ageRatingOverride` (string)
- `advertising` (boolean)
- `ageAssurance` (boolean)
- `ageRatingOverrideV2` (string)
- `developerAgeRatingInfoUrl` (uri)
- `gunsOrOtherWeapons` (string)
- `healthOrWellnessTopics` (boolean)
- `koreaAgeRatingOverride` (string)
- `lootBox` (boolean)
- `messagingAndChat` (boolean)
- `parentalControls` (boolean)
- `userGeneratedContent` (boolean)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ageratingdeclarationupdaterequest/data-data.dictionary/attributes-data.dictionary)*