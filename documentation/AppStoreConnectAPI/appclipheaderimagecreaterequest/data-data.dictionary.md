# AppClipHeaderImageCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object AppClipHeaderImageCreateRequest.Data
```

## Topics

### Objects
- [object AppClipHeaderImageCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new App Clip Header Images resource.
- [object AppClipHeaderImageCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (AppClipHeaderImageCreateRequest.Data.Attributes) *(required)*: The attributes that describes the request that creates an App Clip Header Images resource.
- `relationships` (AppClipHeaderImageCreateRequest.Data.Relationships) *(required)*: The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `appClipHeaderImages`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appclipheaderimagecreaterequest/data-data.dictionary)*