# RetentionMessageLocalizationCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageLocalizationCreateRequest.Data
```

## Topics

### Objects
- [object RetentionMessageLocalizationCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.
- [object RetentionMessageLocalizationCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionMessageLocalizations`
- `attributes` (RetentionMessageLocalizationCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (RetentionMessageLocalizationCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessagelocalizationcreaterequest/data-data.dictionary)*