# Get the age rating declaration ID for an app info

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appInfos/{id}/relationships/ageRatingDeclaration`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Responses

- `200` OK (`AppInfoAgeRatingDeclarationLinkageResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Reading and modifying declarations
- [Read the age-rating declaration](./get-v1-appinfos-_id_-ageratingdeclaration.md)
  Get the age-rating declaration for an app info.
- [Modify an age rating declaration](./patch-v1-ageratingdeclarations-_id_.md)
  Provide age-related information so the App Store can determine the age rating for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appinfos-_id_-relationships-ageratingdeclaration)*