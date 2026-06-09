# Read promoted purchase information for an in-app purchase

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get details about the promoted purchase of an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)
- [Managing in-app purchases](managing-in-app-purchases.md)

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/inAppPurchases/{id}/promotedPurchase`

## Parameters

- `fields[inAppPurchases]` ([string])
- `fields[promotedPurchases]` ([string])
- `fields[subscriptions]` ([string])
- `include` ([string])

## See Also

- [Create an in-app purchase](post-v2-inapppurchases.md)
  Create an in-app purchase, including a consumable, non-consumable, or non-renewing subscription.
- [Read in-app purchase information](get-v2-inapppurchases-_id_.md)
  Get information about a specific in-app purchase.
- [List all in-app purchases for an app](get-v1-apps-_id_-inapppurchasesv2.md)
  Get a list of the in-app purchases for a specific app.
- [Modify an in-app purchase](patch-v2-inapppurchases-_id_.md)
  Update the reference name of a specific in-app purchase.
- [Delete an in-app purchase](delete-v2-inapppurchases-_id_.md)
  Delete a specific in-app purchase from your app.
- [List all price points for an in-app purchase](get-v2-inapppurchases-_id_-pricepoints.md)
  Get a list of possible price points for an in-app purchase.
- [List price point IDs for an in-app purchase](get-v2-inapppurchases-_id_-relationships-pricepoints.md)
  Get a list of price point IDs for a specific in-app purchase.
- [List All In-App Purchase Price Point Equalizations](get-v1-inapppurchasepricepoints-_id_-equalizations.md)
  Get a list of in-app purchase price points and their equivalent in a specified currency.
- [List equalization IDs for an in-app purchase price point](get-v1-inapppurchasepricepoints-_id_-relationships-equalizations.md)
- [Read the promoted purchase ID for an in-app purchase](get-v2-inapppurchases-_id_-relationships-promotedpurchase.md)
  Get the promoted purchase ID for a specific in-app purchase.
- [List all localizations for an in-app purchase](get-v2-inapppurchases-_id_-inapppurchaselocalizations.md)
  Get a list of localized display names and descriptions for a specific in-app purchase.
- [List localization IDs for an in-app purchase](get-v2-inapppurchases-_id_-relationships-inapppurchaselocalizations.md)
  Get a list of localization IDs for a specific in-app purchase.
- [Read review screenshot information for an in-app purchase](get-v2-inapppurchases-_id_-appstorereviewscreenshot.md)
  Get information about a review screenshot for a specific in-app purchase.
- [Read the App Store review screenshot ID for an in-app purchase](get-v2-inapppurchases-_id_-relationships-appstorereviewscreenshot.md)
  Get the App Store review screenshot ID for a specific in-app purchase.
- [Create a review submission for an in-app purchase](post-v1-inapppurchasesubmissions.md)
  Create an in-app purchase submission for review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-inapppurchases-_id_-promotedpurchase)*