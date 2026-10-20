# SubscriptionImageCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to create a subscription purchase image reservation.

**Availability**:
- App Store Connect API 3.6+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use [`SubscriptionImageV2CreateRequest`](../subscriptionimagev2createrequest.md) instead.

## Declaration

```
object SubscriptionImageCreateRequest.Data
```

## Topics

### Objects
- [object SubscriptionImageCreateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a subscription purchase image request resource.
- [object SubscriptionImageCreateRequest.Data.Relationships](./data-data.dictionary/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionImageCreateRequest.Data.Attributes) *(required)*: The resource’s attributes.
- `relationships` (SubscriptionImageCreateRequest.Data.Relationships) *(required)*: Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `subscriptionImages`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionimagecreaterequest/data-data.dictionary)*