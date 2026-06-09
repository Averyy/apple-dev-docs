# Read the age-rating declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the age-rating declaration for an app info.

**Availability**:
- App Store Connect API 1.4+

## Mentions

- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.3 release notes](app-store-connect-api-4-3-release-notes.md)
- [App Store Connect API 4.4 release notes](app-store-connect-api-4-4-release-notes.md)

#### Discussion

Responses for this endpoint include `contests` or `gambling` properties. In an app that has a `FREQUENT_OR_INTENSE` declaration for contests, the age rating for the `AppInfos` is 12+. If you declare a value of true for `gambling`, the age rating for the `AppInfos` is 17+.

##### Read the Age Rating Declaration

**Request**:

```None
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

- `fields[ageRatingDeclarations]` ([string]): Additional fields to include for each age-rating declaration resource that the response returns.

## See Also

- [Get the age rating declaration ID for an app info](get-v1-appinfos-_id_-relationships-ageratingdeclaration.md)
- [Modify an age rating declaration](patch-v1-ageratingdeclarations-_id_.md)
  Provide age-related information so the App Store can determine the age rating for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-ageratingdeclaration)*