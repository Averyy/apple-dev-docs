# BetaAppLocalizationCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object BetaAppLocalizationCreateRequest.Data
```

## Topics

### Objects
- [object BetaAppLocalizationCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.
- [object BetaAppLocalizationCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (BetaAppLocalizationCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (BetaAppLocalizationCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaAppLocalizations`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betaapplocalizationcreaterequest/data-data.dictionary)*