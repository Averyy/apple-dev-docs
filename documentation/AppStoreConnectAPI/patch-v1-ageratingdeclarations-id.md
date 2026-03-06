# Modify an Age Rating Declaration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Provide age-related information so the App Store can determine the age rating for your app.

**Availability**:
- App Store Connect API 1.2+

## Mentions

- [App Store Connect API 3.6 release notes](app-store-connect-api-3-6-release-notes.md)
- [App Store Connect API 4.0 release notes](app-store-connect-api-4-0-release-notes.md)
- [App Store Connect API 4.1 release notes](app-store-connect-api-4-1-release-notes.md)
- [App Store Connect API 4.2 release notes](app-store-connect-api-4-2-release-notes.md)

#### Discussion

Every app store version has an age rating declaration. Use this endpoint to edit the declaration and provide app-characteristic information so App Store Connect can determine the appropriate age rating for the app.

Use this endpoint to indicate whether an app is Made for Kids.

When calling this endpoint, only include the attributes that you’re modifying.

The attributes for age-rating declarations, `INFREQUENT_OR_MILD` and `FREQUENT_OR_INTENSE` are deprecated. Instead, use `INFREQUENT` or `FREQUENT`.

For example, in an app that has a `FREQUENT` declaration for contests, the age rating for the `AppInfos` is 12+. If you declare a value of true for `gambling`, the age rating for the `AppInfos` is 17+.

##### Modify an Age Rating Declaration

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/26b5c300-1814-4b7a-8ec9-5411ecf36305

{
  "data": {
    "type": "ageRatingDeclarations",
    "id": "string",
    "attributes": {
      "alcoholTobaccoOrDrugUseOrReferences": "NONE",
      "contests": "NONE",
      "gambling": true,
      "gamblingSimulated": "NONE",
      "medicalOrTreatmentInformation": "NONE",
      "profanityOrCrudeHumor": "NONE",
      "sexualContentGraphicAndNudity": "NONE",
      "sexualContentOrNudity": "NONE",
      "horrorOrFearThemes": "NONE",
      "matureOrSuggestiveThemes": "NONE",
      "unrestrictedWebAccess": true,
      "violenceCartoonOrFantasy": "NONE",
      "violenceRealisticProlongedGraphicOrSadistic": "NONE",
      "violenceRealistic": "NONE",
      "kidsAgeBand": null
    }
  }
}

```

**Response**:

```json
{
  "data": {
    "type": "ageRatingDeclarations",
    "id": "26b5c300-1814-4b7a-8ec9-5411ecf36305",
    "attributes": {
      "alcoholTobaccoOrDrugUseOrReferences": "NONE",
      "contests": "NONE",
      "gambling": true,
      "gamblingSimulated": "NONE",
      "medicalOrTreatmentInformation": "NONE",
      "profanityOrCrudeHumor": "NONE",
      "sexualContentGraphicAndNudity": "NONE",
      "sexualContentOrNudity": "NONE",
      "horrorOrFearThemes": "NONE",
      "matureOrSuggestiveThemes": "NONE",
      "unrestrictedWebAccess": true,
      "violenceCartoonOrFantasy": "NONE",
      "violenceRealisticProlongedGraphicOrSadistic": "NONE",
      "violenceRealistic": "NONE",
      "kidsAgeBand": null
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/26b5c300-1814-4b7a-8ec9-5411ecf36305"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/26b5c300-1814-4b7a-8ec9-5411ecf36305"
  }
}

```

##### Mark an App As Made for Kids

**Request**:

```None
PATCH https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/26b5c300-1814-4b7a-8ec9-5411ecf36305

{
  "data": {
    "type": "ageRatingDeclarations",
    "id": "string",
    "attributes": {
      "kidsAgeBand": "FIVE_AND_UNDER"
    }
  }
}
```

**Response**:

```json
{
  "data": {
    "type": "ageRatingDeclarations",
    "id": "26b5c300-1814-4b7a-8ec9-5411ecf36305",
    "attributes": {
      "alcoholTobaccoOrDrugUseOrReferences": "NONE",
      "contests": “NONE”,
      “gamblingAndContests”: false,
      "gambling": false,
      "gamblingSimulated": "NONE",
      "medicalOrTreatmentInformation": "NONE",
      "profanityOrCrudeHumor": "NONE",
      "sexualContentGraphicAndNudity": "NONE",
      "sexualContentOrNudity": "NONE",
      "horrorOrFearThemes": "NONE",
      "matureOrSuggestiveThemes": "NONE",
      "unrestrictedWebAccess": true,
      "violenceCartoonOrFantasy": "NONE",
      "violenceRealisticProlongedGraphicOrSadistic": "NONE",
      "violenceRealistic": "NONE",
      "kidsAgeBand": "FIVE_AND_UNDER"
    },
    "links": {
      "self": "https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/26b5c300-1814-4b7a-8ec9-5411ecf36305"
    }
  },
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/26b5c300-1814-4b7a-8ec9-5411ecf36305"
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/ageRatingDeclarations/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.

## Request Body

The request body you use to update an Age Rating Declaration.

## See Also

- [Read age rating declaration](get-v1-appinfos-_id_-ageratingdeclaration.md)
  Get the age rating declaration for the app info.
- [GET /v1/appInfos/{id}/relationships/ageRatingDeclaration](get-v1-appinfos-_id_-relationships-ageratingdeclaration.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-ageratingdeclarations-_id_)*