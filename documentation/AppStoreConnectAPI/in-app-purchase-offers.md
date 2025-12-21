# In-App Purchase Offer Codes

**Framework**: App Store Connect API

Create and manage offers for in-app purchases, including one-time use offer codes and custom offer codes.

## Topics

### Creating and Managing In-App Purchase Offer Codes
- [Create an in-app purchase offer code](post-v1-inapppurchaseoffercodes.md)
  Create an offer code for an in-app purchase.
- [Read in-app purchase offer code information](get-v1-inapppurchaseoffercodes-_id_.md)
  Get information about a specific in-app purchase offer code.
- [Modify an in-app purchase offer code](patch-v1-inapppurchaseoffercodes-_id_.md)
  Update a specific in-app purchase offer code.
- [List all prices for an in-app purchase offer code](get-v1-inapppurchaseoffercodes-_id_-prices.md)
  Get a list of prices for a specific in-app purchase offer code.
- [Get all price IDs for an in-app purchase offer code](get-v1-inapppurchaseoffercodes-_id_-relationships-prices.md)
  Get a list of price resource IDs for a specific in-app purchase offer code.
### Managing One-Time Use Offer Codes
- [Create an in-app purchase offer code one-time use code](post-v1-inapppurchaseoffercodeonetimeusecodes.md)
  Create a one-time use code for an in-app purchase offer code.
- [Read in-app purchase offer code one-time use code information](get-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Get information about a specific in-app purchase offer code one-time use code.
- [Modify an in-app purchase offer code one-time use code](patch-v1-inapppurchaseoffercodeonetimeusecodes-_id_.md)
  Update a specific in-app purchase offer code one-time use code.
- [List all one-time use codes for an in-app purchase offer code](get-v1-inapppurchaseoffercodes-_id_-onetimeusecodes.md)
  Get a list of one-time use codes for a specific in-app purchase offer code.
- [List all values for an in-app purchase offer code one-time use code](get-v1-inapppurchaseoffercodeonetimeusecodes-_id_-values.md)
  Get a list of values for a specific in-app purchase offer code one-time use code.
- [Get all one-time use code IDs for an in-app purchase offer code](get-v1-inapppurchaseoffercodes-_id_-relationships-onetimeusecodes.md)
  Get a list of one-time use code resource IDs for a specific in-app purchase offer code.
### Managing Custom Offer Codes
- [Create an in-app purchase offer code custom code](post-v1-inapppurchaseoffercodecustomcodes.md)
  Create a custom code for an in-app purchase offer code.
- [List all custom codes for an in-app purchase offer code](get-v1-inapppurchaseoffercodes-_id_-customcodes.md)
  Get a list of custom codes for a specific in-app purchase offer code.
- [Get all custom code IDs for an in-app purchase offer code](get-v1-inapppurchaseoffercodes-_id_-relationships-customcodes.md)
  Get a list of custom code resource IDs for a specific in-app purchase offer code.
- [Read in-app purchase offer code custom code information](get-v1-inapppurchaseoffercodecustomcodes-_id_.md)
  Get information about a specific in-app purchase offer code custom code.
- [Modify an in-app purchase offer code custom code](patch-v1-inapppurchaseoffercodecustomcodes-_id_.md)
  Update a specific in-app purchase offer code custom code.
### Objects and Types
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