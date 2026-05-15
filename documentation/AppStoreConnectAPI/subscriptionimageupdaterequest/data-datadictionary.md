# SubscriptionImageUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The request body you use to update a subscription purchase image reservation.

**Availability**:
- App Store Connect API 3.6+

## Declaration

```swift
object SubscriptionImageUpdateRequest.Data
```

## Topics

### Objects
- [object SubscriptionImageUpdateRequest.Data.Attributes](subscriptionimageupdaterequest/data-data.dictionary/attributes-data.dictionary.md)
  Attributes that describe a subscription image request resource.

## Properties

- `attributes` (SubscriptionImageUpdateRequest.Data.Attributes): The resource’s attributes.
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `subscriptionImages` resource ID from the [`List Subscription Images`](get-v1-subscriptions-_id_-images.md) response.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionimageupdaterequest/data-data.dictionary)*