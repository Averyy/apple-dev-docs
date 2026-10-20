# AppClipDefaultExperienceCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipDefaultExperienceCreateRequest.Data
```

## Topics

### Objects
- [object AppClipDefaultExperienceCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the Default App Clip Experiences resource.
- [object AppClipDefaultExperienceCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (AppClipDefaultExperienceCreateRequest.Data.Attributes): The attributes that describe the request that creates a Default App Clip Experiences resource.
- `relationships` (AppClipDefaultExperienceCreateRequest.Data.Relationships) *(required)*: The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `appClipDefaultExperiences`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipdefaultexperiencecreaterequest/data-data.dictionary)*