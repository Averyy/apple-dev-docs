# BetaTesterCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object BetaTesterCreateRequest.Data
```

## Topics

### Objects
- [object BetaTesterCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.
- [object BetaTesterCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (BetaTesterCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (BetaTesterCreateRequest.Data.Relationships): The types and IDs of the related data to update.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaTesters`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betatestercreaterequest/data-data.dictionary)*