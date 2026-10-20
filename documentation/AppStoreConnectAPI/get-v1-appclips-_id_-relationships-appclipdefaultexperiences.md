# List default experience IDs for an App Clip

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

**Availability**:
- App Store Connect API 4.0+

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/appClips/{id}/relationships/appClipDefaultExperiences`

## Parameters

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `limit` (integer): **Maximum**: `200`

## Responses

- `200` OK (`AppClipAppClipDefaultExperiencesLinkagesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting App Clip Experiences
- [List all default app clip experiences for an app clip](./get-v1-appclips-_id_-appclipdefaultexperiences.md)
  Get all default App Clip experiences for an App Clip.
- [List all advanced app clip experiences for an app clip](./get-v1-appclips-_id_-appclipadvancedexperiences.md)
  Get all advanced App Clip experiences for an App Clip.
- [List App Clip advanced experience IDs for an App Clip](./get-v1-appclips-_id_-relationships-appclipadvancedexperiences.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-appclips-_id_-relationships-appclipdefaultexperiences)*