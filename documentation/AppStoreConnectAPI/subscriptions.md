# Subscriptions

**Framework**: App Store Connect API

Create, modify, and delete auto-renewable subscriptions for your app.

## Topics

### Configuring Subscription Prices
- [Configuring subscription prices across territories](configuring-subscription-prices-across-territories.md)
  Set plan types and equalized prices for an auto-renewable subscription with the App Store Connect API.
### Creating and managing subscriptions
- [Create an auto-renewable subscription](post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Read subscription information](get-v1-subscriptions-_id_.md)
  Get information about a specific auto-renewable subscription.
- [Modify an auto-renewable subscription](patch-v1-subscriptions-_id_.md)
  Update a specific auto-renewable subscription.
- [Delete a subscription](delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.
### Getting subscription localizations
- [List all localizations for an auto-renewable subscription](get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [List localization IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-subscriptionlocalizations.md)
### Getting introductory offers
- [List all introductory offers for a subscription](get-v1-subscriptions-_id_-introductoryoffers.md)
  Get a list of introductory offers for a specific auto-renewable subscription.
- [List all introductory offer resource ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Get a list of resource IDs representing introductory offers for an auto-renewable subscription.
- [Delete an introductory offer from a subscription](delete-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Delete a specific introductory offer for an auto-renewable subscription.
### Getting promotional offers
- [List all promotional offer resource ids for an auto-renewable subscription](get-v1-subscriptions-_id_-promotionaloffers.md)
  Get a list of promotional offers for a specific auto-renewable subscription.
- [List promotional offer IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-promotionaloffers.md)
### Getting offer codes
- [List all offer codes for a subscription](get-v1-subscriptions-_id_-offercodes.md)
  Get a list of subscription offer codes for a specific auto-renewable subscription.
- [List offer code IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-offercodes.md)
### Getting win-back offers
- [List Win-Back Offers](get-v1-subscriptions-_id_-winbackoffers.md)
  The data structure that represents a get-v1-subscriptions-{id}-win back offers resource.
- [List win-back offer IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
### Getting the promoted purchase
- [Read promoted purchase information for a subscription](get-v1-subscriptions-_id_-promotedpurchase.md)
  Get details about the promoted purchase of an auto-renewable subscription.
- [Get the promoted purchase ID for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-promotedpurchase.md)
### Getting price points and prices
- [List all price points for a subscription](get-v1-subscriptions-_id_-pricepoints.md)
  Get a list of price points for an auto-renewable subscription by territory.
- [List price point IDs for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-pricepoints.md)
- [List all prices for a subscription](get-v1-subscriptions-_id_-prices.md)
  Get a list of prices for an auto-renewable subscription, by territory.
- [List all subscription price ids for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-prices.md)
  Get a list of resource IDs representing subscription prices for an auto-renewable subscription.
- [Delete prices from a subscription](delete-v1-subscriptions-_id_-relationships-prices.md)
  Delete a scheduled subscription price change for an auto-renewable subscription.
### Getting subscription availability
- [Read information about the availability of a subscription](get-v1-subscriptions-_id_-subscriptionavailability.md)
  Get information about the territory availability for a subscription.
- [Get the subscription availability ID for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-subscriptionavailability.md)
- [List plan availabilities for a subscription](get-v1-subscriptions-_id_-planavailabilities.md)
  List all plan availabilities for a specific auto-renewable subscription.
- [List plan availability IDs for a subscription](get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  Get a list of plan availability resource IDs for a specific auto-renewable subscription.
### Getting the App Store review screenshot
- [Read review screenshot information for a subscription](get-v1-subscriptions-_id_-appstorereviewscreenshot.md)
  Get information about review screenshot for a specific auto-renewable subscription.
- [Get the App Store review screenshot ID for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-appstorereviewscreenshot.md)
### Objects and data types
- [object SubscriptionCreateRequest](subscriptioncreaterequest.md)
  The request body you use to create a subscription.
- [object SubscriptionUpdateRequest](subscriptionupdaterequest.md)
  The request body you use to update a subscription update request.
- [object SubscriptionResponse](subscriptionresponse.md)
  The response body for endpoints that create, read, or modify a single auto-renewable subscription.
- [object SubscriptionsResponse](subscriptionsresponse.md)
  The response body for endpoints that list auto-renewable subscriptions in a subscription group.
- [object Subscription](subscription.md)
  An auto-renewable subscription product offered within an app, with configurable pricing, duration, and promotional offers.
- [object SubscriptionIntroductoryOffersResponse](subscriptionintroductoryoffersresponse.md)
  The response body for endpoints that list introductory offers for a subscription.
- [object SubscriptionIntroductoryOffer](subscriptionintroductoryoffer.md)
  A discounted price or free trial period offered to new subscribers of an auto-renewable subscription.
- [object SubscriptionIntroductoryOffersLinkagesRequest](subscriptionintroductoryofferslinkagesrequest.md)
  The request body for updating the list of introductory offers linked to a subscription.
- [object SubscriptionIntroductoryOffersLinkagesResponse](subscriptionintroductoryofferslinkagesresponse.md)
  A response containing the resource identifiers of introductory offers linked to a subscription.
- [object SubscriptionOfferCodeResponse](subscriptionoffercoderesponse.md)
  The response body for endpoints that create, read, or modify a single subscription offer code.
- [object SubscriptionOfferCodesResponse](subscriptionoffercodesresponse.md)
  The response body for endpoints that list offer codes for a subscription.
- [object SubscriptionOfferCode](subscriptionoffercode.md)
  A promotional code that gives customers a discounted or free subscription for a specified duration and eligibility group.
- [object PromotedPurchaseResponse](promotedpurchaseresponse.md)
  The response body for endpoints that read or modify a promoted in-app purchase or subscription.
- [object PromotedPurchase](promotedpurchase.md)
  An in-app purchase or subscription configured to appear on the app’s App Store product page.
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
  The response body for endpoints that list available price points for a subscription.
- [object SubscriptionPricesResponse](subscriptionpricesresponse.md)
  The response body for endpoints that list scheduled prices for a subscription.
- [object SubscriptionPrice](subscriptionprice.md)
  A configured price for an auto-renewable subscription in a specific App Store territory.
- [object SubscriptionPricesLinkagesRequest](subscriptionpriceslinkagesrequest.md)
  The request body for updating the list of prices linked to a subscription.
- [object SubscriptionPricesLinkagesResponse](subscriptionpriceslinkagesresponse.md)
  A response containing the resource identifiers of prices linked to a subscription.
- [object SubscriptionLocalizationResponse](subscriptionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single subscription localization.
- [object SubscriptionLocalizationsResponse](subscriptionlocalizationsresponse.md)
  The response body for endpoints that list localizations for a subscription.
- [object SubscriptionLocalization](subscriptionlocalization.md)
  The localized display name and description for an auto-renewable subscription shown to customers on the App Store.
- [object SubscriptionWinBackOffersLinkagesResponse](subscriptionwinbackofferslinkagesresponse.md)
- [object SubscriptionAppStoreReviewScreenshotLinkageResponse](subscriptionappstorereviewscreenshotlinkageresponse.md)
- [object SubscriptionPricePointEqualizationsLinkagesResponse](subscriptionpricepointequalizationslinkagesresponse.md)
- [object SubscriptionPricePointsLinkagesResponse](subscriptionpricepointslinkagesresponse.md)
- [object SubscriptionPromotedPurchaseLinkageResponse](subscriptionpromotedpurchaselinkageresponse.md)
- [object SubscriptionPromotionalOfferPricesLinkagesResponse](subscriptionpromotionalofferpriceslinkagesresponse.md)
- [object SubscriptionPromotionalOffersLinkagesResponse](subscriptionpromotionalofferslinkagesresponse.md)
- [object SubscriptionSubscriptionAvailabilityLinkageResponse](subscriptionsubscriptionavailabilitylinkageresponse.md)
- [object SubscriptionSubscriptionLocalizationsLinkagesResponse](subscriptionsubscriptionlocalizationslinkagesresponse.md)

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
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription localizations (v1)](subscription-localizations-v1.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription price points and subscription prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for auto-renewable subscriptions.
- [Subscription images (v1)](subscription-images-v1.md)
  Create, modify, and delete promotion images for your auto-renewable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Subscription plan availability](subscription-plan-availability.md)
  Create and manage subscription plan availability for auto-renewable subscriptions.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptions)*