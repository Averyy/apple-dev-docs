# Read the age-rating declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the age-rating declaration for an app info.

**Availability**:
- App Store Connect API 1.4+

## Mentions

- [App Store Connect API 4.0 release notes](./app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.3 release notes](./app-store-connect-api-4-3-release-notes.md)
- [App Store Connect API 4.4 release notes](./app-store-connect-api-4-4-release-notes.md)

## Discussion

Responses for this endpoint include `contests` or `gambling` properties. In an app that has a `FREQUENT_OR_INTENSE` declaration for contests, the age rating for the `AppInfos` is 12+. If you declare a value of true for `gambling`, the age rating for the `AppInfos` is 17+.

### Read the age-rating declaration

**Request**:

```
GET https://api.appstoreconnect.apple.com/v1/appInfos/994af4c0-ff6c-fdb9-e053-d23ab111187e/ageRatingDeclaration
```

**Response**:

```json
{
  "data": {
    "type": "ageRatingDeclarations",
    "id": "994af4c0-ff6c-fdb9-e053-d23ab111187e",
    "attributes": {
      "alcoholTobaccoOrDrugUseOrReferences": "NONE",
      "contests": "FREQUENT_OR_INTENSE",
      "gambling": false,
      "gamblingSimulated": "NONE",
      "kidsAgeBand": null,
      "medicalOrTreatmentInformation": "NONE",
      "profanityOrCrudeHumor": "NONE",
      "sexualContentGraphicAndNudity": "NONE",
      "sexualContentOrNudity": "NONE",
      "horrorOrFearThemes": "NONE",
      "matureOrSuggestiveThemes": "NONE",
      "unrestrictedWebAccess": false,
      "violenceCartoonOrFantasy": "NONE",
      "violenceRealisticProlongedGraphicOrSadistic": "NONE",
      "violenceRealistic": "NONE"
    },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/994af4c0-ff6c-fdb9-e053-d23ab111187e"
  }
},
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/appInfos/994af4c0-ff6c-fdb9-e053-d23ab111187e/ageRatingDeclaration"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/ageRatingDeclaration`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `appInfo` resource ID from the [`List all app infos for an app`](./get-v1-apps-_id_-appinfos.md) response.

### Query Parameters

- `fields[ageRatingDeclarations]` ([string]): Additional fields to include for each age-rating declaration resource that the response returns.

  **Allowed Values**: `advertising`, `alcoholTobaccoOrDrugUseOrReferences`, `contests`, `gambling`, `gamblingSimulated`, `gunsOrOtherWeapons`, `healthOrWellnessTopics`, `kidsAgeBand`, `lootBox`, `medicalOrTreatmentInformation`, `messagingAndChat`, `parentalControls`, `profanityOrCrudeHumor`, `ageAssurance`, `sexualContentGraphicAndNudity`, `sexualContentOrNudity`, `socialMedia`, `socialMediaAgeRestricted`, `horrorOrFearThemes`, `matureOrSuggestiveThemes`, `unrestrictedWebAccess`, `userGeneratedContent`, `violenceCartoonOrFantasy`, `violenceRealisticProlongedGraphicOrSadistic`, `violenceRealistic`, `ageRatingOverride`, `ageRatingOverrideV2`, `koreaAgeRatingOverride`, `gracRatingClassificationNumber`, `developerAgeRatingInfoUrl`

## Responses

- `200` OK (`AgeRatingDeclarationResponse`, `application/json`): The request completed successfully.
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Authentication failed.
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and modifying declarations
- [Get the age rating declaration ID for an app info](./get-v1-appinfos-_id_-relationships-ageratingdeclaration.md)
- [Modify an age rating declaration](./patch-v1-ageratingdeclarations-_id_.md)
  Provide age-related information so the App Store can determine the age rating for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-ageratingdeclaration)*