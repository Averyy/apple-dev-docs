# Subscription Offer Codes

**Framework**: App Store Connect API

Create and manage subscription offers for auto-renewable subscriptions, including one-time use offer codes, and custom offer codes.

## Topics

### Creating and Managing Subscription Offers
- [Create a Subscription Offer](post-v1-subscriptionoffercodes.md)
  Create a subscription offer that provides offer codes for an auto-renewable subscription.
- [Read Subscription Offer Code Information](get-v1-subscriptionoffercodes-_id_.md)
  Get details about a specific subscription offer that has offer codes for an auto-renewable subscription.
- [Deactivate a Subscription Offer with Offer Codes](patch-v1-subscriptionoffercodes-_id_.md)
  Deactivate a subscription offer that has offer codes for an auto-renewable subscription.
- [List All Subscription Offer Code Prices](get-v1-subscriptionoffercodes-_id_-prices.md)
  Get a list of price tiers for a subscription offer code.
### Managing One-Time Use Offer Codes
- [Create One-Time Use Offer Codes](post-v1-subscriptionoffercodeonetimeusecodes.md)
  Create one-time use codes for an auto-renewable subscription offer.
- [Read One-Time Use Offer Code Information](get-v1-subscriptionoffercodeonetimeusecodes-_id_.md)
  Get details about a specific one-time use offer code for an auto-renewable subscription.
- [Deactivate One-Time Use Offer Codes](patch-v1-subscriptionoffercodeonetimeusecodes-_id_.md)
  Deactivate a batch of one-time use offer codes for an auto-renewable subscription.
- [List All One-Time Use Offer Codes for an Auto-Renewable Subscription](get-v1-subscriptionoffercodes-_id_-onetimeusecodes.md)
  Get details about a one-time use code for a specific subscription offer for an auto-renewable subscription.
- [List One-Time Use Offer Code Values](get-v1-subscriptionoffercodeonetimeusecodes-_id_-values.md)
  Get a list of one-time use offer codes for an auto-renewable subscription in CSV format.
### Managing Custom Offer Codes
- [Create Custom Offer Codes](post-v1-subscriptionoffercodecustomcodes.md)
  Create custom offer codes for an auto-renewable subscription offer.
- [List All Custom Offer Codes for an Auto-Renewable Subscription](get-v1-subscriptionoffercodes-_id_-customcodes.md)
  Get details about a custom code for a specific subscription offer for an auto-renewable subscription.
- [Read Custom Offer Code Information](get-v1-subscriptionoffercodecustomcodes-_id_.md)
  Get details about a specific offer code for an auto-renewable subscription.
- [Deactivate Custom Offer Codes](patch-v1-subscriptionoffercodecustomcodes-_id_.md)
  Deactivate a batch of custom offer codes for an auto-renewable subscription.
### Objects and Types
- [object SubscriptionOfferCodeResponse](subscriptionoffercoderesponse.md)
- [object SubscriptionOfferCode](subscriptionoffercode.md)
- [object SubscriptionOfferCodeCustomCodesResponse](subscriptionoffercodecustomcodesresponse.md)
- [object SubscriptionOfferCodeCustomCode](subscriptionoffercodecustomcode.md)
- [object SubscriptionOfferCodeOneTimeUseCodeValue](subscriptionoffercodeonetimeusecodevalue.md)
- [object SubscriptionOfferCodeOneTimeUseCodesResponse](subscriptionoffercodeonetimeusecodesresponse.md)
- [object SubscriptionOfferCodeOneTimeUseCode](subscriptionoffercodeonetimeusecode.md)
- [type csv](csv.md)
- [object SubscriptionOfferCodePricesResponse](subscriptionoffercodepricesresponse.md)
- [object SubscriptionOfferCodePrice](subscriptionoffercodeprice.md)
- [object SubscriptionOfferCodeCreateRequest](subscriptionoffercodecreaterequest.md)
- [object SubscriptionOfferCodeCustomCodeCreateRequest](subscriptionoffercodecustomcodecreaterequest.md)
- [object SubscriptionOfferCodeCustomCodeResponse](subscriptionoffercodecustomcoderesponse.md)
- [object SubscriptionOfferCodeCustomCodeUpdateRequest](subscriptionoffercodecustomcodeupdaterequest.md)
- [object SubscriptionOfferCodeOneTimeUseCodeCreateRequest](subscriptionoffercodeonetimeusecodecreaterequest.md)
- [object SubscriptionOfferCodeOneTimeUseCodeResponse](subscriptionoffercodeonetimeusecoderesponse.md)
- [object SubscriptionOfferCodeOneTimeUseCodeUpdateRequest](subscriptionoffercodeonetimeusecodeupdaterequest.md)
- [object SubscriptionOfferCodePriceInlineCreate](subscriptionoffercodepriceinlinecreate.md)
- [object SubscriptionOfferCodeUpdateRequest](subscriptionoffercodeupdaterequest.md)

## See Also

- [Subscription Introductory Offers](subscription-introductory-offers.md)
  Create, modify, and delete introductory offers for auto-renewable subscriptions.
- [Subscription Promotional Offers](subscription-promotional-offers.md)
  Create, modify, and delete promotional offers for auto-renewable subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-offer-codes)*