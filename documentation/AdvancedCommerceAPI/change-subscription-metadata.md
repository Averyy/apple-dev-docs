# Change Subscription Metadata

**Framework**: Advanced Commerce API  
**Kind**: httpRequest

Update the SKU, display name, and description associated with a subscription, without affecting the subscription’s billing or its service.

**Availability**:
- Advanced Commerce API 1.0+

## Mentions

- [Advanced Commerce API changelog](changelog.md)
- [Identifying rate limits for Advanced Commerce APIs](ratelimits.md)
- [Authorizing API requests from your server](authorizing-server-calls.md)

#### Discussion

Use this endpoint to update the display name and description of an auto-renewable subscription. Calling this endpoint doesn’t change the price, billing details, or the service. For example, you can call `Change Subscription Metadata` if a subscription’s display name changes due to a change in its branding.

Don’t call this endpoint if a customer is changing subscriptions to receive a different service, such as upgrading, downgrading, or cross-grading. For such changes, use [`SubscriptionModifyInAppRequest`](subscriptionmodifyinapprequest.md).

## Request Body

The request body that contains the metadata changes.

## See Also

- [object SubscriptionChangeMetadataRequest](subscriptionchangemetadatarequest.md)
  The request body you provide to change the metadata of a subscription.
- [object SubscriptionChangeMetadataResponse](subscriptionchangemetadataresponse.md)
  The response body for a successful subscription metadata change.
- [object SubscriptionChangeMetadataDescriptors](subscriptionchangemetadatadescriptors.md)
  The subscription metadata to change, specifically the description and display name.
- [object SubscriptionChangeMetadataItem](subscriptionchangemetadataitem.md)
  The metadata to change for an item, specifically its SKU, description, and display name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/change-subscription-metadata)*