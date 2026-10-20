# AppClipAdvancedExperienceUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipAdvancedExperienceUpdateRequest.Data
```

## Topics

### Objects
- [object AppClipAdvancedExperienceUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the Advanced App Clip Experiences resource.
- [object AppClipAdvancedExperienceUpdateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (AppClipAdvancedExperienceUpdateRequest.Data.Attributes): The attributes that describe the request that updates an Advanced App Clip Experiences resource.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the request.
- `relationships` (AppClipAdvancedExperienceUpdateRequest.Data.Relationships): The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `appClipAdvancedExperiences`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipadvancedexperienceupdaterequest/data-data.dictionary)*