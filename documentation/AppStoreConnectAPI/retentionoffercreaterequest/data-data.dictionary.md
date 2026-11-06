# RetentionOfferCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOfferCreateRequest.Data
```

## Topics

### Objects
- [object RetentionOfferCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.
- [object RetentionOfferCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionOffers`
- `attributes` (RetentionOfferCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (RetentionOfferCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionoffercreaterequest/data-data.dictionary)*