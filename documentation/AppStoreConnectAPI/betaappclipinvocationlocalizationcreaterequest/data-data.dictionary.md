# BetaAppClipInvocationLocalizationCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.6+

## Declaration

```
object BetaAppClipInvocationLocalizationCreateRequest.Data
```

## Topics

### Objects
- [object BetaAppClipInvocationLocalizationCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new Beta App Clip Invocation Localizations resource.
- [object BetaAppClipInvocationLocalizationCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (BetaAppClipInvocationLocalizationCreateRequest.Data.Attributes) *(required)*: The attributes that describes the request that creates a Beta App Clip Invocation Localizations resource.
- `relationships` (BetaAppClipInvocationLocalizationCreateRequest.Data.Relationships) *(required)*: The navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaAppClipInvocationLocalizations`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaappclipinvocationlocalizationcreaterequest/data-data.dictionary)*