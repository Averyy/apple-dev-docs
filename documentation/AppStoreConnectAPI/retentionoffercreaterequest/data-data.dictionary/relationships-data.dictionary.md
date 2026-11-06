# RetentionOfferCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships to other resources that you can set with this request.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOfferCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object RetentionOfferCreateRequest.Data.Relationships.Subscription](./relationships-data.dictionary/subscription-data.dictionary.md)
  The relationships to other resources that you can set with this request.
- [object RetentionOfferCreateRequest.Data.Relationships.Prices](./relationships-data.dictionary/prices-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `subscription` (RetentionOfferCreateRequest.Data.Relationships.Subscription) *(required)*: The auto-renewable subscription to create the offer for.
- `prices` (RetentionOfferCreateRequest.Data.Relationships.Prices) *(required)*: The territory-specific prices for the offer. Provide the prices as inline resources in the request’s included array.

## See Also

### Objects
- [object RetentionOfferCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  Attributes that you set that describe the new resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionoffercreaterequest/data-data.dictionary/relationships-data.dictionary)*