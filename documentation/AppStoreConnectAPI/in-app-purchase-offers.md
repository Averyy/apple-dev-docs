# In-App Purchase Offer Codes

**Framework**: App Store Connect API

Create and manage offers for in-app purchases, including one-time use offer codes and custom offer codes.

## Topics

### Creating and Managing In-App Purchase Offer Codes
- [Create an In-App Purchase Offer Code](post-v1-inapppurchaseoffercodes.md)
  Create an offer code for an in-app purchase.
- [Read In-App Purchase Offer Code Information](get-v1-inapppurchaseoffercodes-_id_.md)
  Get information about a specific in-app purchase offer code.
- [Modify an In-App Purchase Offer Code](patch-v1-inapppurchaseoffercodes-_id_.md)
  Update a specific in-app purchase offer code.
- [List All Prices for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-prices.md)
  Get a list of prices for a specific in-app purchase offer code.
- [Get All Price IDs for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific in-app purchase offer code.
### Managing One-Time Use Offer Codes
- [Create an In-App Purchase Offer Code One-Time Use Code](post-v1-inapppurchaseoffercodeonetimeusecodes.md)
  Create a one-time use code for an in-app purchase offer code.
- [Read In-App Purchase Offer Code One-Time Use Code Information](get-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Get information about a specific in-app purchase offer code one-time use code.
- [Modify an In-App Purchase Offer Code One-Time Use Code](patch-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Update a specific in-app purchase offer code one-time use code.
- [List All One-Time Use Codes for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-onetimeusecodes.md)
  Get a list of one-time use codes for a specific in-app purchase offer code.
- [List All Values for an In-App Purchase Offer Code One-Time Use Code](get-v1-inapppurchaseoffercodeonetimeusecodes-_id_-values.md)
  Get a list of values for a specific in-app purchase offer code one-time use code.
- [Get All One-Time Use Code IDs for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-relationships-onetimeusecodes.md)
  Get a list of one-time use code resource IDs for a specific in-app purchase offer code.
### Managing Custom Offer Codes
- [Create an In-App Purchase Offer Code Custom Code](post-v1-inapppurchaseoffercodecustomcodes.md)
  Create a custom code for an in-app purchase offer code.
- [List All Custom Codes for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-customcodes.md)
  Get a list of custom codes for a specific in-app purchase offer code.
- [Get All Custom Code IDs for an In-App Purchase Offer Code](get-v1-inapppurchaseoffercodes-_id_-relationships-customcodes.md)
  Get a list of custom code resource IDs for a specific in-app purchase offer code.
- [Read In-App Purchase Offer Code Custom Code Information](get-v1-inapppurchaseoffercodecustomcodes-_id_.md)
  Get information about a specific in-app purchase offer code custom code.
- [Modify an In-App Purchase Offer Code Custom Code](patch-v1-inapppurchaseoffercodecustomcodes-_id_.md)
  Update a specific in-app purchase offer code custom code.
### Objects and types
- [object InAppPurchaseOfferCodeResponse](inapppurchaseoffercoderesponse.md)
  A response that contains a single in-app purchase offer code resource.
- [object InAppPurchaseOfferCode](inapppurchaseoffercode.md)
  The data structure that represents an in-app purchase offer code resource.
- [object InAppPurchaseOfferCodeCustomCodesResponse](inapppurchaseoffercodecustomcodesresponse.md)
  A response that contains a list of in-app purchase offer code custom code resources.
- [object InAppPurchaseOfferCodeCustomCode](inapppurchaseoffercodecustomcode.md)
  The data structure that represents an in-app purchase offer code custom code resource.
- [object InAppPurchaseOfferCodeOneTimeUseCodeValue](inapppurchaseoffercodeonetimeusecodevalue.md)
  The data structure that represents an in-app purchase offer code one-time use code value resource.
- [object InAppPurchaseOfferCodeOneTimeUseCodesResponse](inapppurchaseoffercodeonetimeusecodesresponse.md)
  A response that contains a list of in-app purchase offer code one-time use code resources.
- [object InAppPurchaseOfferCodeOneTimeUseCode](inapppurchaseoffercodeonetimeusecode.md)
  The data structure that represents an in-app purchase offer code one-time use code resource.
- [object InAppPurchaseOfferCodePricesLinkagesResponse](inapppurchaseoffercodepriceslinkagesresponse.md)
  A response that contains a list of in-app purchase offer code prices linkage resources.
- [object InAppPurchaseOfferPrice](inapppurchaseofferprice.md)
  The data structure that represents an in-app purchase offer price resource.
- [object InAppPurchaseOfferPriceInlineCreate](inapppurchaseofferpriceinlinecreate.md)
  The data structure you use to configure an offer price when you create an in-app purchase offer code.
- [object InAppPurchaseOfferPricesResponse](inapppurchaseofferpricesresponse.md)
  A response that contains a list of in-app purchase offer price resources.
- [object InAppPurchaseOfferCodeCreateRequest](inapppurchaseoffercodecreaterequest.md)
  The request body you use to create an in-app purchase offer code.
- [object InAppPurchaseOfferCodeCustomCodeCreateRequest](inapppurchaseoffercodecustomcodecreaterequest.md)
  The request body you use to create an in-app purchase offer code custom code.
- [object InAppPurchaseOfferCodeCustomCodeResponse](inapppurchaseoffercodecustomcoderesponse.md)
  A response that contains a single in-app purchase offer code custom code resource.
- [object InAppPurchaseOfferCodeCustomCodeUpdateRequest](inapppurchaseoffercodecustomcodeupdaterequest.md)
  The request body you use to update an in-app purchase offer code custom code.
- [object InAppPurchaseOfferCodeOneTimeUseCodeCreateRequest](inapppurchaseoffercodeonetimeusecodecreaterequest.md)
  The request body you use to create an in-app purchase offer code one-time use code.
- [object InAppPurchaseOfferCodeOneTimeUseCodeResponse](inapppurchaseoffercodeonetimeusecoderesponse.md)
  A response that contains a single in-app purchase offer code one-time use code resource.
- [object InAppPurchaseOfferCodeOneTimeUseCodeUpdateRequest](inapppurchaseoffercodeonetimeusecodeupdaterequest.md)
  The request body you use to update an in-app purchase offer code one-time use code.
- [object InAppPurchaseOfferCodeUpdateRequest](inapppurchaseoffercodeupdaterequest.md)
  The request body you use to update an in-app purchase offer code.
- [object InAppPurchaseOfferCodeCustomCodesLinkagesResponse](inapppurchaseoffercodecustomcodeslinkagesresponse.md)
  A response that contains a list of in-app purchase offer code custom codes linkage resources.
- [object InAppPurchaseOfferCodeOneTimeUseCodeValuesLinkageResponse](inapppurchaseoffercodeonetimeusecodevalueslinkageresponse.md)
  A response that contains a single in-app purchase offer code one-time use code values linkage resource.
- [object InAppPurchaseOfferCodeOneTimeUseCodesLinkagesResponse](inapppurchaseoffercodeonetimeusecodeslinkagesresponse.md)
  A response that contains a list of in-app purchase offer code one-time use codes linkage resources.
- [object InAppPurchaseOfferCodesResponse](inapppurchaseoffercodesresponse.md)
  A response that contains a list of in-app purchase offer code resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/in-app-purchase-offers)*