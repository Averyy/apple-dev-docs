# Subscription images (v1)

**Framework**: App Store Connect API

Create, modify, and delete promotion images for your auto-renewable subscription.

**Availability**:
- App Store Connect API 3.6+

#### Overview

> ❗ **Important**:  This is deprecated. Use [`Subscription images`](subscription-images.md) instead.

## Topics

### Endpoints
- [Create an image for a subscription (v1)](post-v1-subscriptionimages.md)
  Reserve an image asset to appear in the App Store, representing a subscription.
- [Read subscription image information (v1)](get-v1-subscriptionimages-_id_.md)
  Read details about a specific subscription image.
- [List Subscription Images](get-v1-subscriptions-_id_-images.md)
  List all images for a specific subscription.
- [List subscription image ids](get-v1-subscriptions-_id_-relationships-images.md)
  List all images IDs for a specific subscription.
- [Commit a subscription image (v1)](patch-v1-subscriptionimages-_id_.md)
  Commit an uploaded subscription image.
- [Delete a subscription image (v1)](delete-v1-subscriptionimages-_id_.md)
  Delete the image asset that appears on the App Store listing that represents a subscription.
### Objects
- [object SubscriptionImage](subscriptionimage.md)
  An image used to represent a subscription product on the App Store product page.
- [object SubscriptionImageCreateRequest](subscriptionimagecreaterequest.md)
  The request body you use to create a subscription purchase image reservation.
- [object SubscriptionImageResponse](subscriptionimageresponse.md)
  A response containing a single subscription product image.
- [object SubscriptionImagesResponse](subscriptionimagesresponse.md)
  A response containing a list of images for a subscription product.
- [object SubscriptionImageUpdateRequest](subscriptionimageupdaterequest.md)
  The request body for updating the upload status or content of a subscription product image.
- [object SubscriptionImagesLinkagesResponse](subscriptionimageslinkagesresponse.md)

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Working with subscription versions](working-with-subscription-versions.md)
  Manage draft versions of an auto-renewable subscription’s localized metadata and review images before submitting for App Review.
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
- [Querying adjusted subscription price equalizations](querying-adjusted-subscription-price-equalizations.md)
  Compare a subscription price point against the equalized price points that Apple recommends across territories, adjusted for local pricing rules.
- [Subscription Versions](subscription-versions.md)
  Create and read draft versions of an auto-renewable subscription, with their localized metadata and review images.
- [Subscriptions](subscriptions.md)
  Create, modify, and delete auto-renewable subscriptions for your app.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-images-v1)*