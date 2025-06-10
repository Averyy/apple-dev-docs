# Subscriptions

**Framework**: App Store Connect API

Create, modify, and delete auto-renewable subscriptions for your app.

## Topics

### Endpoints
- [Create an Auto-Renewable Subscription](post-v1-subscriptions.md)
  Create an auto-renewable subscription for your app.
- [Read Subscription Information](get-v1-subscriptions-_id_.md)
  Get information about a specific auto-renewable subscription.
- [Modify an Auto-Renewable Subscription](patch-v1-subscriptions-_id_.md)
  Update a specific auto-renewable subscription.
- [Delete a Subscription](delete-v1-subscriptions-_id_.md)
  Delete a specific auto-renewable subscription that you configured for an app.
- [List All Localizations for an Auto-Renewable Subscription](get-v1-subscriptions-_id_-subscriptionlocalizations.md)
  Get a list of the subscription localizations for a specific auto-renewable subscription.
- [GET /v1/subscriptions/{id}/relationships/subscriptionLocalizations](get-v1-subscriptions-_id_-relationships-subscriptionlocalizations.md)
- [List All Introductory Offers for a Subscription](get-v1-subscriptions-_id_-introductoryoffers.md)
  Get a list of introductory offers for a specific auto-renewable subscription.
- [List All Introductory Offer Resource IDs for an Auto-Renewable Subscription](get-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Get a list of resource IDs representing introductory offers for an auto-renewable subscription.
- [Delete an Introductory Offer from a Subscription](delete-v1-subscriptions-_id_-relationships-introductoryoffers.md)
  Delete a specific introductory offer for an auto-renewable subscription.
- [Read Promoted Purchase Information for a Subscription](get-v1-subscriptions-_id_-promotedpurchase.md)
  Get details about the promoted purchase of an auto-renewable subscription.
- [GET /v1/subscriptions/{id}/relationships/promotedPurchase](get-v1-subscriptions-_id_-relationships-promotedpurchase.md)
- [List All Offer Codes for a Subscription](get-v1-subscriptions-_id_-offercodes.md)
  Get a list of subscription offer codes for a specific auto-renewable subscription.
- [GET /v1/subscriptions/{id}/relationships/offerCodes](get-v1-subscriptions-_id_-relationships-offercodes.md)
- [List All Promotional Offer Resource IDs for an Auto-Renewable Subscription](get-v1-subscriptions-_id_-promotionaloffers.md)
  Get a list of promotional offers for a specific auto-renewable subscription.
- [GET /v1/subscriptions/{id}/relationships/promotionalOffers](get-v1-subscriptions-_id_-relationships-promotionaloffers.md)
- [List All Price Points for a Subscription](get-v1-subscriptions-_id_-pricepoints.md)
  Get a list of price points for an auto-renewable subscription by territory.
- [GET /v1/subscriptions/{id}/relationships/pricePoints](get-v1-subscriptions-_id_-relationships-pricepoints.md)
- [List All Prices for a Subscription](get-v1-subscriptions-_id_-prices.md)
  Get a list of prices for an auto-renewable subscription, by territory.
- [List All Subscription Prices IDs for an Auto-Renewable Subscription](get-v1-subscriptions-_id_-relationships-prices.md)
  Get a list of resource IDs representing subscription prices for an auto-renewable subscription.
- [Delete Prices from a Subscription](delete-v1-subscriptions-_id_-relationships-prices.md)
  Delete a scheduled subscription price change for an auto-renewable subscription.
- [Read Review Screenshot Information for a Subscription](get-v1-subscriptions-_id_-appstorereviewscreenshot.md)
  Get information about review screenshot for a specific auto-renewable subscription.
- [GET /v1/subscriptions/{id}/relationships/appStoreReviewScreenshot](get-v1-subscriptions-_id_-relationships-appstorereviewscreenshot.md)
- [Read Information About the Availability of a Subscription](get-v1-subscriptions-_id_-subscriptionavailability.md)
  Get information about the territory availability for a subscription.
- [GET /v1/subscriptions/{id}/relationships/subscriptionAvailability](get-v1-subscriptions-_id_-relationships-subscriptionavailability.md)
- [List win-back offers](get-v1-subscriptions-_id_-winbackoffers.md)
  List all win-back offers for a specific subscription.
- [GET /v1/subscriptions/{id}/relationships/winBackOffers](get-v1-subscriptions-_id_-relationships-winbackoffers.md)
### Objects
- [object SubscriptionCreateRequest](subscriptioncreaterequest.md)
- [object SubscriptionUpdateRequest](subscriptionupdaterequest.md)
- [object SubscriptionResponse](subscriptionresponse.md)
- [object SubscriptionsResponse](subscriptionsresponse.md)
- [object Subscription](subscription.md)
- [object SubscriptionIntroductoryOffersResponse](subscriptionintroductoryoffersresponse.md)
- [object SubscriptionIntroductoryOffer](subscriptionintroductoryoffer.md)
- [object SubscriptionIntroductoryOffersLinkagesRequest](subscriptionintroductoryofferslinkagesrequest.md)
  The data structure that represents a subscription introductory offers linkages request resource.
- [object SubscriptionIntroductoryOffersLinkagesResponse](subscriptionintroductoryofferslinkagesresponse.md)
  A response that contains a list of Ids of related resources.
- [object SubscriptionOfferCodeResponse](subscriptionoffercoderesponse.md)
- [object SubscriptionOfferCodesResponse](subscriptionoffercodesresponse.md)
- [object SubscriptionOfferCode](subscriptionoffercode.md)
- [object PromotedPurchaseResponse](promotedpurchaseresponse.md)
- [object PromotedPurchase](promotedpurchase.md)
- [object SubscriptionPricePointsResponse](subscriptionpricepointsresponse.md)
- [object SubscriptionPricesResponse](subscriptionpricesresponse.md)
- [object SubscriptionPrice](subscriptionprice.md)
- [object SubscriptionPricesLinkagesRequest](subscriptionpriceslinkagesrequest.md)
  The data structure that represents a subscription prices linkages request resource.
- [object SubscriptionPricesLinkagesResponse](subscriptionpriceslinkagesresponse.md)
  A response that contains a list of Ids of related resources.
- [object SubscriptionLocalizationResponse](subscriptionlocalizationresponse.md)
- [object SubscriptionLocalizationsResponse](subscriptionlocalizationsresponse.md)
- [object SubscriptionLocalization](subscriptionlocalization.md)
- [object SubscriptionWinBackOffersLinkagesResponse](subscriptionwinbackofferslinkagesresponse.md)
- [object SubscriptionAppStoreReviewScreenshotLinkageResponse](subscriptionappstorereviewscreenshotlinkageresponse.md)
- [object SubscriptionPricePointEqualizationsLinkagesResponse](subscriptionpricepointequalizationslinkagesresponse.md)
- [object SubscriptionPricePointsLinkagesResponse](subscriptionpricepointslinkagesresponse.md)
- [object SubscriptionPromotedPurchaseLinkageResponse](subscriptionpromotedpurchaselinkageresponse.md)
- [object SubscriptionPromotionalOfferPricesLinkagesResponse](subscriptionpromotionalofferpriceslinkagesresponse.md)
- [object SubscriptionPromotionalOffersLinkagesResponse](subscriptionpromotionalofferslinkagesresponse.md)
- [object SubscriptionSubscriptionAvailabilityLinkageResponse](subscriptionsubscriptionavailabilitylinkageresponse.md)
- [object SubscriptionSubscriptionLocalizationsLinkagesResponse](subscriptionsubscriptionlocalizationslinkagesresponse.md)
- [object SubscriptionWinBackOffersLinkagesResponse](subscriptionwinbackofferslinkagesresponse.md)

## See Also

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
  Create and manage subscriptions with the App Store Connect API.
- [Subscription Localizations](subscription-localizations.md)
  Create, modify, and delete localized metadata for auto-renewable subscriptions.
- [Subscription Price Points and Subscription Prices](subscription-price-points-and-subscription-prices.md)
  Manage scheduled price changes for auto-renewable subscriptions and get price point information.
- [Subscription images](subscription-images.md)
  Create, modify, and delete promotion images for your auto-renewalable subscription.
- [Subscription availability](subscription-availability.md)
  Read and modify territory availability for an auto-renewable subscription.
- [Billing Grace Periods](billing-grace-periods.md)
  Get information about the grace period and modify the opt-in value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptions)*