# SubscriptionChangeMetadataResponse

**Framework**: Advanced Commerce API  
**Kind**: dictionary

The response body for a successful subscription metadata change.

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```swift
object SubscriptionChangeMetadataResponse
```

#### Discussion

This is the response body for the [`Change Subscription Metadata`](change-subscription-metadata.md) endpoint.

## Properties

- `signedRenewalInfo` (JWSRenewalInfo) *(required)*: Subscription renewal information signed by the App Store, in JSON Web Signature (JWS) format.
- `signedTransactionInfo` (JWSTransaction) *(required)*: Transaction information signed by the App Store, in JWS Compact Serialization format.

## See Also

- [Change Subscription Metadata](change-subscription-metadata.md)
  Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.
- [object SubscriptionChangeMetadataRequest](subscriptionchangemetadatarequest.md)
  The request body you provide to change the metadata of a subscription.
- [object SubscriptionChangeMetadataDescriptors](subscriptionchangemetadatadescriptors.md)
  The subscription metadata to change, specifically the description and display name.
- [object SubscriptionChangeMetadataItem](subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionchangemetadataresponse)*