# BetaGroupCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object BetaGroupCreateRequest.Data
```

## Topics

### Objects
- [object BetaGroupCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new beta group resource.
- [object BetaGroupCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (BetaGroupCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (BetaGroupCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaGroups`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betagroupcreaterequest/data-data.dictionary)*