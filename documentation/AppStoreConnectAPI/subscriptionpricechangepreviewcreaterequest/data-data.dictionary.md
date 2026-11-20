# SubscriptionPriceChangePreviewCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 4.6.1+

## Declaration

```
object SubscriptionPriceChangePreviewCreateRequest.Data
```

## Topics

### Objects
- [object SubscriptionPriceChangePreviewCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  The attributes you include in the request.
- [object SubscriptionPriceChangePreviewCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `subscriptionPriceChangePreviews`
- `attributes` (SubscriptionPriceChangePreviewCreateRequest.Data.Attributes): The resource’s attributes.
- `relationships` (SubscriptionPriceChangePreviewCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionpricechangepreviewcreaterequest/data-data.dictionary)*